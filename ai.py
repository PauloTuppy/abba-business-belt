from flask import Blueprint, request, jsonify
from src.services.ai_agent import BusinessAIAgent
from src.models.business import Business, AIRecommendation
from src.models.user import db
import json

ai_bp = Blueprint('ai', __name__)
ai_agent = BusinessAIAgent()

@ai_bp.route('/ai/business-recommendations', methods=['POST'])
def get_business_recommendations():
    """Get AI-powered business recommendations"""
    try:
        data = request.get_json()
        business_type = data.get('business_type', '')
        query = data.get('query', '')
        business_id = data.get('business_id')
        
        if not business_type or not query:
            return jsonify({
                'success': False,
                'error': 'business_type and query are required'
            }), 400
        
        # Get recommendations from AI agent
        result = ai_agent.search_business_practices(business_type, query)
        
        if result['success'] and business_id:
            # Save recommendation to database
            ai_rec = AIRecommendation(
                business_id=business_id,
                query=f"{business_type}: {query}",
                recommendation=result['recommendations'],
                sources=json.dumps(result.get('sources', []))
            )
            db.session.add(ai_rec)
            db.session.commit()
            
            result['recommendation_id'] = ai_rec.id
        
        return jsonify(result)
        
    except Exception as e:
        if business_id:
            db.session.rollback()
        return jsonify({'success': False, 'error': str(e)}), 500

@ai_bp.route('/ai/belt-content/<string:belt_level>', methods=['POST'])
def get_belt_specific_content(belt_level):
    """Get content specific to user's belt level"""
    try:
        data = request.get_json()
        business_type = data.get('business_type', '')
        
        if not business_type:
            return jsonify({
                'success': False,
                'error': 'business_type is required'
            }), 400
        
        result = ai_agent.generate_belt_specific_content(belt_level, business_type)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@ai_bp.route('/ai/analyze-metrics', methods=['POST'])
def analyze_business_metrics():
    """Analyze business metrics and provide insights"""
    try:
        data = request.get_json()
        business_id = data.get('business_id')
        
        if business_id:
            # Get metrics from database
            business = Business.query.get_or_404(business_id)
            metrics = {
                'monthly_revenue': business.monthly_revenue,
                'active_customers': business.active_customers,
                'conversion_rate': business.conversion_rate,
                'goals_completed': business.goals_completed,
                'total_goals': business.total_goals
            }
        else:
            # Use provided metrics
            metrics = {
                'monthly_revenue': data.get('monthly_revenue', 0),
                'active_customers': data.get('active_customers', 0),
                'conversion_rate': data.get('conversion_rate', 0),
                'goals_completed': data.get('goals_completed', 0),
                'total_goals': data.get('total_goals', 5)
            }
        
        result = ai_agent.analyze_business_metrics(metrics)
        return jsonify(result)
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@ai_bp.route('/ai/quick-tips/<string:category>', methods=['GET'])
def get_quick_tips(category):
    """Get quick tips for specific business categories"""
    try:
        tips_database = {
            'marketing': [
                "Defina claramente sua proposta de valor única",
                "Conheça profundamente seu público-alvo",
                "Use redes sociais onde seus clientes estão",
                "Meça sempre os resultados das suas campanhas",
                "Invista em conteúdo de qualidade"
            ],
            'finance': [
                "Separe sempre as finanças pessoais das empresariais",
                "Mantenha um controle rigoroso de fluxo de caixa",
                "Reserve uma porcentagem da receita para emergências",
                "Acompanhe seus indicadores financeiros mensalmente",
                "Negocie prazos de pagamento favoráveis"
            ],
            'sales': [
                "Escute mais do que fala durante vendas",
                "Entenda a dor real do seu cliente",
                "Tenha um processo de vendas bem definido",
                "Faça follow-up consistente com leads",
                "Peça sempre feedback após a venda"
            ],
            'operations': [
                "Documente todos os seus processos importantes",
                "Automatize tarefas repetitivas sempre que possível",
                "Mantenha a qualidade consistente em todos os produtos/serviços",
                "Invista em ferramentas que aumentem sua produtividade",
                "Tenha backup de dados e processos críticos"
            ],
            'growth': [
                "Foque em reter clientes antes de buscar novos",
                "Meça e otimize sua taxa de conversão",
                "Desenvolva parcerias estratégicas",
                "Invista em capacitação da equipe",
                "Mantenha-se atualizado com tendências do mercado"
            ]
        }
        
        tips = tips_database.get(category, [])
        
        if not tips:
            return jsonify({
                'success': False,
                'error': f'Category {category} not found'
            }), 404
        
        return jsonify({
            'success': True,
            'category': category,
            'tips': tips
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

@ai_bp.route('/ai/business-health-check', methods=['POST'])
def business_health_check():
    """Perform a comprehensive business health check"""
    try:
        data = request.get_json()
        business_id = data.get('business_id')
        
        if not business_id:
            return jsonify({
                'success': False,
                'error': 'business_id is required'
            }), 400
        
        business = Business.query.get_or_404(business_id)
        
        # Calculate health score based on various factors
        health_score = 0
        max_score = 100
        
        # Revenue health (25 points)
        if business.monthly_revenue > 0:
            health_score += 25
        elif business.monthly_revenue > 1000:
            health_score += 20
        elif business.monthly_revenue > 5000:
            health_score += 25
        
        # Customer base health (25 points)
        if business.active_customers > 0:
            health_score += 15
        if business.active_customers > 10:
            health_score += 20
        if business.active_customers > 50:
            health_score += 25
        
        # Conversion health (25 points)
        if business.conversion_rate > 0:
            health_score += 10
        if business.conversion_rate > 2:
            health_score += 20
        if business.conversion_rate > 5:
            health_score += 25
        
        # Goal completion health (25 points)
        goal_completion_rate = (business.goals_completed / business.total_goals) * 100 if business.total_goals > 0 else 0
        health_score += min(25, int(goal_completion_rate * 0.25))
        
        # Determine health status
        if health_score >= 80:
            status = "Excelente"
            color = "green"
        elif health_score >= 60:
            status = "Bom"
            color = "blue"
        elif health_score >= 40:
            status = "Regular"
            color = "yellow"
        else:
            status = "Precisa de Atenção"
            color = "red"
        
        recommendations = []
        if business.monthly_revenue == 0:
            recommendations.append("Foque em gerar suas primeiras vendas")
        if business.active_customers < 10:
            recommendations.append("Trabalhe na aquisição de mais clientes")
        if business.conversion_rate < 2:
            recommendations.append("Otimize seu processo de vendas")
        if goal_completion_rate < 50:
            recommendations.append("Concentre-se em completar suas metas")
        
        return jsonify({
            'success': True,
            'business_id': business_id,
            'health_score': health_score,
            'max_score': max_score,
            'status': status,
            'color': color,
            'recommendations': recommendations,
            'metrics': {
                'monthly_revenue': business.monthly_revenue,
                'active_customers': business.active_customers,
                'conversion_rate': business.conversion_rate,
                'goal_completion_rate': goal_completion_rate
            }
        })
        
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)}), 500

