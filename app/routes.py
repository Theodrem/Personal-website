from flask import Flask, render_template, request, flash
from app import app
from app.forms import MessageForm
from flask_mail import Mail, Message
import os

app.config['MAIL_PASSWORD'] = os.environ.get('MOT_DE_PASSE')
app.config['MAIL_SERVER']='smtp.office365.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USERNAME'] = 'theotim@outlook.fr'
app.config['MAIL_PASSWORD'] = 'Intelligence97'
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USE_SSL'] = False
mail = Mail(app)



@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def home():
    form = MessageForm()
    if request.method == 'POST':
        if form.validate() == False:
            flash('Remplir tous les champs')
            return render_template('index.html', form=form)
        else:
            msg = Message(form.sujet.data, sender='theotim@outlook.fr', recipients=['theotim@outlook.fr'])
            msg.body = "Nom = {}, mail = {}, msg = {}".format(form.nom.data, form.email.data, form.message.data)
            mail.send(msg)
            return 'form_posted'

    elif request.method == 'GET':
        return render_template('index.html', form=form)





