from flask import Flask
from flask_restful import Api
from db import db 
from dotenv import load_dotenv, find_dotenv
from flask_jwt_extended import JWTManager
from security import authenticate, identity
from resources.user import UserRegister, UserLogin
import os

load_dotenv(find_dotenv())

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI']=os.getenv('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = os.getenv('SECRET_KEY')
jwt = JWTManager(app)
api = Api(app)



# create all the tables before the first request
@app.before_first_request
def create_tables():
    db.create_all()




api.add_resource(UserRegister, '/register')
api.add_resource(UserLogin, '/login')


if __name__ == '__main__':
    db.init_app(app)
    app.run(port=5000, debug=True)

