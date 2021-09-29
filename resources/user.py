from flask_restful import Resource, reqparse
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

        if UserModel.find_by_username(data['username']):
            return {"message": "User with that username already exists."}, 400
        
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())

        user = UserModel(data['username'], hashed)
        # user = UserModel(**data)
        user.save_to_db()

        return {"message": "User created successfully."}, 201


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
        data = UserLogin.parser.parse_args()
        
        user = UserModel.find_by_username(data['username'])
        

        if bcrypt.checkpw(data['password'].encode(), user.password_hash):
            return {"message": "Welcome"}