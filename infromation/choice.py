def choice(user_choice):
    synonyms_loss = ["lose", "weight loss", "lose weight", "cut"]
    synonyms_gain = ["gain", "weight gain", "gain weight", "bulk"]
    synonyms_maintain = ["maintain", "stay the same", "keep", "maintain weight"]

    if user_choice in synonyms_loss:
        user_choice = "Weight loss"
        return user_choice

    elif user_choice in synonyms_gain:
        user_choice = "Weight gain"
        return user_choice

    else:
        if user_choice in synonyms_maintain:
            user_choice = "Maintain weight"
            return user_choice
    return f"{user_choice}"
