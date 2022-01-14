from infromation.person import Person
from user_pov.questions import Questions


def main():
    questions = Questions()
    questions.greeting()
    questions.about_user()
    questions.about_training()

    user = Person(questions)

    print(user.generate_report())
    print(user.generate_suggestion())
    print(user.generate_tips_bulk())
    print(user.generate_cut_tips())


if __name__ == "__main__":
    main()
