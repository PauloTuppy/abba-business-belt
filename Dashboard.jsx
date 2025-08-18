import { useState } from 'react'
import { Card, CardContent, CardHeader, CardTitle } from '@/components/ui/card.jsx'
import { Button } from '@/components/ui/button.jsx'
import { Badge } from '@/components/ui/badge.jsx'
import { Tabs, TabsContent, TabsList, TabsTrigger } from '@/components/ui/tabs.jsx'
import { BeltSystem } from './BeltSystem.jsx'
import { SearchTab } from './SearchTab.jsx'
import { VoiceChatbot } from './VoiceChatbot.jsx'
import { SupportChat } from './SupportChat.jsx'
import { 
  TrendingUp, 
  DollarSign, 
  Users, 
  Target,
  BookOpen,
  Brain,
  Instagram,
  Apple,
  PiggyBank,
  BarChart3,
  MessageSquare,
  Settings,
  Search,
  Bot,
  HelpCircle
} from 'lucide-react'

export function Dashboard() {
  const [userPoints, setUserPoints] = useState(45)
  const [businessType, setBusinessType] = useState('')
  const [showAIChat, setShowAIChat] = useState(false)

  // Função para mapear vídeos às abas
  const getVideoForTab = (tabId) => {
    const videoMap = {
      'marketing': 'Crafting_the_Irresistible__A_Guide_to_the_$100M_Offer.mp4',
      'mindset': 'The_Architecture_of_Your_Reality.mp4',
      'social': 'The_Faceless_Creator_s_Blueprint.mp4',
      'nutrition': 'Cracking_the_Code_of_Your_Diet.mp4',
      'finance': 'Your_Financial_Journey.mp4'
    }
    return videoMap[tabId] || ''
  }

  const metrics = [
    {
      title: 'Receita Mensal',
      value: 'R$ 0',
      change: '+0%',
      icon: DollarSign,
      color: 'text-green-600'
    },
    {
      title: 'Clientes Ativos',
      value: '0',
      change: '+0%',
      icon: Users,
      color: 'text-blue-600'
    },
    {
      title: 'Taxa de Conversão',
      value: '0%',
      change: '+0%',
      icon: TrendingUp,
      color: 'text-purple-600'
    },
    {
      title: 'Metas Concluídas',
      value: '0/5',
      change: '0%',
      icon: Target,
      color: 'text-orange-600'
    }
  ]

  const educationalTabs = [
    {
      id: 'search',
      title: 'Busca IA',
      icon: Search,
      description: 'Busca Inteligente com Perplexity AI'
    },
    {
      id: 'voice',
      title: 'Anna',
      icon: Bot,
      description: 'Assistente de Voz com ElevenLabs'
    },
    {
      id: 'support',
      title: 'Suporte',
      icon: HelpCircle,
      description: 'Chat de Suporte e FAQ'
    },
    {
      id: 'marketing',
      title: 'Marketing',
      icon: BarChart3,
      description: 'Elementos Fundamentais para Lançamentos de Sucesso'
    },
    {
      id: 'mindset',
      title: 'Mindset',
      icon: Brain,
      description: 'Modulando Seu Ambiente e Hábitos'
    },
    {
      id: 'social',
      title: 'Mídias Sociais',
      icon: Instagram,
      description: 'Estratégias para Sucesso no YouTube e Instagram'
    },
    {
      id: 'nutrition',
      title: 'Dieta',
      icon: Apple,
      description: 'Nutrição e Estratégias Alimentares'
    },
    {
      id: 'finance',
      title: 'Finanças',
      icon: PiggyBank,
      description: 'Anamnese Financeira: O Diagnóstico Vital para sua Vida'
    }
  ]

  return (
    <div className="min-h-screen bg-gray-50 p-4 space-y-6">
      {/* Header */}
      <header className="flex flex-col md:flex-row justify-between items-start md:items-center gap-4">
        <div>
          <h1 className="text-3xl font-bold text-gray-900">abbā</h1>
          <p className="text-gray-600">From White Belt to Black Belt in Business Mastery</p>
        </div>
        <div className="flex items-center gap-4">
          <BeltSystem userPoints={userPoints} />
          <Button variant="outline" size="icon">
            <Settings className="h-4 w-4" />
          </Button>
        </div>
      </header>

      {/* AI Business Assistant */}
      <Card className="border-blue-200 bg-blue-50">
        <CardHeader>
          <CardTitle className="flex items-center gap-2 text-blue-800">
            <MessageSquare className="h-5 w-5" />
            Assistente de IA para Negócios
          </CardTitle>
        </CardHeader>
        <CardContent>
          <p className="text-blue-700 mb-4">
            Conte-me sobre seu negócio e eu buscarei as melhores práticas e estratégias para você!
          </p>
          <div className="flex gap-2">
            <input
              type="text"
              placeholder="Descreva seu negócio (ex: loja de roupas online, consultoria em marketing...)"
              className="flex-1 px-3 py-2 border border-blue-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500"
              value={businessType}
              onChange={(e) => setBusinessType(e.target.value)}
            />
            <Button 
              onClick={() => setShowAIChat(true)}
              disabled={!businessType.trim()}
              className="bg-blue-600 hover:bg-blue-700"
            >
              Buscar Estratégias
            </Button>
          </div>
        </CardContent>
      </Card>

      {/* Metrics Grid */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-4">
        {metrics.map((metric, index) => (
          <Card key={index}>
            <CardContent className="p-6">
              <div className="flex items-center justify-between">
                <div>
                  <p className="text-sm font-medium text-gray-600">{metric.title}</p>
                  <p className="text-2xl font-bold text-gray-900">{metric.value}</p>
                  <p className={`text-sm ${metric.color}`}>{metric.change}</p>
                </div>
                <metric.icon className={`h-8 w-8 ${metric.color}`} />
              </div>
            </CardContent>
          </Card>
        ))}
      </div>

      {/* Educational Content Tabs */}
      <Card>
        <CardHeader>
          <CardTitle className="flex items-center gap-2">
            <BookOpen className="h-5 w-5" />
            Conteúdo Educacional
          </CardTitle>
        </CardHeader>
        <CardContent>
          <Tabs defaultValue="marketing" className="w-full">
            <TabsList className="grid w-full grid-cols-2 md:grid-cols-4 lg:grid-cols-8">
              {educationalTabs.map((tab) => (
                <TabsTrigger key={tab.id} value={tab.id} className="flex items-center gap-1">
                  <tab.icon className="h-4 w-4" />
                  <span className="hidden sm:inline">{tab.title}</span>
                </TabsTrigger>
              ))}
            </TabsList>
            
            {educationalTabs.map((tab) => (
              <TabsContent key={tab.id} value={tab.id} className="mt-4">
                {tab.id === 'search' ? (
                  <SearchTab />
                ) : tab.id === 'voice' ? (
                  <VoiceChatbot />
                ) : tab.id === 'support' ? (
                  <SupportChat />
                ) : (
                  <Card>
                    <CardHeader>
                      <CardTitle className="flex items-center gap-2">
                        <tab.icon className="h-5 w-5" />
                        {tab.title}
                      </CardTitle>
                    </CardHeader>
                    <CardContent>
                      <p className="text-gray-600 mb-4">{tab.description}</p>
                      
                      {/* Video Player */}
                      <div className="mb-6">
                        <div className="aspect-video bg-black rounded-lg overflow-hidden">
                          <video 
                            controls 
                            className="w-full h-full"
                            poster="/api/placeholder/800/450"
                          >
                            <source 
                              src={`/videos/${getVideoForTab(tab.id)}`} 
                              type="video/mp4" 
                            />
                            Seu navegador não suporta o elemento de vídeo.
                          </video>
                        </div>
                      </div>
                      
                      <div className="space-y-3">
                        <div className="p-4 bg-gray-50 rounded-lg">
                          <h4 className="font-semibold mb-2">Conteúdo Educacional Completo</h4>
                          <p className="text-sm text-gray-600">
                            Assista ao vídeo acima e explore o conteúdo detalhado sobre {tab.title.toLowerCase()}.
                          </p>
                        </div>
                        <Button variant="outline" className="w-full">
                          Acessar Material Complementar
                        </Button>
                      </div>
                    </CardContent>
                  </Card>
                )}
              </TabsContent>
            ))}
          </Tabs>
        </CardContent>
      </Card>

      {/* Business Management Tools */}
      <Card>
        <CardHeader>
          <CardTitle>Ferramentas de Gestão (Faixa Branca)</CardTitle>
        </CardHeader>
        <CardContent>
          <div className="grid grid-cols-1 md:grid-cols-3 gap-4">
            <Card className="border-dashed border-2 border-gray-300">
              <CardContent className="p-6 text-center">
                <BarChart3 className="h-8 w-8 mx-auto mb-2 text-gray-400" />
                <h3 className="font-semibold mb-2">Planilhas Financeiras</h3>
                <p className="text-sm text-gray-600 mb-4">
                  Controle suas finanças com planilhas automatizadas
                </p>
                <Button variant="outline" size="sm">
                  Em Breve
                </Button>
              </CardContent>
            </Card>
            
            <Card className="border-dashed border-2 border-gray-300">
              <CardContent className="p-6 text-center">
                <Users className="h-8 w-8 mx-auto mb-2 text-gray-400" />
                <h3 className="font-semibold mb-2">CRM Simples</h3>
                <p className="text-sm text-gray-600 mb-4">
                  Gerencie seus clientes e leads
                </p>
                <Button variant="outline" size="sm">
                  Em Breve
                </Button>
              </CardContent>
            </Card>
            
            <Card className="border-dashed border-2 border-gray-300">
              <CardContent className="p-6 text-center">
                <Target className="h-8 w-8 mx-auto mb-2 text-gray-400" />
                <h3 className="font-semibold mb-2">Metas e Objetivos</h3>
                <p className="text-sm text-gray-600 mb-4">
                  Defina e acompanhe suas metas
                </p>
                <Button variant="outline" size="sm">
                  Em Breve
                </Button>
              </CardContent>
            </Card>
          </div>
        </CardContent>
      </Card>
    </div>
  )
}

