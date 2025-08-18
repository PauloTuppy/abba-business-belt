from flask import Blueprint, request, jsonify
import requests
import os

revenuecat_bp = Blueprint('revenuecat', __name__)

# RevenueCat configuration
REVENUECAT_API_KEY = os.getenv('REVENUECAT_API_KEY', 'your_revenuecat_api_key_here')
REVENUECAT_BASE_URL = 'https://api.revenuecat.com/v1'

@revenuecat_bp.route('/revenuecat/subscriber/<string:user_id>', methods=['GET'])
def get_subscriber_info(user_id):
    """Get subscriber information from RevenueCat"""
    try:
        headers = {
            'Authorization': f'Bearer {REVENUECAT_API_KEY}',
            'Content-Type': 'application/json'
        }
        
        response = requests.get(
            f'{REVENUECAT_BASE_URL}/subscribers/{user_id}',
            headers=headers
        )
        
        if response.status_code == 200:
            subscriber_data = response.json()
            return jsonify({
                'success': True,
                'subscriber': subscriber_data
            })
        else:
            return jsonify({
                'success': False,
                'error': 'Failed to fetch subscriber info',
                'status_code': response.status_code
            }), response.status_code
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@revenuecat_bp.route('/revenuecat/webhook', methods=['POST'])
def revenuecat_webhook():
    """Handle RevenueCat webhooks for subscription events"""
    try:
        data = request.get_json()
        event_type = data.get('type')
        
        # Handle different webhook events
        if event_type == 'INITIAL_PURCHASE':
            # User made their first purchase
            user_id = data.get('app_user_id')
            product_id = data.get('product_id')
            
            # Here you would update the user's subscription status
            # and unlock premium features
            
            return jsonify({
                'success': True,
                'message': f'Initial purchase processed for user {user_id}'
            })
            
        elif event_type == 'RENEWAL':
            # Subscription renewed
            user_id = data.get('app_user_id')
            
            return jsonify({
                'success': True,
                'message': f'Renewal processed for user {user_id}'
            })
            
        elif event_type == 'CANCELLATION':
            # Subscription cancelled
            user_id = data.get('app_user_id')
            
            return jsonify({
                'success': True,
                'message': f'Cancellation processed for user {user_id}'
            })
            
        else:
            return jsonify({
                'success': True,
                'message': f'Webhook event {event_type} received'
            })
            
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@revenuecat_bp.route('/revenuecat/products', methods=['GET'])
def get_products():
    """Get available products/subscriptions"""
    try:
        # In a real implementation, you would fetch this from RevenueCat
        # For now, we'll return mock data
        products = [
            {
                'id': 'business_belt_premium_monthly',
                'title': 'Business Belt Premium - Mensal',
                'description': 'Acesso completo a todas as funcionalidades premium',
                'price': 'R$ 29,90',
                'currency': 'BRL',
                'period': 'monthly',
                'features': [
                    'Acesso a todas as faixas',
                    'Relatórios avançados',
                    'Suporte prioritário',
                    'Integração com ferramentas externas',
                    'Conteúdo educacional premium'
                ]
            },
            {
                'id': 'business_belt_premium_yearly',
                'title': 'Business Belt Premium - Anual',
                'description': 'Acesso completo com desconto anual',
                'price': 'R$ 299,90',
                'currency': 'BRL',
                'period': 'yearly',
                'discount': '17% de desconto',
                'features': [
                    'Acesso a todas as faixas',
                    'Relatórios avançados',
                    'Suporte prioritário',
                    'Integração com ferramentas externas',
                    'Conteúdo educacional premium',
                    'Consultoria mensal gratuita'
                ]
            },
            {
                'id': 'business_belt_upgrade',
                'title': 'Upgrade de Faixa',
                'description': 'Desbloqueie a próxima faixa instantaneamente',
                'price': 'R$ 9,90',
                'currency': 'BRL',
                'period': 'one_time',
                'features': [
                    'Acesso imediato à próxima faixa',
                    'Novas ferramentas desbloqueadas',
                    'Conteúdo educacional avançado'
                ]
            }
        ]
        
        return jsonify({
            'success': True,
            'products': products
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@revenuecat_bp.route('/revenuecat/purchase', methods=['POST'])
def process_purchase():
    """Process a purchase (mock implementation)"""
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        product_id = data.get('product_id')
        
        if not user_id or not product_id:
            return jsonify({
                'success': False,
                'error': 'user_id and product_id are required'
            }), 400
        
        # In a real implementation, you would:
        # 1. Validate the purchase with RevenueCat
        # 2. Update the user's subscription status
        # 3. Unlock premium features
        
        # Mock successful purchase
        return jsonify({
            'success': True,
            'message': f'Purchase of {product_id} processed for user {user_id}',
            'transaction_id': f'txn_{user_id}_{product_id}_mock',
            'status': 'completed'
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@revenuecat_bp.route('/revenuecat/restore', methods=['POST'])
def restore_purchases():
    """Restore previous purchases for a user"""
    try:
        data = request.get_json()
        user_id = data.get('user_id')
        
        if not user_id:
            return jsonify({
                'success': False,
                'error': 'user_id is required'
            }), 400
        
        # In a real implementation, you would fetch the user's purchase history
        # from RevenueCat and restore their subscription status
        
        return jsonify({
            'success': True,
            'message': f'Purchases restored for user {user_id}',
            'restored_products': []  # Would contain actual restored products
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

