import { useState, useRef, useEffect } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { 
  Mic, 
  MicOff, 
  Volume2, 
  VolumeX,
  MessageCircle,
  Loader2,
  Play,
  Pause,
  RotateCcw,
  Bot
} from 'lucide-react'

export function VoiceChatbot() {
  const [isListening, setIsListening] = useState(false)
  const [isPlaying, setIsPlaying] = useState(false)
  const [isMuted, setIsMuted] = useState(false)
  const [isLoading, setIsLoading] = useState(false)
  const [conversationId, setConversationId] = useState(null)
  const [messages, setMessages] = useState([])
  const [currentMessage, setCurrentMessage] = useState('')
  const [isConnected, setIsConnected] = useState(false)

  const audioRef = useRef(null)
  const recognitionRef = useRef(null)

  // Inicializar reconhecimento de voz
  useEffect(() => {
    if ('webkitSpeechRecognition' in window || 'SpeechRecognition' in window) {
      const SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition
      recognitionRef.current = new SpeechRecognition()
      recognitionRef.current.continuous = false
      recognitionRef.current.interimResults = false
      recognitionRef.current.lang = 'pt-BR'

      recognitionRef.current.onresult = (event) => {
        const transcript = event.results[0][0].transcript
        setCurrentMessage(transcript)
        sendMessageToAnna(transcript)
      }

      recognitionRef.current.onerror = (event) => {
        console.error('Erro no reconhecimento de voz:', event.error)
        setIsListening(false)
      }

      recognitionRef.current.onend = () => {
        setIsListening(false)
      }
    }
  }, [])

  const startConversation = async () => {
    setIsLoading(true)
    try {
      const response = await fetch('http://localhost:5000/api/elevenlabs/anna-agent/start-conversation', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        }
      })

      const data = await response.json()
      
      if (data.success) {
        setConversationId(data.conversation_id)
        setIsConnected(true)
        setMessages([{
          type: 'system',
          content: 'Conversa iniciada com Anna, sua assistente de negócios!',
          timestamp: new Date().toLocaleTimeString()
        }])
      } else {
        console.error('Erro ao iniciar conversa:', data.error)
      }
    } catch (error) {
      console.error('Erro na requisição:', error)
    } finally {
      setIsLoading(false)
    }
  }

  const sendMessageToAnna = async (message) => {
    if (!conversationId || !message.trim()) return

    setIsLoading(true)
    
    // Adicionar mensagem do usuário
    const userMessage = {
      type: 'user',
      content: message,
      timestamp: new Date().toLocaleTimeString()
    }
    setMessages(prev => [...prev, userMessage])

    try {
      const response = await fetch('http://localhost:5000/api/elevenlabs/anna-agent/send-message', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({
          conversation_id: conversationId,
          message: message
        })
      })

      const data = await response.json()
      
      if (data.success) {
        // Adicionar resposta da Anna
        const annaMessage = {
          type: 'assistant',
          content: data.response_text,
          audio_url: data.audio_url,
          timestamp: new Date().toLocaleTimeString()
        }
        setMessages(prev => [...prev, annaMessage])

        // Reproduzir áudio se disponível
        if (data.audio_url && !isMuted) {
          playAudio(data.audio_url)
        }
      } else {
        console.error('Erro ao enviar mensagem:', data.error)
      }
    } catch (error) {
      console.error('Erro na requisição:', error)
    } finally {
      setIsLoading(false)
      setCurrentMessage('')
    }
  }

  const playAudio = (audioUrl) => {
    if (audioRef.current) {
      audioRef.current.src = audioUrl
      audioRef.current.play()
      setIsPlaying(true)
    }
  }

  const startListening = () => {
    if (recognitionRef.current && !isListening) {
      setIsListening(true)
      recognitionRef.current.start()
    }
  }

  const stopListening = () => {
    if (recognitionRef.current && isListening) {
      recognitionRef.current.stop()
      setIsListening(false)
    }
  }

  const toggleMute = () => {
    setIsMuted(!isMuted)
    if (audioRef.current) {
      audioRef.current.muted = !isMuted
    }
  }

  const resetConversation = () => {
    setConversationId(null)
    setIsConnected(false)
    setMessages([])
    setCurrentMessage('')
  }

  const handleSendText = () => {
    if (currentMessage.trim()) {
      sendMessageToAnna(currentMessage)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      handleSendText()
    }
  }

  return (
    <div className="space-y-6">
      {/* Header */}
      <Card className="border-purple-200 bg-gradient-to-r from-purple-50 to-pink-50">
        <CardHeader>
          <CardTitle className="flex items-center gap-2 text-purple-800">
            <Bot className="h-6 w-6" />
            Anna - Assistente de Voz para Negócios
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex items-center justify-between">
            <div>
              <p className="text-purple-700 mb-2">
                Converse por voz com Anna, sua assistente especializada em empreendedorismo!
              </p>
              <div className="flex items-center gap-2">
                <Badge variant={isConnected ? "default" : "secondary"}>
                  {isConnected ? 'Conectado' : 'Desconectado'}
                </Badge>
                {isListening && (
                  <Badge variant="destructive" className="animate-pulse">
                    Ouvindo...
                  </Badge>
                )}
              </div>
            </div>
            
            <div className="flex items-center gap-2">
              <Button
                onClick={toggleMute}
                variant="outline"
                size="icon"
                className={isMuted ? 'text-red-600' : 'text-green-600'}
              >
                {isMuted ? <VolumeX className="h-4 w-4" /> : <Volume2 className="h-4 w-4" />}
              </Button>
              
              <Button
                onClick={resetConversation}
                variant="outline"
                size="icon"
                disabled={!isConnected}
              >
                <RotateCcw className="h-4 w-4" />
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Connection */}
      {!isConnected && (
        <Card>
          <CardContent className="p-6 text-center">
            <Bot className="h-12 w-12 mx-auto mb-4 text-purple-600" />
            <h3 className="text-lg font-semibold mb-2">Iniciar Conversa com Anna</h3>
            <p className="text-gray-600 mb-4">
              Clique no botão abaixo para começar a conversar com sua assistente de negócios.
            </p>
            <Button
              onClick={startConversation}
              disabled={isLoading}
              className="bg-purple-600 hover:bg-purple-700"
            >
              {isLoading ? (
                <Loader2 className="h-4 w-4 animate-spin mr-2" />
              ) : (
                <MessageCircle className="h-4 w-4 mr-2" />
              )}
              {isLoading ? 'Conectando...' : 'Iniciar Conversa'}
            </Button>
          </CardContent>
        </Card>
      )}

      {/* Voice Controls */}
      {isConnected && (
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <Mic className="h-5 w-5" />
              Controles de Voz
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="flex items-center gap-4 mb-4">
              <Button
                onClick={isListening ? stopListening : startListening}
                disabled={isLoading}
                className={`${isListening ? 'bg-red-600 hover:bg-red-700' : 'bg-blue-600 hover:bg-blue-700'} flex-1`}
              >
                {isListening ? (
                  <MicOff className="h-4 w-4 mr-2" />
                ) : (
                  <Mic className="h-4 w-4 mr-2" />
                )}
                {isListening ? 'Parar de Ouvir' : 'Falar com Anna'}
              </Button>
            </div>

            {/* Text Input Alternative */}
            <div className="space-y-2">
              <label className="text-sm font-medium text-gray-700">
                Ou digite sua mensagem:
              </label>
              <div className="flex gap-2">
                <textarea
                  value={currentMessage}
                  onChange={(e) => setCurrentMessage(e.target.value)}
                  onKeyPress={handleKeyPress}
                  placeholder="Digite sua pergunta sobre negócios..."
                  className="flex-1 px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-purple-500 resize-none"
                  rows={2}
                  disabled={isLoading}
                />
                <Button
                  onClick={handleSendText}
                  disabled={!currentMessage.trim() || isLoading}
                  className="bg-purple-600 hover:bg-purple-700"
                >
                  {isLoading ? (
                    <Loader2 className="h-4 w-4 animate-spin" />
                  ) : (
                    <MessageCircle className="h-4 w-4" />
                  )}
                </Button>
              </div>
            </div>
          </CardContent>
        </Card>
      )}

      {/* Chat Messages */}
      {messages.length > 0 && (
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <MessageCircle className="h-5 w-5" />
              Conversa
            </CardTitle>
          </CardHeader>
          <CardContent>
            <div className="space-y-4 max-h-96 overflow-y-auto">
              {messages.map((message, index) => (
                <div
                  key={index}
                  className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}
                >
                  <div
                    className={`max-w-xs lg:max-w-md px-4 py-2 rounded-lg ${
                      message.type === 'user'
                        ? 'bg-blue-600 text-white'
                        : message.type === 'assistant'
                        ? 'bg-purple-100 text-purple-900'
                        : 'bg-gray-100 text-gray-700'
                    }`}
                  >
                    <p className="text-sm">{message.content}</p>
                    <p className="text-xs opacity-70 mt-1">{message.timestamp}</p>
                    
                    {message.audio_url && (
                      <Button
                        onClick={() => playAudio(message.audio_url)}
                        variant="ghost"
                        size="sm"
                        className="mt-2 p-1 h-auto"
                      >
                        <Play className="h-3 w-3 mr-1" />
                        Reproduzir
                      </Button>
                    )}
                  </div>
                </div>
              ))}
            </div>
          </CardContent>
        </Card>
      )}

      {/* Hidden Audio Element */}
      <audio
        ref={audioRef}
        onPlay={() => setIsPlaying(true)}
        onPause={() => setIsPlaying(false)}
        onEnded={() => setIsPlaying(false)}
        muted={isMuted}
      />
    </div>
  )
}

