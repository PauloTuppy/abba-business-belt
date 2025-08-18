from flask import Blueprint, request, jsonify
import os
import jwt
import time
from datetime import datetime, timedelta

streamchat_bp = Blueprint('streamchat', __name__)

# Configuração do StreamChat
STREAM_API_KEY = os.getenv('STREAM_API_KEY', 'p744wjdfmg6c')
STREAM_API_SECRET = os.getenv('STREAM_API_SECRET', 'avmjgmm6fcat3ex7je3t94paaj88m7p8nrsm4p7hkuu8y5pvpsspv49k5vb9d9ae')

def create_stream_token(user_id, exp=None):
    """
    Cria um token JWT para autenticação no StreamChat
    """
    payload = {
        'user_id': user_id,
        'iat': int(time.time())
    }
    
    if exp:
        payload['exp'] = exp
    else:
        # Token válido por 24 horas por padrão
        payload['exp'] = int(time.time()) + (24 * 60 * 60)
    
    return jwt.encode(payload, STREAM_API_SECRET, algorithm='HS256')

@streamchat_bp.route('/get-token', methods=['POST'])
def get_stream_token():
    """
    Endpoint para obter token de autenticação do StreamChat
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id', 'default_user')
        
        # Criar token
        token = create_stream_token(user_id)
        
        return jsonify({
            'success': True,
            'token': token,
            'api_key': STREAM_API_KEY,
            'user_id': user_id,
            'expires_in': 24 * 60 * 60  # 24 horas em segundos
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@streamchat_bp.route('/create-channel', methods=['POST'])
def create_support_channel():
    """
    Endpoint para criar canal de suporte
    """
    try:
        data = request.get_json()
        user_id = data.get('user_id', 'default_user')
        channel_type = data.get('channel_type', 'support')
        channel_id = data.get('channel_id', f'support_{user_id}_{int(time.time())}')
        
        # Dados do canal
        channel_data = {
            'id': channel_id,
            'type': channel_type,
            'created_by_id': user_id,
            'name': f'Suporte - {user_id}',
            'members': [user_id, 'support_bot']
        }
        
        return jsonify({
            'success': True,
            'channel': channel_data,
            'message': 'Canal de suporte criado com sucesso'
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@streamchat_bp.route('/faq', methods=['GET'])
def get_faq():
    """
    Endpoint para obter perguntas frequentes
    """
    try:
        faq_data = [
            {
                'id': 1,
                'question': 'Como funciona o sistema de faixas?',
                'answer': 'O sistema de faixas no abbā funciona como no karatê. Você começa na faixa branca e progride através de diferentes níveis conforme completa desafios e acumula pontos. Cada faixa desbloqueia novas funcionalidades e conteúdos.',
                'category': 'Sistema de Faixas'
            },
            {
                'id': 2,
                'question': 'Como ganho pontos no aplicativo?',
                'answer': 'Você ganha pontos completando módulos educacionais, assistindo vídeos, participando de desafios, usando o assistente de IA, e atingindo metas de negócio. Cada atividade tem uma pontuação específica.',
                'category': 'Pontuação'
            },
            {
                'id': 3,
                'question': 'O que é o assistente de IA?',
                'answer': 'O assistente de IA é uma ferramenta que usa inteligência artificial para buscar as melhores práticas de negócios baseadas na descrição do seu empreendimento. Ele fornece estratégias personalizadas e atualizadas.',
                'category': 'Assistente IA'
            },
            {
                'id': 4,
                'question': 'Como funciona a busca inteligente?',
                'answer': 'A busca inteligente usa a API da Perplexity para encontrar informações atualizadas sobre empreendedorismo, marketing, finanças e outros tópicos relevantes. Você pode fazer perguntas em linguagem natural.',
                'category': 'Busca'
            },
            {
                'id': 5,
                'question': 'O que é a Anna?',
                'answer': 'Anna é sua assistente de voz especializada em negócios. Você pode conversar com ela por voz ou texto para obter conselhos sobre empreendedorismo, estratégias de marketing e muito mais.',
                'category': 'Assistente de Voz'
            },
            {
                'id': 6,
                'question': 'Como acessar o conteúdo premium?',
                'answer': 'O conteúdo premium pode ser acessado através de assinaturas mensais (R$ 29,90) ou anuais (R$ 299,90). Você também pode fazer upgrade de faixa por R$ 9,90 para desbloquear recursos específicos.',
                'category': 'Premium'
            },
            {
                'id': 7,
                'question': 'Os vídeos educacionais são gratuitos?',
                'answer': 'Sim! Todos os vídeos educacionais nas abas de Marketing, Mindset, Mídias Sociais, Dieta e Finanças são gratuitos e estão disponíveis para todos os usuários.',
                'category': 'Conteúdo'
            },
            {
                'id': 8,
                'question': 'Como funciona o dashboard de métricas?',
                'answer': 'O dashboard mostra métricas importantes do seu negócio como receita mensal, clientes ativos, taxa de conversão e metas concluídas. Você pode atualizar esses dados manualmente ou integrar com suas ferramentas.',
                'category': 'Dashboard'
            },
            {
                'id': 9,
                'question': 'Posso usar o app offline?',
                'answer': 'Algumas funcionalidades como visualização de vídeos baixados funcionam offline, mas recursos como assistente de IA, busca inteligente e Anna requerem conexão com internet.',
                'category': 'Funcionalidades'
            },
            {
                'id': 10,
                'question': 'Como entrar em contato com o suporte?',
                'answer': 'Você pode usar este chat de suporte integrado, enviar email para suporte@abba.app ou usar a Anna para questões rápidas sobre o funcionamento do aplicativo.',
                'category': 'Suporte'
            }
        ]
        
        return jsonify({
            'success': True,
            'faq': faq_data,
            'total': len(faq_data)
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@streamchat_bp.route('/search-faq', methods=['POST'])
def search_faq():
    """
    Endpoint para buscar nas perguntas frequentes
    """
    try:
        data = request.get_json()
        query = data.get('query', '').lower()
        
        if not query:
            return jsonify({'error': 'Query é obrigatória'}), 400
        
        # FAQ data (mesmo do endpoint anterior)
        faq_data = [
            {
                'id': 1,
                'question': 'Como funciona o sistema de faixas?',
                'answer': 'O sistema de faixas no abbā funciona como no karatê. Você começa na faixa branca e progride através de diferentes níveis conforme completa desafios e acumula pontos. Cada faixa desbloqueia novas funcionalidades e conteúdos.',
                'category': 'Sistema de Faixas'
            },
            {
                'id': 2,
                'question': 'Como ganho pontos no aplicativo?',
                'answer': 'Você ganha pontos completando módulos educacionais, assistindo vídeos, participando de desafios, usando o assistente de IA, e atingindo metas de negócio. Cada atividade tem uma pontuação específica.',
                'category': 'Pontuação'
            },
            {
                'id': 3,
                'question': 'O que é o assistente de IA?',
                'answer': 'O assistente de IA é uma ferramenta que usa inteligência artificial para buscar as melhores práticas de negócios baseadas na descrição do seu empreendimento. Ele fornece estratégias personalizadas e atualizadas.',
                'category': 'Assistente IA'
            },
            {
                'id': 4,
                'question': 'Como funciona a busca inteligente?',
                'answer': 'A busca inteligente usa a API da Perplexity para encontrar informações atualizadas sobre empreendedorismo, marketing, finanças e outros tópicos relevantes. Você pode fazer perguntas em linguagem natural.',
                'category': 'Busca'
            },
            {
                'id': 5,
                'question': 'O que é a Anna?',
                'answer': 'Anna é sua assistente de voz especializada em negócios. Você pode conversar com ela por voz ou texto para obter conselhos sobre empreendedorismo, estratégias de marketing e muito mais.',
                'category': 'Assistente de Voz'
            },
            {
                'id': 6,
                'question': 'Como acessar o conteúdo premium?',
                'answer': 'O conteúdo premium pode ser acessado através de assinaturas mensais (R$ 29,90) ou anuais (R$ 299,90). Você também pode fazer upgrade de faixa por R$ 9,90 para desbloquear recursos específicos.',
                'category': 'Premium'
            },
            {
                'id': 7,
                'question': 'Os vídeos educacionais são gratuitos?',
                'answer': 'Sim! Todos os vídeos educacionais nas abas de Marketing, Mindset, Mídias Sociais, Dieta e Finanças são gratuitos e estão disponíveis para todos os usuários.',
                'category': 'Conteúdo'
            },
            {
                'id': 8,
                'question': 'Como funciona o dashboard de métricas?',
                'answer': 'O dashboard mostra métricas importantes do seu negócio como receita mensal, clientes ativos, taxa de conversão e metas concluídas. Você pode atualizar esses dados manualmente ou integrar com suas ferramentas.',
                'category': 'Dashboard'
            },
            {
                'id': 9,
                'question': 'Posso usar o app offline?',
                'answer': 'Algumas funcionalidades como visualização de vídeos baixados funcionam offline, mas recursos como assistente de IA, busca inteligente e Anna requerem conexão com internet.',
                'category': 'Funcionalidades'
            },
            {
                'id': 10,
                'question': 'Como entrar em contato com o suporte?',
                'answer': 'Você pode usar este chat de suporte integrado, enviar email para suporte@abba.app ou usar a Anna para questões rápidas sobre o funcionamento do aplicativo.',
                'category': 'Suporte'
            }
        ]
        
        # Buscar nas perguntas e respostas
        results = []
        for item in faq_data:
            if (query in item['question'].lower() or 
                query in item['answer'].lower() or 
                query in item['category'].lower()):
                results.append(item)
        
        return jsonify({
            'success': True,
            'results': results,
            'query': query,
            'total_found': len(results)
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@streamchat_bp.route('/bot-response', methods=['POST'])
def get_bot_response():
    """
    Endpoint para obter resposta automática do bot de suporte
    """
    try:
        data = request.get_json()
        message = data.get('message', '').lower()
        
        # Respostas automáticas baseadas em palavras-chave
        auto_responses = {
            'faixa': 'O sistema de faixas funciona como no karatê! Você progride completando desafios e acumulando pontos. Cada faixa desbloqueia novos recursos.',
            'pontos': 'Você ganha pontos assistindo vídeos, usando o assistente de IA, completando módulos e atingindo metas. Cada atividade tem pontuação específica.',
            'anna': 'Anna é sua assistente de voz! Você pode conversar com ela sobre negócios, marketing e empreendedorismo. Acesse a aba "Assistente de Voz".',
            'busca': 'A busca inteligente usa IA para encontrar informações atualizadas. Faça perguntas em linguagem natural na aba "Busca IA".',
            'premium': 'O conteúdo premium custa R$ 29,90/mês ou R$ 299,90/ano. Você também pode fazer upgrade de faixa por R$ 9,90.',
            'video': 'Todos os vídeos educacionais são gratuitos! Acesse as abas Marketing, Mindset, Mídias Sociais, Dieta e Finanças.',
            'suporte': 'Estou aqui para ajudar! Você também pode enviar email para suporte@abba.app ou usar a Anna para questões rápidas.',
            'offline': 'Algumas funcionalidades funcionam offline, mas IA, busca e Anna precisam de internet.',
            'dashboard': 'O dashboard mostra métricas do seu negócio. Você pode atualizar os dados manualmente ou integrar com suas ferramentas.'
        }
        
        # Encontrar resposta baseada em palavras-chave
        response = None
        for keyword, auto_response in auto_responses.items():
            if keyword in message:
                response = auto_response
                break
        
        if not response:
            response = 'Olá! Sou o bot de suporte do abbā. Como posso ajudar você hoje? Você pode perguntar sobre faixas, pontos, Anna, busca, premium, vídeos ou qualquer funcionalidade do app.'
        
        return jsonify({
            'success': True,
            'response': response,
            'timestamp': datetime.now().isoformat(),
            'is_automated': True
        })
        
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

