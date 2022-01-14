class Questions:
    def __init__(self):
        self.user_goal = ""
        self.user_training = ""
        self.user_gender = ""
        self.user_weight = ""
        self.user_height = ""
        self.user_age = ""

    def greeting(self):
        print("Welcome to my calorie calculator!")
        print("----------------------------")

    def about_training(self):
        self.goal_check()
        print("----------------------------")
        self.training_check()

    def goal_check(self):
        goal = (input("Would you like to: \nLose weight \nGain weight \nMaintain weight \nYour answer:"))
        for synonym in ["lose", "weight loss", "lose weight", "cut"]:
            if synonym == goal:
                self.user_goal = goal
                return
        for synonym in ["gain", "weight gain", "gain weight", "bulk"]:
            if synonym == goal:
                self.user_goal = goal
                return
        for synonym in ["maintain", "stay the same", "keep", "maintain weight"]:
            if synonym == goal:
                self.user_goal = goal
                return
        print("That was not an option")
        print("----------------------------")
        self.goal_check()

    def training_check(self):
        try:
            training = int(input("How many times per week do you train?:"))
            if isinstance(training, int) and training >= 0:
                self.user_training = training
            else:
                print("That is not a positive number")
                print("----------------------------")
                self.training_check()
        except ValueError:
            print("That is not a number")
            print("----------------------------")
            self.training_check()

    def about_user(self):
        self.gender_check()
        print("----------------------------")
        self.weight_check()
        self.height_check()
        self.age_check()
        print("----------------------------")

    def gender_check(self):
        gender = str(input("Please enter your gender here:"))
        if gender == "male" or gender == "female":
            self.user_gender = gender
            return
        else:
            print("That was not an option")
            print("----------------------------")
            self.gender_check()

    def weight_check(self):
        try:
            weight = int(input("Please enter your weight:"))
            if isinstance(weight, int) and weight > 0:
                self.user_weight = weight
            else:
                print("That is not a positive number")
                print("----------------------------")
                self.weight_check()
        except ValueError:
            print("That is not a number")
            print("----------------------------")
            self.weight_check()

    def height_check(self):
        try:
            height = int(input("Please enter your height:"))
            if isinstance(height, int) and height > 0:
                self.user_height = height
            else:
                print("That is not a positive number")
                print("----------------------------")
                self.height_check()
        except ValueError:
            print("That is not a number")
            print("----------------------------")
            self.height_check()

    def age_check(self):
        try:
            age = int(input("Please enter your age:"))
            if isinstance(age, int) and age > 0:
                self.user_age = age
            else:
                print("That is not a positive number")
                print("----------------------------")
                self.age_check()
        except ValueError:
            print("That is not a number")
            print("----------------------------")
            self.age_check()
