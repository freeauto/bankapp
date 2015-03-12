from flask import render_template
from flask_wtf import Form
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

from main import app

import wtforms as wtf

db = SQLAlchemy(app)
    
#=================================== MODEL DEFINITIONS ==========================================
class User(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.String)
    authenticated = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return '<User %r>' % self.email
        
    def is_active(self):
        return True

    def get_id(self):
        return self.email

    def is_authenticated(self):
        return self.authenticated

    def is_anonymous(self):
        return False
                
class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    user = db.relationship('User', backref='applications')
    
    # page 1 - Loan Info
    purpose = db.Column(db.Text, nullable=False)
    collateral = db.Column(db.Text)
    
    # page 2 - Borrower Info
    # Contact Info
    
    # Address Info
    
    # About Info
    
    # page 6 - 
    