from website.controllers.user_controller import create_user


def main():
    first_name = input(': ')
    last_name = input(': ')
    email = input(': ')
    password = input(': ')
    create_user(first_name, last_name, email, password)


if __name__ == '__main__':
    main()
