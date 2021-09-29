from flask import Flask
from flask_restful import Api
from db import db 
from dotenv import load_dotenv, find_dotenv
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
import os

load_dotenv(find_dotenv())

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY')
api = Api(app)



# create all the tables before the first request
@app.before_first_request
def create_tables():
    db.create_all()

app.config['JWT_AUTH_URL_RULE'] = '/login'
jwt = JWT(app, authenticate, identity)

@jwt.jwt_error_handler
def customized_error_handler(error):
    return "The username or password is incorrect", 401

api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

