from website.persistence.models import User, Data


def create_user(user):
    User(user).save()


def add_diary_note(diary: dict):
    from website.persistence.models import Diary
    Diary(diary).save()


def get_all_diary_notes_for_user(user_id):
    from website.persistence.models import Diary
    return Diary.find(user_id=user_id)


def add_data(data):
    Data(data).save()


def get_user_by_email(email):
    return User.find(email=email).first_or_none()
    