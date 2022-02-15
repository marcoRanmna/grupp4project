import datetime

from passlib.hash import argon2
from website.persistence.repository import user_repository
from flask_login import login_user, current_user, logout_user


def create_user(first_name, last_name, email, password):
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'full_name': f'{first_name} {last_name}',
        'email': email,
        'password': argon2.using(rounds=12).hash(password),
        'date_created': datetime.datetime.now(),
        'last_signin': None,
        'bio': "Write something about yourself",
        "goal_weight": None,
        "start_weight": None,
        "current_weight": None
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
        diary_entry.user_id = user_repository.get_user_by_id(diary_entry.user_id)
        diary_entry.diary_note
        diary_entry.diary_created

    return diary_entries


def add_data(date, steps, training_time, weight, calories_eaten, calories_burned, average_pulse, highest_pulse, lowest_pulse, average_stress, average_o2):
    data = {
        "user_id": current_user._id,
        "date": date,
        "steps": steps,
        "training_time": training_time,
        "weight": weight,
        "calories_eaten": calories_eaten,
        "calories_burned": calories_burned,
        "average_pulse": average_pulse,
        "highest_pulse": highest_pulse,
        "lowest_pulse": lowest_pulse,
        "average_stress": average_stress,
        "average_o2": average_o2
    }
    user_repository.add_data(data)


def add_training(date, training_form, average_pulse, duration):
    training = {
        "user_id": current_user._id,
        "date": date,
        "training_form": training_form,
        "average_pulse": average_pulse,
        "duration": duration + "min"
    }
    user_repository.add_training(training)


def add_sleep(date, total_sleep, deep_sleep, light_sleep):
    sleep = {
        "user_id": current_user._id,
        "date": date,
        "total_sleep": total_sleep,
        "deep_sleep": deep_sleep,
        "light_sleep": light_sleep
    }
    user_repository.add_sleep(sleep)


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


def weight_progress(goal_weight, start_weight, current_weight, calorie_goal):
    user = user_repository.get_user_by_id(current_user._id)
    user.goal_weight = goal_weight
    user.start_weight = start_weight
    user.current_weight = current_weight
    user.calorie_goal = calorie_goal
    user.save()


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


def get_training_for_user_by_date(date):
    training_data = user_repository.get_training_data_by_id(current_user._id)
    training_for_date = []
    for data in training_data:
        if data.date == date:
            training_for_date.append(data)
    return training_for_date


def get_sleep_for_user_by_date(date):
    sleep_data = user_repository.get_sleep_data_by_id(current_user._id)
    sleep_for_date = []
    for data in sleep_data:
        if data.date == date:
            sleep_for_date.append(data)
    return sleep_for_date


def get_data_for_user():
    return user_repository.get_data_by_id(current_user._id)


def get_training_data_by_id():
    return user_repository.get_last_training_data_by_id(current_user._id)


def get_sleep_data_by_id():
    return user_repository.get_last_sleep_data_by_id(current_user._id)
