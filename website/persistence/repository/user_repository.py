from website.persistence.models import User, Data, Training, Sleep


def get_user_by_id(user_id):
    return User.find(_id=user_id).first_or_none()


def get_data_by_id(user_id):
    return Data.find(user_id=user_id)


def get_training_data_by_id(user_id):
    return Training.find(user_id=user_id)


def get_sleep_data_by_id(user_id):
    return Sleep.find(user_id=user_id)


def create_user(user):
    User(user).save()


def add_diary_note(diary: dict):
    from website.persistence.models import Diary
    Diary(diary).save()


def get_all_diary_notes_for_user(user_id):
    from website.persistence.models import Diary
    return Diary.find(user_id=user_id)


def get_diary_note_by_id(object_id):
    from website.persistence.models import Diary
    return Diary.find(_id=object_id).first_or_none()


def add_data(data):
    Data(data).save()


def add_training(training):
    Training(training).save()


def add_sleep(sleep):
    Sleep(sleep).save()


def get_user_by_email(email):
    return User.find(email=email).first_or_none()


def get_last_training_data_by_id(user_id):
    return Training.find(user_id=user_id).last_or_none()


def get_last_sleep_data_by_id(user_id):
    return Sleep.find(user_id=user_id).last_or_none()
