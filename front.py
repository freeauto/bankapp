from flask import Flask, render_template, request
from flask_wtf import Form
from wtforms.validators import DataRequired
from flask_sqlalchemy import SQLAlchemy

from main import app
import wtforms as wtf

db = SQLAlchemy(app)

#======================== MODEL DEFINITIONS ==========================================

class User(db.Model):
    id = db.Column(db.Integer, nullable=False, primary_key=True)
    first_name = db.Column(db.Text)
    last_name = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text)
    email = db.Column(db.Text, nullable=False, unique=True)
    password = db.Column(db.String)
    applications = db.relationship('LoanApplication', backref='user', lazy='dynamic')
    
    def __repr__(self):
        return '<User %r>' % self.email

class LoanApplication(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    # page 1 - Loan Info
    purpose = db.Column(db.Text, nullable=False)
    collateral = db.Column(db.Text)

#=========================== FORM DEFINITIONS =============================================
class ApplicationForm(Form):
    # Borrower
    first_name = wtf.StringField(validators=[DataRequired()])
    last_name = wtf.StringField(validators=[DataRequired()])
    email = wtf.StringField(validators=[DataRequired()])
    phone = wtf.StringField(validators=[DataRequired()])
    
    address1 = wtf.StringField(validators=[DataRequired()])
    address2 = wtf.StringField(validators=[DataRequired()])
    state = wtf.StringField(validators=[DataRequired()])
    city = wtf.StringField(validators=[DataRequired()])
    zip = wtf.StringField(validators=[DataRequired()])
    
    ssn = wtf.StringField(validators=[DataRequired()])
    birthday = wtf.StringField(validators=[DataRequired()])
    citizenship = wtf.StringField(validators=[DataRequired()])
    driversLicence = wtf.StringField(validators=[DataRequired()])  
    
    # Loan
    purpose = wtf.StringField(validators=[DataRequired()])
    collateral = wtf.StringField(validators=[DataRequired()])
    term = wtf.StringField(validators=[DataRequired()])
    when = wtf.StringField(validators=[DataRequired()])
    how = wtf.StringField(validators=[DataRequired()])
    
    #Financial
    status = wtf.StringField(validators=[DataRequired()])    
    title = wtf.StringField(validators=[DataRequired()])    
    employer = wtf.StringField(validators=[DataRequired()])    
    supervisor = wtf.StringField(validators=[DataRequired()])    
    timeAtJob = wtf.StringField(validators=[DataRequired()])    
    experience = wtf.StringField(validators=[DataRequired()])

    incomeJob = wtf.StringField(validators=[DataRequired()])
    incomeOther = wtf.StringField(validators=[DataRequired()])
    expensesEmployment = wtf.StringField(validators=[DataRequired()])
    expensesInterest = wtf.StringField(validators=[DataRequired()])
    expensesHousing = wtf.StringField(validators=[DataRequired()])
    expensesAlimony = wtf.StringField(validators=[DataRequired()])

    bankruptcy = wtf.StringField(validators=[DataRequired()])    
    outstandingJudgements = wtf.StringField(validators=[DataRequired()])    
    lawsuit = wtf.StringField(validators=[DataRequired()])    
    foreclosed = wtf.StringField(validators=[DataRequired()])    
    repossessedGoods = wtf.StringField(validators=[DataRequired()])    
    obligationsNotListed = wtf.StringField(validators=[DataRequired()])    
    loanObligations = wtf.StringField(validators=[DataRequired()])    
    creditInAnotherName = wtf.StringField(validators=[DataRequired()])    
    alimony = wtf.StringField(validators=[DataRequired()])      
    
    answer = wtf.StringField(validators=[DataRequired()])      
    
class SubscribeForm(Form):
    first_name = wtf.StringField(label='First Name', validators=[DataRequired()])
    last_name = wtf.StringField(label='Last Name', validators=[DataRequired()])
    email = wtf.StringField(label='Your Email', validators=[DataRequired()])
    zip = wtf.StringField(lable='Zip Code', validators=[DataRequired()])
    
#=========================== ROUTES ===================================
# BASIC
@app.route('/')
def home_view():
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def form_view():
    form = SubscribeForm()
    if form.validate_on_submit():
        return "Thanks"
    return render_template('form.html', form=form)
    
# ADMIN
@app.route('/admin/')
def admin_view():
    return render_template('admin/admin.html')

@app.route('/admin/login/')
def admin_login_view():
    return render_template('admin/login.html')

@app.route('/admin/flot/')
def admin_flot_view():
    return render_template('admin/flot.html')

@app.route('/admin/morris/')
def admin_morris_view():
    return render_template('admin/morris.html')

@app.route('/admin/tables/')
def admin_tables_view():
    return render_template('admin/tables.html')

# DEMO
@app.route('/demo.html')
def application_start_view():
    return render_template('/demo/templates/start.html')

@app.route('/<name>/demo.html', methods=['GET', 'POST'])
def application_view(name):
    form = ApplicationForm()
    if form.validate_on_submit():
        loan = LoanApplication(
            #loan.user.first_name = form.first_name.data,
            #loan.user.first_name = form.first_name.data,
            #loan.user.phone = form.phone.data,
            #loan.user.email = form.email.data,
            #loan.purpose = form.purpose.data
            #loan.collateral = form.collateral.data
        )
        print "#blake -- hello"
        print loan
        db.session.add(loan)
        db.session.commit()
        return "Thanks"
        
    if request.method == 'POST':
        return 'Form posted.'
    elif request.method == 'GET':
        return render_template('/demo/templates/application.html', form=form, title=name)

