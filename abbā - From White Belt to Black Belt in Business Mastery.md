# abbā - From White Belt to Black Belt in Business Mastery

## 🎯 Visão Geral

O **abbā** é um aplicativo web completo para empreendedores que combina gamificação, inteligência artificial e conteúdo educacional de alta qualidade. O sistema utiliza um conceito de faixas (como no karatê) para guiar o progresso do usuário através de diferentes níveis de maestria em negócios.

## ✨ Funcionalidades Principais

### 🥋 Sistema de Faixas
- **Faixa Atual**: Branca (iniciante)
- **Próxima Faixa**: Amarela
- **Progresso**: 45/100 pontos
- Sistema de pontuação baseado em atividades e conquistas

### 📊 Dashboard de Negócios
- Métricas em tempo real (Receita Mensal, Clientes Ativos, Taxa de Conversão, Metas)
- Visualização clara do progresso
- Interface responsiva e moderna

### 🤖 Assistente de IA para Negócios
- Busca personalizada de estratégias baseada na descrição do negócio
- Integração com OpenAI para respostas inteligentes
- Sugestões de melhores práticas atualizadas

### 🔍 Busca Inteligente com Perplexity AI
- **Nova Funcionalidade**: Busca avançada com IA
- Perguntas em linguagem natural
- Informações atualizadas sobre empreendedorismo
- Tópicos em alta para empreendedores brasileiros
- Citações e fontes confiáveis

### 🎙️ Anna - Assistente de Voz
- **Nova Funcionalidade**: Chatbot de voz com ElevenLabs
- Conversa por voz ou texto
- Especializada em negócios e empreendedorismo
- Respostas em áudio de alta qualidade
- Reconhecimento de voz em português

### 💬 Chat de Suporte e FAQ
- **Nova Funcionalidade**: Sistema de suporte integrado
- FAQ completo com 10+ perguntas frequentes
- Chat automático com respostas inteligentes
- Busca nas perguntas frequentes
- Categorização por tópicos

### 📚 Conteúdo Educacional
- **5 Abas Educacionais** com vídeos integrados:
  - **Marketing**: Crafting_the_Irresistible__A_Guide_to_the_$100M_Offer.mp4
  - **Mindset**: The_Architecture_of_Your_Reality.mp4
  - **Mídias Sociais**: The_Faceless_Creator_s_Blueprint.mp4
  - **Dieta**: Cracking_the_Code_of_Your_Diet.mp4
  - **Finanças**: Your_Financial_Journey.mp4
- Conteúdo escrito extenso (50.000+ palavras total)
- Player de vídeo integrado

### 💰 Sistema de Monetização
- Integração com RevenueCat
- Planos de assinatura (Mensal R$ 29,90 / Anual R$ 299,90)
- Upgrade de faixa por R$ 9,90

## 🛠️ Tecnologias Utilizadas

### Frontend
- **React 19.1.0** com Vite
- **Tailwind CSS** para estilização
- **shadcn/ui** para componentes
- **Lucide React** para ícones
- **Stream Chat React** para chat de suporte

### Backend
- **Flask** (Python)
- **SQLAlchemy** para banco de dados
- **Flask-CORS** para integração frontend/backend
- **PyJWT** para autenticação

### APIs Integradas
- **OpenAI API** - Assistente de IA
- **Perplexity API** - Busca inteligente
- **ElevenLabs API** - Assistente de voz Anna
- **StreamChat API** - Sistema de chat
- **RevenueCat API** - Monetização

## 📁 Estrutura do Projeto

```
/home/ubuntu/
├── business-belt-app/          # Frontend React
│   ├── src/
│   │   ├── components/
│   │   │   ├── BeltSystem.jsx
│   │   │   ├── Dashboard.jsx
│   │   │   ├── SearchTab.jsx      # Nova: Busca IA
│   │   │   ├── VoiceChatbot.jsx   # Nova: Anna
│   │   │   └── SupportChat.jsx    # Nova: Suporte
│   │   └── App.jsx
│   └── public/videos/          # Vídeos educacionais
├── business-belt-backend/      # Backend Flask
│   ├── src/
│   │   ├── routes/
│   │   │   ├── ai.py
│   │   │   ├── perplexity.py      # Nova: API Perplexity
│   │   │   ├── elevenlabs.py      # Nova: API ElevenLabs
│   │   │   ├── streamchat.py      # Nova: API StreamChat
│   │   │   ├── business.py
│   │   │   ├── revenuecat.py
│   │   │   └── user.py
│   │   ├── services/
│   │   │   └── ai_agent.py
│   │   └── main.py
└── conteudo_educacional_*.md   # Conteúdo das abas
```

## 🚀 Como Executar

### Pré-requisitos
- Python 3.11+
- Node.js 20+
- pnpm

### Backend
```bash
cd business-belt-backend
pip install flask flask-cors flask-sqlalchemy openai requests PyJWT
python src/main.py
```

### Frontend
```bash
cd business-belt-app
pnpm install
pnpm run dev --host
```

### URLs de Acesso
- **Frontend**: http://localhost:5173
- **Backend**: http://localhost:5000

## 🔑 Configuração de APIs

### Variáveis de Ambiente
```bash
# OpenAI
OPENAI_API_KEY=sk-...

# Perplexity
PERPLEXITY_API_KEY=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

# ElevenLabs
ELEVENLABS_API_KEY=sk_64ec45f1d9009448a521bb142fa02aad9318e7c2dbb4d678
ANNA_AGENT_ID=agent_4501k2afd14xfres2jbtd5hm3d0j

# StreamChat
STREAM_API_KEY=p744wjdfmg6c
STREAM_API_SECRET=avmjgmm6fcat3ex7je3t94paaj88m7p8nrsm4p7hkuu8y5pvpsspv49k5vb9d9ae
```

## 📱 Funcionalidades por Aba

### 1. Busca IA (Perplexity)
- Busca inteligente com IA
- Tópicos em alta
- Perguntas relacionadas
- Citações e fontes

### 2. Anna (ElevenLabs)
- Assistente de voz
- Reconhecimento de fala
- Respostas em áudio
- Chat por texto alternativo

### 3. Suporte (StreamChat)
- FAQ com 10+ perguntas
- Chat automático
- Busca nas perguntas
- Categorização por tópicos

### 4. Marketing
- Vídeo: Crafting the Irresistible
- Conteúdo: Estratégias de lançamento
- Material complementar

### 5. Mindset
- Vídeo: The Architecture of Your Reality
- Conteúdo: Psicologia empreendedora
- Modulação de ambiente

### 6. Mídias Sociais
- Vídeo: The Faceless Creator's Blueprint
- Conteúdo: YouTube e Instagram
- Estratégias de crescimento

### 7. Dieta
- Vídeo: Cracking the Code of Your Diet
- Conteúdo: Nutrição para performance
- Estratégias alimentares

### 8. Finanças
- Vídeo: Your Financial Journey
- Conteúdo: Anamnese financeira
- Diagnóstico vital

## 🎯 Endpoints da API

### Perplexity
- `POST /api/perplexity/search` - Busca inteligente
- `GET /api/perplexity/trending-topics` - Tópicos em alta

### ElevenLabs
- `POST /api/elevenlabs/anna-agent/start-conversation` - Iniciar conversa
- `POST /api/elevenlabs/anna-agent/send-message` - Enviar mensagem
- `POST /api/elevenlabs/text-to-speech` - Converter texto em fala

### StreamChat
- `POST /api/streamchat/get-token` - Token de autenticação
- `GET /api/streamchat/faq` - Perguntas frequentes
- `POST /api/streamchat/bot-response` - Resposta automática

### Outros
- `POST /api/ai/business-strategies` - Estratégias de negócio
- `GET /api/revenuecat/products` - Produtos de assinatura

## 🔧 Melhorias Implementadas

### Interface
- 8 abas educacionais (3 novas)
- Layout responsivo otimizado
- Componentes reutilizáveis
- Design system consistente

### Backend
- 3 novas integrações de API
- Sistema de autenticação JWT
- Tratamento de erros robusto
- CORS configurado

### Funcionalidades
- Busca inteligente com IA
- Assistente de voz multilíngue
- Sistema de suporte completo
- FAQ automatizado

## 📈 Métricas e Analytics

### Dashboard
- Receita Mensal: R$ 0 (+0%)
- Clientes Ativos: 0 (+0%)
- Taxa de Conversão: 0% (+0%)
- Metas Concluídas: 0/5 (0%)

### Sistema de Pontos
- Pontos atuais: 45/100
- Próxima faixa: Amarela (55 pontos necessários)
- Atividades que geram pontos:
  - Assistir vídeos educacionais
  - Usar assistente de IA
  - Completar módulos
  - Atingir metas de negócio

## 🎨 Design e UX

### Cores e Temas
- Paleta principal: Azul, Verde, Roxo
- Gradientes suaves
- Modo claro otimizado
- Acessibilidade considerada

### Componentes
- Cards informativos
- Botões interativos
- Badges de status
- Indicadores de progresso

## 🔒 Segurança

### Autenticação
- Tokens JWT para APIs
- Chaves de API seguras
- CORS configurado
- Validação de entrada

### Privacidade
- Dados locais protegidos
- APIs externas seguras
- Logs controlados

## 🚀 Deploy e Produção

### Preparação
- Ambiente de desenvolvimento testado
- APIs configuradas e funcionais
- Frontend e backend integrados
- Vídeos e assets organizados

### Próximos Passos
1. Configurar ambiente de produção
2. Deploy do backend (Flask)
3. Deploy do frontend (React)
4. Configurar domínio personalizado
5. Monitoramento e analytics

## 📞 Suporte

### Contato
- Email: suporte@abba.app
- Chat integrado no aplicativo
- FAQ completo disponível
- Assistente Anna para dúvidas rápidas

### Documentação
- README completo
- Guias de uso
- Troubleshooting
- API documentation

---

**abbā** - Transformando empreendedores iniciantes em mestres dos negócios, uma faixa por vez! 🥋✨

