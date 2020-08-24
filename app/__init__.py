from flask import Flask
from flask_mail import Mail


app = Flask(__name__,
            static_folder='templates/static',
            template_folder='templates')

app.config.from_object('config')
mail = Mail(app)

from app import routes



