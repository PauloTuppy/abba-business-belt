import openai
import requests
import json
from typing import Dict, List, Optional
import os

class BusinessAIAgent:
    def __init__(self):
        self.openai_client = openai.OpenAI(
            api_key=os.getenv('OPENAI_API_KEY'),
            base_url=os.getenv('OPENAI_API_BASE')
        )
    
    def search_business_practices(self, business_type: str, query: str) -> Dict:
        """Search for business best practices using web search and AI analysis"""
        try:
            # First, search for relevant information
            search_results = self._search_web(f"{business_type} best practices {query}")
            
            # Then, use AI to analyze and provide recommendations
            ai_recommendations = self._generate_ai_recommendations(business_type, query, search_results)
            
            return {
                'success': True,
                'business_type': business_type,
                'query': query,
                'recommendations': ai_recommendations,
                'sources': search_results[:3]  # Top 3 sources
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def _search_web(self, query: str) -> List[Dict]:
        """Simulate web search results (in production, use actual search API)"""
        # This is a mock implementation. In production, you would use:
        # - Google Custom Search API
        # - Bing Search API
        # - Or other search services
        
        mock_results = [
            {
                'title': 'Melhores Práticas para Empreendedores Iniciantes',
                'url': 'https://example.com/best-practices',
                'snippet': 'Guia completo com estratégias comprovadas para novos empreendedores...'
            },
            {
                'title': 'Como Validar Sua Ideia de Negócio',
                'url': 'https://example.com/validate-business',
                'snippet': 'Métodos eficazes para testar e validar sua proposta de valor...'
            },
            {
                'title': 'Marketing Digital para Pequenos Negócios',
                'url': 'https://example.com/digital-marketing',
                'snippet': 'Estratégias de marketing digital acessíveis e eficazes...'
            }
        ]
        
        return mock_results
    
    def _generate_ai_recommendations(self, business_type: str, query: str, search_results: List[Dict]) -> str:
        """Generate AI-powered recommendations based on business type and search results"""
        try:
            # Prepare context from search results
            context = "\n".join([f"- {result['title']}: {result['snippet']}" for result in search_results])
            
            prompt = f"""
            Como um consultor especialista em negócios, forneça recomendações detalhadas e práticas para o seguinte cenário:

            Tipo de Negócio: {business_type}
            Pergunta/Situação: {query}

            Contexto de pesquisa:
            {context}

            Por favor, forneça:
            1. Análise da situação atual
            2. 3-5 recomendações específicas e acionáveis
            3. Próximos passos práticos
            4. Métricas para acompanhar o progresso
            5. Recursos ou ferramentas recomendadas

            Mantenha as recomendações práticas, específicas e adequadas para empreendedores brasileiros.
            """
            
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um consultor especialista em negócios com vasta experiência em empreendedorismo no Brasil. Suas respostas são sempre práticas, específicas e acionáveis."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            # Fallback to template-based recommendations
            return self._generate_template_recommendations(business_type, query)
    
    def _generate_template_recommendations(self, business_type: str, query: str) -> str:
        """Generate template-based recommendations as fallback"""
        return f"""
        **Análise para {business_type}**

        Baseado na sua consulta "{query}", aqui estão recomendações específicas:

        **1. Análise da Situação**
        - Identifique claramente seu público-alvo
        - Analise a concorrência no seu nicho
        - Defina sua proposta de valor única

        **2. Recomendações Principais**
        - **Validação de Mercado**: Teste sua ideia com clientes reais antes de investir pesado
        - **Presença Digital**: Crie perfis profissionais nas redes sociais relevantes
        - **Controle Financeiro**: Implemente um sistema básico de controle de receitas e despesas
        - **Networking**: Conecte-se com outros empreendedores do seu setor
        - **Aprendizado Contínuo**: Invista em capacitação e conhecimento do mercado

        **3. Próximos Passos**
        1. Defina seu MVP (Produto Mínimo Viável)
        2. Crie um plano de marketing básico
        3. Estabeleça metas financeiras realistas
        4. Desenvolva um sistema de feedback de clientes

        **4. Métricas Importantes**
        - Taxa de conversão de leads
        - Custo de aquisição de clientes
        - Receita mensal recorrente
        - Satisfação do cliente (NPS)

        **5. Ferramentas Recomendadas**
        - Google Analytics (análise de tráfego)
        - Redes sociais (Instagram, LinkedIn, Facebook)
        - Planilhas Google (controle financeiro)
        - WhatsApp Business (atendimento)
        """
    
    def generate_belt_specific_content(self, belt_level: str, business_type: str) -> Dict:
        """Generate content specific to the user's current belt level"""
        try:
            belt_content = {
                'white': {
                    'focus': 'Fundamentos do Empreendedorismo',
                    'goals': [
                        'Definir claramente seu negócio',
                        'Identificar público-alvo',
                        'Criar presença básica online',
                        'Estabelecer controle financeiro básico'
                    ],
                    'tools': ['Planilhas financeiras', 'Redes sociais básicas', 'WhatsApp Business']
                },
                'yellow': {
                    'focus': 'Estruturação e Validação',
                    'goals': [
                        'Validar proposta de valor',
                        'Implementar sistema de vendas',
                        'Criar processo de atendimento',
                        'Desenvolver marca básica'
                    ],
                    'tools': ['CRM simples', 'Landing pages', 'Google Analytics', 'Canva']
                },
                'orange': {
                    'focus': 'Crescimento e Otimização',
                    'goals': [
                        'Automatizar processos',
                        'Expandir canais de venda',
                        'Implementar marketing digital',
                        'Melhorar experiência do cliente'
                    ],
                    'tools': ['Automação de marketing', 'E-commerce', 'Ads Manager', 'Chatbots']
                }
            }
            
            current_belt = belt_content.get(belt_level, belt_content['white'])
            
            prompt = f"""
            Crie um guia específico para um empreendedor na faixa {belt_level} com negócio do tipo "{business_type}".
            
            Foco da faixa: {current_belt['focus']}
            
            Forneça:
            1. Objetivos específicos para esta faixa
            2. Estratégias detalhadas
            3. Ferramentas recomendadas
            4. Cronograma sugerido (30-90 dias)
            5. Indicadores de sucesso
            
            Mantenha o conteúdo prático e específico para o tipo de negócio mencionado.
            """
            
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um mentor de negócios especializado em desenvolvimento progressivo de empreendedores."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1200,
                temperature=0.7
            )
            
            return {
                'success': True,
                'belt_level': belt_level,
                'business_type': business_type,
                'content': response.choices[0].message.content,
                'focus': current_belt['focus'],
                'recommended_tools': current_belt['tools']
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }
    
    def analyze_business_metrics(self, metrics: Dict) -> Dict:
        """Analyze business metrics and provide insights"""
        try:
            prompt = f"""
            Analise as seguintes métricas de negócio e forneça insights acionáveis:
            
            Receita Mensal: R$ {metrics.get('monthly_revenue', 0)}
            Clientes Ativos: {metrics.get('active_customers', 0)}
            Taxa de Conversão: {metrics.get('conversion_rate', 0)}%
            Metas Concluídas: {metrics.get('goals_completed', 0)}/{metrics.get('total_goals', 5)}
            
            Forneça:
            1. Análise do desempenho atual
            2. Pontos fortes identificados
            3. Áreas que precisam de atenção
            4. Recomendações específicas para melhorar cada métrica
            5. Metas sugeridas para os próximos 30 dias
            """
            
            response = self.openai_client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "Você é um analista de negócios especializado em métricas e KPIs para pequenos e médios empreendedores."},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1000,
                temperature=0.7
            )
            
            return {
                'success': True,
                'analysis': response.choices[0].message.content,
                'metrics': metrics
            }
            
        except Exception as e:
            return {
                'success': False,
                'error': str(e)
            }

