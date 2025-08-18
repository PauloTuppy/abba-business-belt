from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from src.models.user import db

class Business(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    name = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    business_type = db.Column(db.String(100), nullable=True)
    current_belt = db.Column(db.String(20), default='white')
    points = db.Column(db.Integer, default=0)
    monthly_revenue = db.Column(db.Float, default=0.0)
    active_customers = db.Column(db.Integer, default=0)
    conversion_rate = db.Column(db.Float, default=0.0)
    goals_completed = db.Column(db.Integer, default=0)
    total_goals = db.Column(db.Integer, default=5)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f'<Business {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'name': self.name,
            'description': self.description,
            'business_type': self.business_type,
            'current_belt': self.current_belt,
            'points': self.points,
            'monthly_revenue': self.monthly_revenue,
            'active_customers': self.active_customers,
            'conversion_rate': self.conversion_rate,
            'goals_completed': self.goals_completed,
            'total_goals': self.total_goals,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'updated_at': self.updated_at.isoformat() if self.updated_at else None
        }

class Goal(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    target_value = db.Column(db.Float, nullable=True)
    current_value = db.Column(db.Float, default=0.0)
    is_completed = db.Column(db.Boolean, default=False)
    points_reward = db.Column(db.Integer, default=10)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    completed_at = db.Column(db.DateTime, nullable=True)

    def __repr__(self):
        return f'<Goal {self.title}>'

    def to_dict(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'title': self.title,
            'description': self.description,
            'target_value': self.target_value,
            'current_value': self.current_value,
            'is_completed': self.is_completed,
            'points_reward': self.points_reward,
            'progress_percentage': (self.current_value / self.target_value * 100) if self.target_value else 0,
            'created_at': self.created_at.isoformat() if self.created_at else None,
            'completed_at': self.completed_at.isoformat() if self.completed_at else None
        }

class AIRecommendation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    business_id = db.Column(db.Integer, db.ForeignKey('business.id'), nullable=False)
    query = db.Column(db.Text, nullable=False)
    recommendation = db.Column(db.Text, nullable=False)
    sources = db.Column(db.Text, nullable=True)  # JSON string of sources
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<AIRecommendation {self.id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'business_id': self.business_id,
            'query': self.query,
            'recommendation': self.recommendation,
            'sources': self.sources,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

