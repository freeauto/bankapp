from flask import render_template
from flask_wtf import Form
from wtforms.validators import DataRequired

from main import app
import wtforms as wtf


class SubscribeForm(Form):
    email = wtf.StringField(label='Your Email', validators=[DataRequired()])

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
