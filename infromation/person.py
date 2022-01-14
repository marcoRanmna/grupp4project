from infromation.activity import activity
from infromation.choice import choice
from user_pov.questions import Questions
from user_pov.reporter import Report


class Person:

    def __init__(self, data: Questions):
        self.kg = data.user_weight
        self.cm = data.user_height
        self.my_age = data.user_age
        self.gender = data.user_gender
        self.weight_change = choice(data.user_goal)
        self.training_intensity = activity(data.user_training)
        self.cal = 0

    def generate_report(self):
        easy_cal = self.calculate("easy")
        normal_cal = self.calculate("normal")
        extreme_cal = self.calculate("extreme")

        return Report(easy_cal, normal_cal, extreme_cal).generate()

    def generate_tips_bulk(self):
        easy_cal = self.calculate("easy")
        normal_cal = self.calculate("normal")
        extreme_cal = self.calculate("extreme")

        return Report(easy_cal, normal_cal, extreme_cal).tips_bulk()

    def generate_suggestion(self):
        easy_cal = self.calculate("easy")
        normal_cal = self.calculate("normal")
        extreme_cal = self.calculate("extreme")

        return Report(easy_cal, normal_cal, extreme_cal).suggestion()

    def generate_cut_tips(self):
        easy_cal = self.calculate("easy")
        normal_cal = self.calculate("normal")
        extreme_cal = self.calculate("extreme")

        return Report(easy_cal, normal_cal, extreme_cal).cut_tips()

    def calculate(self, level):
        self.calories()
        self.train()
        self.levels(level)
        return self.cal

    def weight(self):
        return self.kg * 9

    def height(self):
        return self.cm * 7

    def age(self):
        temp_age = self.my_age * 6
        if temp_age >= 15:
            temp_age += 100
        return temp_age

    def calories(self):
        self.cal = self.weight() + self.height() + self.age()

    def train(self):
        if self.training_intensity == "Little to no exercise":
            self.little_to_no_exercise()

        elif self.training_intensity == "Light: exercise":
            self.light_exercise()

        elif self.training_intensity == "Moderate: exercise":
            self.moderate_exercise()

        elif self.training_intensity == "Very Active: Intense exercise":
            self.very_active_exercise()

    def levels(self, level_choice):
        if level_choice == "easy":
            self.easy()

        elif level_choice == "normal":
            self.normal()

        elif level_choice == "extreme":
            self.extreme()

    def little_to_no_exercise(self):
        if self.gender == "female":
            self.cal -= 199

    def light_exercise(self):
        self.cal += 290
        if self.gender == 'male':
            self.cal += 229

        elif self.gender == "female":
            self.cal -= 229

    def moderate_exercise(self):
        self.cal += 439

        if self.gender == "male":
            self.cal += 244
        elif self.gender == "female":
            self.cal -= 244

    def very_active_exercise(self):
        self.cal += 869

        if self.gender == "male":
            self.cal += 286
        elif self.gender == "female":
            self.cal -= 286

    def easy(self):
        if self.weight_change == "Weight gain":
            self.cal += 250
            return self.weight_change
        elif self.weight_change == "Weight loss":
            self.cal -= 250
            return self.weight_change

    def normal(self):
        if self.weight_change == "Weight gain":
            self.cal += 500
            return self.cal
        elif self.weight_change == "Weight loss":
            self.cal -= 500
            return self.cal

    def extreme(self):
        if self.weight_change == "Weight gain":
            self.cal += 1000
            return self.cal
        elif self.weight_change == "Weight loss":
            self.cal -= 1000
            return self.cal
