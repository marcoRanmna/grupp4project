import datetime

from passlib.hash import argon2
from website.persistence.repository import user_repository
from flask_login import login_user, current_user, logout_user

from website.persistence.repository.user_repository import get_diary_note_by_id
from website.persistence.repository.user_repository import get_user_by_id


def create_user(first_name, last_name, email, password):
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'full_name': f'{first_name} {last_name}',
        'email': email,
        'password': argon2.using(rounds=12).hash(password),
        'date_created': datetime.datetime.now(),
        'last_signin': None,
        'bio': "Write something about yourself"
    }

    user_repository.create_user(user)


def add_diary_note(diary_note):
    diary_entry = {
        'user_id': current_user._id,
        'diary_note': diary_note,
        'diary_created': datetime.datetime.now()
    }

    user_repository.add_diary_note(diary_entry)


def get_all_diary_notes_for_user():
    diary_entries = user_repository.get_all_diary_notes_for_user(current_user._id)
    for diary_entry in diary_entries:
        diary_entry.user_id = get_user_by_id(diary_entry.user_id)
        diary_entry.diary_note
        diary_entry.diary_created

    return diary_entries


def add_data(date, steps, weight, calories_eaten, calories_burned, average_pulse):
    data = {
        "user_id": current_user._id,
        "date": date,
        "data": {
            "steps": steps,
            "weight": weight,
            "calories_eaten": calories_eaten,
            "calories_burned": calories_burned,
            "average_pulse": average_pulse
        }
    }
    user_repository.add_data(data)


def account_settings(first_name, last_name, email, bio):
    user = user_repository.get_user_by_id(current_user._id)
    print(user)
    user.first_name = first_name
    user.last_name = last_name
    user.full_name = first_name + " " + last_name
    user.email = email
    user.bio = bio
    user.save()
    logout_user()


def password_settings(old_password, new_password):
    if not verify_user(current_user.email, old_password):
        print(current_user)
        return False
    user = user_repository.get_user_by_email(current_user.email)
    user.password = argon2.using(rounds=12).hash(new_password)
    user.save()
    logout_user()
    return True


def get_user_by_email(email):
    return user_repository.get_user_by_email(email)


def signin_user(email):
    user = get_user_by_email(email)
    if user is not None:
        login_user(user)
        user.last_signin = datetime.datetime.now()
        user.save()
    else:
        print("error")


def verify_user(email, password):
    user = user_repository.get_user_by_email(email)
    if user is None:
        print("wrong email")
        return False
    return argon2.verify(password, user.password)


def get_user_data():
    return user_repository.get_user_by_id(current_user._id)


def get_data_for_user_by_date(date):
    data_user = user_repository.get_data_by_id(current_user._id)
    data_for_date = []
    for data in data_user:
        if data.date == date:
            data_for_date.append(data)
    return data_for_date
