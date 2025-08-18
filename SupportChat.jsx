import { useState, useEffect, useRef } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { 
  MessageCircle, 
  Send, 
  Bot,
  User,
  Search,
  HelpCircle,
  ChevronDown,
  ChevronUp,
  Loader2
} from 'lucide-react'

export function SupportChat() {
  const [messages, setMessages] = useState([])
  const [currentMessage, setCurrentMessage] = useState('')
  const [isLoading, setIsLoading] = useState(false)
  const [showFAQ, setShowFAQ] = useState(true)
  const [faqData, setFaqData] = useState([])
  const [searchQuery, setSearchQuery] = useState('')
  const [filteredFAQ, setFilteredFAQ] = useState([])
  const [isConnected, setIsConnected] = useState(false)

  const messagesEndRef = useRef(null)

  // Carregar FAQ ao montar o componente
  useEffect(() => {
    loadFAQ()
    initializeChat()
  }, [])

  // Auto-scroll para a última mensagem
  useEffect(() => {
    scrollToBottom()
  }, [messages])

  // Filtrar FAQ baseado na busca
  useEffect(() => {
    if (searchQuery.trim()) {
      const filtered = faqData.filter(item =>
        item.question.toLowerCase().includes(searchQuery.toLowerCase()) ||
        item.answer.toLowerCase().includes(searchQuery.toLowerCase()) ||
        item.category.toLowerCase().includes(searchQuery.toLowerCase())
      )
      setFilteredFAQ(filtered)
    } else {
      setFilteredFAQ(faqData)
    }
  }, [searchQuery, faqData])

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: 'smooth' })
  }

  const loadFAQ = async () => {
    try {
      const response = await fetch('http://localhost:5000/api/streamchat/faq')
      const data = await response.json()
      
      if (data.success) {
        setFaqData(data.faq)
        setFilteredFAQ(data.faq)
      }
    } catch (error) {
      console.error('Erro ao carregar FAQ:', error)
    }
  }

  const initializeChat = () => {
    setIsConnected(true)
    setMessages([{
      type: 'bot',
      content: 'Olá! Sou o assistente de suporte do abbā. Como posso ajudar você hoje? Você pode perguntar sobre qualquer funcionalidade do aplicativo ou consultar as perguntas frequentes abaixo.',
      timestamp: new Date().toLocaleTimeString()
    }])
  }

  const sendMessage = async () => {
    if (!currentMessage.trim()) return

    const userMessage = {
      type: 'user',
      content: currentMessage,
      timestamp: new Date().toLocaleTimeString()
    }

    setMessages(prev => [...prev, userMessage])
    setIsLoading(true)

    try {
      // Obter resposta do bot
      const response = await fetch('http://localhost:5000/api/streamchat/bot-response', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ message: currentMessage })
      })

      const data = await response.json()
      
      if (data.success) {
        const botMessage = {
          type: 'bot',
          content: data.response,
          timestamp: new Date().toLocaleTimeString(),
          isAutomated: data.is_automated
        }
        setMessages(prev => [...prev, botMessage])
      }
    } catch (error) {
      console.error('Erro ao enviar mensagem:', error)
      const errorMessage = {
        type: 'bot',
        content: 'Desculpe, ocorreu um erro. Tente novamente em alguns instantes.',
        timestamp: new Date().toLocaleTimeString()
      }
      setMessages(prev => [...prev, errorMessage])
    } finally {
      setIsLoading(false)
      setCurrentMessage('')
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter' && !e.shiftKey) {
      e.preventDefault()
      sendMessage()
    }
  }

  const selectFAQItem = (item) => {
    setCurrentMessage(item.question)
    setShowFAQ(false)
  }

  const categories = [...new Set(faqData.map(item => item.category))]

  return (
    <div className="space-y-6">
      {/* Header */}
      <Card className="border-green-200 bg-gradient-to-r from-green-50 to-blue-50">
        <CardHeader>
          <CardTitle className="flex items-center gap-2 text-green-800">
            <MessageCircle className="h-6 w-6" />
            Suporte e Tutorial - abbā
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="flex items-center justify-between">
            <div>
              <p className="text-green-700 mb-2">
                Precisa de ajuda? Converse conosco ou consulte as perguntas frequentes!
              </p>
              <Badge variant={isConnected ? "default" : "secondary"}>
                {isConnected ? 'Chat Ativo' : 'Desconectado'}
              </Badge>
            </div>
            
            <Button
              onClick={() => setShowFAQ(!showFAQ)}
              variant="outline"
              className="flex items-center gap-2"
            >
              <HelpCircle className="h-4 w-4" />
              FAQ
              {showFAQ ? <ChevronUp className="h-4 w-4" /> : <ChevronDown className="h-4 w-4" />}
            </Button>
          </div>
        </CardContent>
      </Card>

      {/* FAQ Section */}
      {showFAQ && (
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <HelpCircle className="h-5 w-5" />
              Perguntas Frequentes
            </CardTitle>
          </CardHeader>
          <CardContent>
            {/* Search FAQ */}
            <div className="mb-4">
              <div className="flex gap-2">
                <div className="relative flex-1">
                  <Search className="absolute left-3 top-1/2 transform -translate-y-1/2 h-4 w-4 text-gray-400" />
                  <input
                    type="text"
                    placeholder="Buscar nas perguntas frequentes..."
                    className="w-full pl-10 pr-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500"
                    value={searchQuery}
                    onChange={(e) => setSearchQuery(e.target.value)}
                  />
                </div>
              </div>
            </div>

            {/* Categories */}
            <div className="mb-4">
              <div className="flex flex-wrap gap-2">
                <Button
                  variant={searchQuery === '' ? "default" : "outline"}
                  size="sm"
                  onClick={() => setSearchQuery('')}
                >
                  Todas
                </Button>
                {categories.map(category => (
                  <Button
                    key={category}
                    variant="outline"
                    size="sm"
                    onClick={() => setSearchQuery(category)}
                  >
                    {category}
                  </Button>
                ))}
              </div>
            </div>

            {/* FAQ Items */}
            <div className="space-y-3 max-h-96 overflow-y-auto">
              {filteredFAQ.map(item => (
                <Card key={item.id} className="border-gray-200 hover:border-green-300 transition-colors cursor-pointer">
                  <CardContent className="p-4" onClick={() => selectFAQItem(item)}>
                    <div className="flex items-start justify-between">
                      <div className="flex-1">
                        <h4 className="font-medium text-gray-900 mb-2">{item.question}</h4>
                        <p className="text-sm text-gray-600 mb-2">{item.answer}</p>
                        <Badge variant="secondary" className="text-xs">
                          {item.category}
                        </Badge>
                      </div>
                      <Button variant="ghost" size="sm" className="ml-2">
                        <MessageCircle className="h-4 w-4" />
                      </Button>
                    </div>
                  </CardContent>
                </Card>
              ))}
            </div>

            {filteredFAQ.length === 0 && searchQuery && (
              <div className="text-center py-8 text-gray-500">
                <HelpCircle className="h-12 w-12 mx-auto mb-4 opacity-50" />
                <p>Nenhuma pergunta encontrada para "{searchQuery}"</p>
                <p className="text-sm mt-2">Tente usar o chat abaixo para fazer sua pergunta.</p>
              </div>
            )}
          </CardContent>
        </Card>
      )}

      {/* Chat Interface */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Bot className="h-5 w-5" />
            Chat de Suporte
          </CardTitle>
        </CardHeader>
        <CardContent>
          {/* Messages */}
          <div className="space-y-4 mb-4 max-h-96 overflow-y-auto border rounded-lg p-4 bg-gray-50">
            {messages.map((message, index) => (
              <div
                key={index}
                className={`flex ${message.type === 'user' ? 'justify-end' : 'justify-start'}`}
              >
                <div
                  className={`max-w-xs lg:max-w-md px-4 py-2 rounded-lg flex items-start gap-2 ${
                    message.type === 'user'
                      ? 'bg-blue-600 text-white'
                      : 'bg-white text-gray-900 border border-gray-200'
                  }`}
                >
                  {message.type === 'bot' && (
                    <Bot className="h-4 w-4 mt-0.5 flex-shrink-0" />
                  )}
                  {message.type === 'user' && (
                    <User className="h-4 w-4 mt-0.5 flex-shrink-0" />
                  )}
                  <div className="flex-1">
                    <p className="text-sm">{message.content}</p>
                    <p className="text-xs opacity-70 mt-1">{message.timestamp}</p>
                    {message.isAutomated && (
                      <Badge variant="secondary" className="text-xs mt-1">
                        Resposta Automática
                      </Badge>
                    )}
                  </div>
                </div>
              </div>
            ))}
            
            {isLoading && (
              <div className="flex justify-start">
                <div className="bg-white text-gray-900 border border-gray-200 px-4 py-2 rounded-lg flex items-center gap-2">
                  <Bot className="h-4 w-4" />
                  <Loader2 className="h-4 w-4 animate-spin" />
                  <span className="text-sm">Digitando...</span>
                </div>
              </div>
            )}
            
            <div ref={messagesEndRef} />
          </div>

          {/* Message Input */}
          <div className="flex gap-2">
            <textarea
              value={currentMessage}
              onChange={(e) => setCurrentMessage(e.target.value)}
              onKeyPress={handleKeyPress}
              placeholder="Digite sua pergunta sobre o abbā..."
              className="flex-1 px-3 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-green-500 resize-none"
              rows={2}
              disabled={isLoading}
            />
            <Button
              onClick={sendMessage}
              disabled={!currentMessage.trim() || isLoading}
              className="bg-green-600 hover:bg-green-700"
            >
              {isLoading ? (
                <Loader2 className="h-4 w-4 animate-spin" />
              ) : (
                <Send className="h-4 w-4" />
              )}
            </Button>
          </div>

          {/* Quick Actions */}
          <div className="mt-4 flex flex-wrap gap-2">
            <Button
              variant="outline"
              size="sm"
              onClick={() => setCurrentMessage('Como funciona o sistema de faixas?')}
              disabled={isLoading}
            >
              Sistema de Faixas
            </Button>
            <Button
              variant="outline"
              size="sm"
              onClick={() => setCurrentMessage('Como usar o assistente de IA?')}
              disabled={isLoading}
            >
              Assistente IA
            </Button>
            <Button
              variant="outline"
              size="sm"
              onClick={() => setCurrentMessage('Como acessar conteúdo premium?')}
              disabled={isLoading}
            >
              Premium
            </Button>
            <Button
              variant="outline"
              size="sm"
              onClick={() => setCurrentMessage('Problemas técnicos')}
              disabled={isLoading}
            >
              Suporte Técnico
            </Button>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

