import datetime
from website.persistence.repository import user_repository
from flask_login import login_user


def create_user(first_name, last_name, email, password):
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'full_name': f'{first_name} {last_name}',
        'email': email,
        'password': password,
        'date_created': datetime.datetime.now(),
        'last_signin': None
    }

    user_repository.create_user(user)


def add_data(date, steps, weight, calories_eaten, calories_burned, average_pulse):
    data = {
        "date": date,
        "steps": steps,
        "weight": weight,
        "calories_eaten": calories_eaten,
        "calories_burned": calories_burned,
        "average_pulse": average_pulse
    }
    user_repository.add_data(data)


def get_user_by_email(email):
    return user_repository.get_user_by_email(email)


def signin_user(email):
    user = get_user_by_email(email)
    if user is not None:
        login_user(user)
        user.last_signin = datetime.datetime.now()
        user.save()


def verify_user(email, password):
    user = user_repository.get_user_by_email(email)
    if user is None:
        return False
