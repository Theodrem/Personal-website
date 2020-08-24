from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,TextAreaField, ValidationError, validators
from wtforms.validators import DataRequired, Email



class MessageForm(FlaskForm):
    nom = StringField('Nom', [validators.DataRequired(message='Entrez un nom valide')])
    sujet = StringField('Sujet', [validators.DataRequired(message='Entrez le sujet du mail')])
    email = StringField('Email', [validators.DataRequired(message='Entrez un email'), Email()])
    message = TextAreaField('Message', [validators.DataRequired(message='Entrez un message')])
    envoyer = SubmitField('Envoyer')
