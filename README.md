# abbā - Business Belt Application

**From White Belt to Black Belt in Business Mastery**

abbā é um aplicativo web inovador para empreendedores que oferece um sistema de cinturões (similar às artes marciais) para desenvolvimento empresarial, com IA integrada para consultoria personalizada.

## 🎯 Visão Geral

O abbā combina gamificação com inteligência artificial para criar uma experiência única de aprendizado empresarial, onde os usuários progridem através de diferentes níveis (cinturões) enquanto recebem orientação personalizada de IA.

## 🏗️ Estrutura do Projeto

```
abbā/
├── frontend/                 # Aplicação React
│   ├── App.jsx              # Componente principal
│   ├── Dashboard.jsx        # Dashboard principal
│   ├── BeltSystem.jsx       # Sistema de cinturões
│   ├── SearchTab.jsx        # Busca e pesquisa
│   ├── SupportChat.jsx      # Chat de suporte
│   └── VoiceChatbot.jsx     # Chatbot com voz
├── backend/                 # Backend Python
│   ├── main.py              # Servidor principal
│   ├── ai_agent.py          # Agente de IA
│   ├── business.py          # Lógica de negócios
│   └── user.py              # Gestão de usuários
├── supabase/                # Edge Functions
│   └── functions/
│       ├── _shared/
│       │   └── cors.ts      # Configurações CORS
│       └── business-ai-agent/
│           └── index.ts     # Edge Function principal
└── docs/                    # Documentação
```

## 🚀 Funcionalidades

### Sistema de Cinturões
- **Cinturão Branco**: Fundamentos do empreendedorismo
- **Cinturão Amarelo**: Planejamento e estratégia
- **Cinturão Laranja**: Marketing e vendas
- **Cinturão Verde**: Operações e gestão
- **Cinturão Azul**: Finanças e investimentos
- **Cinturão Marrom**: Liderança e equipes
- **Cinturão Preto**: Maestria empresarial

### IA Integrada
- Consultoria personalizada baseada no perfil do usuário
- Análise de negócios em tempo real
- Recomendações estratégicas
- Chat com voz para interação natural

### Recursos Adicionais
- Dashboard interativo
- Sistema de busca avançado
- Chat de suporte
- Integração com APIs externas

## 🛠️ Tecnologias

### Frontend
- **React**: Interface de usuário
- **CSS3**: Estilização moderna
- **JavaScript ES6+**: Lógica do frontend

### Backend
- **Python**: Servidor principal
- **FastAPI/Flask**: Framework web
- **OpenAI API**: Inteligência artificial
- **ElevenLabs**: Síntese de voz

### Infraestrutura
- **Supabase**: Backend-as-a-Service
- **Edge Functions**: Processamento serverless
- **PostgreSQL**: Banco de dados

## 📦 Instalação e Configuração

### Pré-requisitos
- Node.js 16+
- Python 3.8+
- Conta Supabase
- Chave API OpenAI

### Configuração Local

1. **Clone o repositório**
```bash
git clone <repository-url>
cd abba-business-belt
```

2. **Configure as variáveis de ambiente**
```bash
# Crie um arquivo .env com:
OPENAI_API_KEY=sua_chave_openai
SUPABASE_URL=sua_url_supabase
SUPABASE_ANON_KEY=sua_chave_supabase
```

3. **Instale dependências do frontend**
```bash
npm install
```

4. **Instale dependências do backend**
```bash
pip install -r requirements.txt
```

### Deploy das Edge Functions

1. **Instale o Supabase CLI**
```bash
npm install -g supabase
```

2. **Faça login no Supabase**
```bash
supabase login
```

3. **Linke o projeto**
```bash
supabase link --project-ref vfzlbtojeqxkkskldrur
```

4. **Deploy das funções**
```bash
supabase functions deploy business-ai-agent
```

## 🌐 Deploy com Gitpod

Para desenvolvimento em ambiente cloud:

1. Acesse: `gitpod.io/#<repository-url>`
2. Aguarde a inicialização do ambiente
3. Execute os comandos de configuração
4. Faça o deploy das Edge Functions

## 📚 Documentação

- [Conceito de Design](./Conceito%20de%20Design%20-%20Aplicativo%20de%20Empreendedorismo.md)
- [Business Belt - Aplicativo Web](./Business%20Belt%20-%20Aplicativo%20Web%20para%20Empreendedores.md)
- [Guia de Desenvolvimento](./abbā%20-%20From%20White%20Belt%20to%20Black%20Belt%20in%20Business%20Mastery.md)

## 🤝 Contribuição

1. Fork o projeto
2. Crie uma branch para sua feature
3. Commit suas mudanças
4. Push para a branch
5. Abra um Pull Request

## 📄 Licença

Este projeto está sob a licença MIT. Veja o arquivo LICENSE para mais detalhes.

## 📞 Suporte

Para suporte e dúvidas, entre em contato através do sistema de chat integrado no aplicativo.

---

**abbā** - Transformando empreendedores através da gamificação e IA 🥋
