from website.persistence.models import User, Data


def get_user_by_id(user_id):
    return User.find(_id=user_id).first_or_none()


def create_user(user):
    User(user).save()


def add_data(data):
    Data(data).save()


def get_user_by_email(email):
    return User.find(email=email).first_or_none()


def get_user_data():
    return User.find
    