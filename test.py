from website.controllers.user_controller import create_user, add_data


def main():
    first_name = input(': ')
    last_name = input(': ')
    email = input(': ')
    password = input(': ')
    create_user(first_name, last_name, email, password)


def data():
    date = input(': ')
    steps = int(input(': '))
    weight = int(input(': '))
    calories_eaten = int(input(': '))
    calories_burned = int(input(': '))
    average_pulse = int(input(': '))
    add_data(date, steps, weight, calories_eaten, calories_burned, average_pulse)


if __name__ == '__main__':
    data()
