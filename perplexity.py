from flask import Blueprint, request, jsonify
import requests
import os

perplexity_bp = Blueprint('perplexity', __name__)

# Configuração da API Perplexity
PERPLEXITY_API_URL = "https://api.perplexity.ai/chat/completions"
PERPLEXITY_API_KEY = os.getenv('PERPLEXITY_API_KEY', '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')

@perplexity_bp.route('/search', methods=['POST'])
def search_with_perplexity():
    """
    Endpoint para realizar buscas usando a API da Perplexity
    """
    try:
        data = request.get_json()
        query = data.get('query', '')
        
        if not query:
            return jsonify({'error': 'Query é obrigatória'}), 400
        
        # Configuração da requisição para Perplexity
        headers = {
            'Authorization': f'Bearer {PERPLEXITY_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            "model": "llama-3.1-sonar-small-128k-online",
            "messages": [
                {
                    "role": "system",
                    "content": "Você é um assistente especializado em pesquisa para empreendedores brasileiros. Forneça informações precisas, atualizadas e relevantes sobre negócios, marketing, finanças e empreendedorismo."
                },
                {
                    "role": "user",
                    "content": f"Pesquise e forneça informações detalhadas sobre: {query}"
                }
            ],
            "max_tokens": 1000,
            "temperature": 0.2,
            "top_p": 0.9,
            "return_citations": True,
            "search_domain_filter": ["perplexity.ai"],
            "return_images": False,
            "return_related_questions": True,
            "search_recency_filter": "month",
            "top_k": 0,
            "stream": False,
            "presence_penalty": 0,
            "frequency_penalty": 1
        }
        
        # Fazer a requisição para Perplexity
        response = requests.post(PERPLEXITY_API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            
            # Extrair informações relevantes da resposta
            content = result['choices'][0]['message']['content']
            citations = result.get('citations', [])
            related_questions = result.get('related_questions', [])
            
            return jsonify({
                'success': True,
                'content': content,
                'citations': citations,
                'related_questions': related_questions,
                'query': query
            })
        else:
            return jsonify({
                'error': f'Erro na API Perplexity: {response.status_code}',
                'message': response.text
            }), response.status_code
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@perplexity_bp.route('/quick-search', methods=['GET'])
def quick_search():
    """
    Endpoint para busca rápida com query parameter
    """
    try:
        query = request.args.get('q', '')
        
        if not query:
            return jsonify({'error': 'Parâmetro q (query) é obrigatório'}), 400
        
        # Usar o mesmo endpoint de search
        return search_with_perplexity()
        
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@perplexity_bp.route('/trending-topics', methods=['GET'])
def get_trending_topics():
    """
    Endpoint para obter tópicos em alta para empreendedores
    """
    try:
        headers = {
            'Authorization': f'Bearer {PERPLEXITY_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            "model": "llama-3.1-sonar-small-128k-online",
            "messages": [
                {
                    "role": "system",
                    "content": "Você é um especialista em tendências de negócios e empreendedorismo no Brasil."
                },
                {
                    "role": "user",
                    "content": "Quais são os 5 tópicos mais relevantes e em alta para empreendedores brasileiros neste momento? Forneça uma lista concisa com explicações breves."
                }
            ],
            "max_tokens": 500,
            "temperature": 0.3,
            "return_citations": True,
            "search_recency_filter": "week"
        }
        
        response = requests.post(PERPLEXITY_API_URL, headers=headers, json=payload)
        
        if response.status_code == 200:
            result = response.json()
            content = result['choices'][0]['message']['content']
            
            return jsonify({
                'success': True,
                'trending_topics': content,
                'timestamp': result.get('created', '')
            })
        else:
            return jsonify({
                'error': f'Erro na API Perplexity: {response.status_code}',
                'message': response.text
            }), response.status_code
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

