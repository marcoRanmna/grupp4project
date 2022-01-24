from website.persistence.repository import user_repository


def create_user(first_name, last_name, email, password):
    user = {
        'first_name': first_name,
        'last_name': last_name,
        'full_name': f'{first_name} {last_name}',
        'email': email,
        'password': password
    }

    user_repository.create_user(user)
