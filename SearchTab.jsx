import { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { 
  Search, 
  TrendingUp, 
  ExternalLink,
  Loader2,
  BookOpen,
  Lightbulb
} from 'lucide-react'

export function SearchTab() {
  const [query, setQuery] = useState('')
  const [searchResults, setSearchResults] = useState(null)
  const [isLoading, setIsLoading] = useState(false)
  const [trendingTopics, setTrendingTopics] = useState(null)
  const [loadingTrending, setLoadingTrending] = useState(false)

  const handleSearch = async () => {
    if (!query.trim()) return

    setIsLoading(true)
    try {
      const response = await fetch('http://localhost:5000/api/perplexity/search', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ query: query.trim() })
      })

      const data = await response.json()
      
      if (data.success) {
        setSearchResults(data)
      } else {
        console.error('Erro na busca:', data.error)
        setSearchResults({
          error: data.error || 'Erro desconhecido na busca'
        })
      }
    } catch (error) {
      console.error('Erro na requisição:', error)
      setSearchResults({
        error: 'Erro de conexão com o servidor'
      })
    } finally {
      setIsLoading(false)
    }
  }

  const handleTrendingTopics = async () => {
    setLoadingTrending(true)
    try {
      const response = await fetch('http://localhost:5000/api/perplexity/trending-topics')
      const data = await response.json()
      
      if (data.success) {
        setTrendingTopics(data.trending_topics)
      } else {
        console.error('Erro ao buscar tópicos em alta:', data.error)
      }
    } catch (error) {
      console.error('Erro na requisição:', error)
    } finally {
      setLoadingTrending(false)
    }
  }

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSearch()
    }
  }

  return (
    <div className="space-y-6">
      {/* Search Interface */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <Search className="h-5 w-5" />
            Busca Inteligente com IA
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <p className="text-gray-600">
              Faça perguntas sobre negócios, marketing, finanças ou qualquer tópico relacionado ao empreendedorismo. 
              Nossa IA buscará as informações mais atualizadas para você.
            </p>
            
            <div className="flex gap-2">
              <input
                type="text"
                placeholder="Ex: Como criar uma estratégia de marketing digital eficaz?"
                className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:ring-2 focus:ring-blue-500"
                value={query}
                onChange={(e) => setQuery(e.target.value)}
                onKeyPress={handleKeyPress}
                disabled={isLoading}
              />
              <Button 
                onClick={handleSearch}
                disabled={!query.trim() || isLoading}
                className="bg-blue-600 hover:bg-blue-700"
              >
                {isLoading ? (
                  <Loader2 className="h-4 w-4 animate-spin" />
                ) : (
                  <Search className="h-4 w-4" />
                )}
                {isLoading ? 'Buscando...' : 'Buscar'}
              </Button>
            </div>

            {/* Quick Actions */}
            <div className="flex flex-wrap gap-2">
              <Button
                variant="outline"
                size="sm"
                onClick={() => setQuery('Tendências de marketing digital 2025')}
                disabled={isLoading}
              >
                Marketing Digital
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => setQuery('Como validar uma ideia de negócio')}
                disabled={isLoading}
              >
                Validação de Negócio
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => setQuery('Estratégias de precificação para startups')}
                disabled={isLoading}
              >
                Precificação
              </Button>
              <Button
                variant="outline"
                size="sm"
                onClick={() => setQuery('Como conseguir investimento para startup')}
                disabled={isLoading}
              >
                Investimento
              </Button>
            </div>
          </div>
        </CardContent>
      </Card>

      {/* Trending Topics */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <TrendingUp className="h-5 w-5" />
            Tópicos em Alta
          </CardTitle>
        </CardHeader>
        <CardContent>
          <div className="space-y-4">
            <p className="text-gray-600">
              Descubra os assuntos mais relevantes para empreendedores brasileiros no momento.
            </p>
            
            <Button
              onClick={handleTrendingTopics}
              disabled={loadingTrending}
              variant="outline"
              className="w-full"
            >
              {loadingTrending ? (
                <Loader2 className="h-4 w-4 animate-spin mr-2" />
              ) : (
                <TrendingUp className="h-4 w-4 mr-2" />
              )}
              {loadingTrending ? 'Carregando...' : 'Ver Tópicos em Alta'}
            </Button>

            {trendingTopics && (
              <Card className="bg-gradient-to-r from-purple-50 to-blue-50 border-purple-200">
                <CardContent className="p-4">
                  <div className="prose prose-sm max-w-none">
                    <div className="whitespace-pre-wrap text-gray-700">
                      {trendingTopics}
                    </div>
                  </div>
                </CardContent>
              </Card>
            )}
          </div>
        </CardContent>
      </Card>

      {/* Search Results */}
      {searchResults && (
        <Card>
          <CardHeader>
            <CardTitle className="flex items-center gap-2">
              <BookOpen className="h-5 w-5" />
              Resultados da Busca
            </CardTitle>
          </CardHeader>
          <CardContent>
            {searchResults.error ? (
              <div className="p-4 bg-red-50 border border-red-200 rounded-lg">
                <p className="text-red-700">
                  <strong>Erro:</strong> {searchResults.error}
                </p>
              </div>
            ) : (
              <div className="space-y-6">
                {/* Query */}
                <div className="p-3 bg-gray-50 rounded-lg">
                  <p className="text-sm text-gray-600 mb-1">Sua pergunta:</p>
                  <p className="font-medium text-gray-900">{searchResults.query}</p>
                </div>

                {/* Main Content */}
                <div className="prose prose-sm max-w-none">
                  <div className="whitespace-pre-wrap text-gray-700 leading-relaxed">
                    {searchResults.content}
                  </div>
                </div>

                {/* Citations */}
                {searchResults.citations && searchResults.citations.length > 0 && (
                  <div className="space-y-2">
                    <h4 className="font-semibold text-gray-900 flex items-center gap-2">
                      <ExternalLink className="h-4 w-4" />
                      Fontes
                    </h4>
                    <div className="space-y-2">
                      {searchResults.citations.map((citation, index) => (
                        <div key={index} className="p-3 bg-blue-50 border border-blue-200 rounded-lg">
                          <a 
                            href={citation} 
                            target="_blank" 
                            rel="noopener noreferrer"
                            className="text-blue-600 hover:text-blue-800 text-sm break-all"
                          >
                            {citation}
                          </a>
                        </div>
                      ))}
                    </div>
                  </div>
                )}

                {/* Related Questions */}
                {searchResults.related_questions && searchResults.related_questions.length > 0 && (
                  <div className="space-y-2">
                    <h4 className="font-semibold text-gray-900 flex items-center gap-2">
                      <Lightbulb className="h-4 w-4" />
                      Perguntas Relacionadas
                    </h4>
                    <div className="space-y-2">
                      {searchResults.related_questions.map((question, index) => (
                        <Button
                          key={index}
                          variant="outline"
                          size="sm"
                          className="text-left justify-start h-auto p-3 whitespace-normal"
                          onClick={() => setQuery(question)}
                        >
                          {question}
                        </Button>
                      ))}
                    </div>
                  </div>
                )}
              </div>
            )}
          </CardContent>
        </Card>
      )}
    </div>
  )
}

