from models.user import UserModel
import bcrypt


def authenticate(username, password):
    user = UserModel.find_by_username(username)
    if user and bcrypt.checkpw(password.encode(), user.password_hash):
        return user


def identity(payload):
    user_id = payload['identity']
    return UserModel.find_by_id(user_id)