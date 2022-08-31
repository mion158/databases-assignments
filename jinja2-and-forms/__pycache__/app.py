from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
app = Flask(__name__)
app.secret_key = 'issasecretkeylol'
#configurate key database to connect to flask application
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///justtravel.db'
#SQLAlchemy object
db = SQLAlchemy(app)
#instantiate LoginManager
login = LoginManager(app)
login.login_view = 'login'


import routes, models