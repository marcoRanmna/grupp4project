def activity(user_training):
    if user_training == 0:
        user_training = "Little to no exercise"
        return user_training

    elif user_training == 1 or user_training <= 3:
        user_training = "Light: exercise"
        return user_training

    elif user_training == 4 or user_training <= 5:
        user_training = "Moderate: exercise"
        return user_training

    elif user_training == 6 or user_training <= 7:
        user_training = "Very Active: Intense exercise"
        return user_training
