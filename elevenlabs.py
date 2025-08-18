from flask import Blueprint, request, jsonify, send_file
import requests
import os
import tempfile
import uuid
from datetime import datetime

elevenlabs_bp = Blueprint('elevenlabs', __name__)

# Configuração da API ElevenLabs
ELEVENLABS_API_URL = "https://api.elevenlabs.io/v1"
ELEVENLABS_API_KEY = os.getenv('ELEVENLABS_API_KEY', 'sk_64ec45f1d9009448a521bb142fa02aad9318e7c2dbb4d678')
ANNA_AGENT_ID = os.getenv('ANNA_AGENT_ID', 'agent_4501k2afd14xfres2jbtd5hm3d0j')

@elevenlabs_bp.route('/text-to-speech', methods=['POST'])
def text_to_speech():
    """
    Endpoint para converter texto em fala usando ElevenLabs
    """
    try:
        data = request.get_json()
        text = data.get('text', '')
        voice_id = data.get('voice_id', 'pNInz6obpgDQGcFmaJgB')  # Adam voice por padrão
        
        if not text:
            return jsonify({'error': 'Texto é obrigatório'}), 400
        
        # Configuração da requisição para ElevenLabs
        headers = {
            'Accept': 'audio/mpeg',
            'Content-Type': 'application/json',
            'xi-api-key': ELEVENLABS_API_KEY
        }
        
        payload = {
            "text": text,
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
                "stability": 0.5,
                "similarity_boost": 0.5
            }
        }
        
        # Fazer a requisição para ElevenLabs
        response = requests.post(
            f"{ELEVENLABS_API_URL}/text-to-speech/{voice_id}",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            # Salvar o arquivo de áudio temporariamente
            temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.mp3')
            temp_file.write(response.content)
            temp_file.close()
            
            return send_file(
                temp_file.name,
                mimetype='audio/mpeg',
                as_attachment=True,
                download_name=f'speech_{uuid.uuid4().hex[:8]}.mp3'
            )
        else:
            return jsonify({
                'error': f'Erro na API ElevenLabs: {response.status_code}',
                'message': response.text
            }), response.status_code
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@elevenlabs_bp.route('/voice-chat', methods=['POST'])
def voice_chat():
    """
    Endpoint para chat de voz com o agente Anna
    """
    try:
        data = request.get_json()
        message = data.get('message', '')
        
        if not message:
            return jsonify({'error': 'Mensagem é obrigatória'}), 400
        
        # Configuração da requisição para o agente Anna
        headers = {
            'Content-Type': 'application/json',
            'xi-api-key': ELEVENLABS_API_KEY
        }
        
        payload = {
            "text": message
        }
        
        # Fazer a requisição para o agente Anna
        response = requests.post(
            f"{ELEVENLABS_API_URL}/convai/agents/{ANNA_AGENT_ID}/conversation",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            result = response.json()
            
            return jsonify({
                'success': True,
                'response': result.get('response', ''),
                'audio_url': result.get('audio_url', ''),
                'conversation_id': result.get('conversation_id', ''),
                'timestamp': datetime.now().isoformat()
            })
        else:
            return jsonify({
                'error': f'Erro na API ElevenLabs: {response.status_code}',
                'message': response.text
            }), response.status_code
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@elevenlabs_bp.route('/voices', methods=['GET'])
def get_voices():
    """
    Endpoint para listar vozes disponíveis
    """
    try:
        headers = {
            'xi-api-key': ELEVENLABS_API_KEY
        }
        
        response = requests.get(f"{ELEVENLABS_API_URL}/voices", headers=headers)
        
        if response.status_code == 200:
            voices = response.json()
            
            # Filtrar apenas as informações essenciais
            simplified_voices = []
            for voice in voices.get('voices', []):
                simplified_voices.append({
                    'voice_id': voice.get('voice_id'),
                    'name': voice.get('name'),
                    'category': voice.get('category'),
                    'description': voice.get('description', ''),
                    'preview_url': voice.get('preview_url', '')
                })
            
            return jsonify({
                'success': True,
                'voices': simplified_voices
            })
        else:
            return jsonify({
                'error': f'Erro na API ElevenLabs: {response.status_code}',
                'message': response.text
            }), response.status_code
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@elevenlabs_bp.route('/anna-agent/start-conversation', methods=['POST'])
def start_anna_conversation():
    """
    Endpoint para iniciar uma conversa com o agente Anna
    """
    try:
        headers = {
            'Content-Type': 'application/json',
            'xi-api-key': ELEVENLABS_API_KEY
        }
        
        payload = {
            "require_auth": False
        }
        
        response = requests.post(
            f"{ELEVENLABS_API_URL}/convai/agents/{ANNA_AGENT_ID}/conversation",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            result = response.json()
            
            return jsonify({
                'success': True,
                'conversation_id': result.get('conversation_id', ''),
                'agent_id': ANNA_AGENT_ID,
                'status': 'conversation_started'
            })
        else:
            return jsonify({
                'error': f'Erro na API ElevenLabs: {response.status_code}',
                'message': response.text
            }), response.status_code
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@elevenlabs_bp.route('/anna-agent/send-message', methods=['POST'])
def send_message_to_anna():
    """
    Endpoint para enviar mensagem para o agente Anna
    """
    try:
        data = request.get_json()
        conversation_id = data.get('conversation_id', '')
        message = data.get('message', '')
        
        if not conversation_id or not message:
            return jsonify({'error': 'conversation_id e message são obrigatórios'}), 400
        
        headers = {
            'Content-Type': 'application/json',
            'xi-api-key': ELEVENLABS_API_KEY
        }
        
        payload = {
            "text": message,
            "conversation_id": conversation_id
        }
        
        response = requests.post(
            f"{ELEVENLABS_API_URL}/convai/agents/{ANNA_AGENT_ID}/conversation",
            headers=headers,
            json=payload
        )
        
        if response.status_code == 200:
            result = response.json()
            
            return jsonify({
                'success': True,
                'response_text': result.get('response', ''),
                'audio_url': result.get('audio_url', ''),
                'conversation_id': conversation_id,
                'timestamp': datetime.now().isoformat()
            })
        else:
            return jsonify({
                'error': f'Erro na API ElevenLabs: {response.status_code}',
                'message': response.text
            }), response.status_code
            
    except Exception as e:
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

