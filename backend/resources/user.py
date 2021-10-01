from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token
from models.user import UserModel
import bcrypt

class UserRegister(Resource):
    TABLE_NAME = 'user'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        username = data['username']
        if UserModel.find_by_username(username):
            return {"message": "User with that username already exists."}, 400
        
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

        user = UserModel(username, hashed)
        # user = UserModel(**data)
        user.save_to_db()
        access_token = create_access_token(identity=username)

        return {"access_token": access_token}, 201

class UserLogin(Resource):
    TABLE_NAME = 'user'

    parser = reqparse.RequestParser()
    parser.add_argument('username',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )
    parser.add_argument('password',
                        type=str,
                        required=True,
                        help="This field cannot be left blank!"
                        )

    def post(self):
        data = UserRegister.parser.parse_args()
        username = data['username']
        password = data['password']
        user = UserModel.find_by_username(username)  
        if user is None:
            return {"message": "This user does not exist"}, 400

        elif user and bcrypt.checkpw(password.encode(), user.password_hash):
            access_token = create_access_token(identity=username)
            return {"access_token": access_token}, 201
