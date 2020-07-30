from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SECRET_KEY'] = '8u3rouhfkjdsfiluh'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
app.config['SERVER_NAME'] = '0.0.0.0'
#
# Turning on echo will crash the app
# app.config['SQLALCHEMY_ECHO'] = 'True'
#

db = SQLAlchemy(app)

from routes import *

if __name__ == '__main__':
    app.run(debug=True)
