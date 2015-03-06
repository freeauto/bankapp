from flask import render_template
from flask_wtf import Form
from wtforms.validators import DataRequired

from main import app
import wtforms as wtf


class SubscribeForm(Form):
    first_name = wtf.StringField(label='First Name', validators=[DataRequired()])
    last_name = wtf.StringField(label='Last Name', validators=[DataRequired()])
    email = wtf.StringField(label='Your Email', validators=[DataRequired()])
    zip = wtf.StringField(lable='Zip Code', validators=[DataRequired()])

@app.route('/')
def home_view():
    return render_template('home.html')

@app.route('/form', methods=['GET', 'POST'])
def form_view():
    form = SubscribeForm()
    if form.validate_on_submit():
        return "Thanks"
    return render_template('form.html', form=form)

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

