from website.persistence.models import User, Data, Diary


def create_user(user):
    User(user).save()


def add_diary_note(diary):
    Diary(diary).save()


def add_data(data):
    Data(data).save()


def get_user_by_email(email):
    return User.find(email=email).first_or_none()
    