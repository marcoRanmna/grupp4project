from website.persistence.models import User


def create_user(user):
    User(user).save()
    