class Report:
    def __init__(self, easy_cal, normal_cal, extreme_cal):
        self.easy_cal = easy_cal
        self.normal_cal = normal_cal
        self.extreme_cal = extreme_cal
        self.report = ""
        self.bulk = ""
        self.proposal = ""
        self.cut = ""

    def generate(self):
        print("----------------------------")
        print("----------------------------")
        self.report += "Results: \n"
        self.report += "-------- \n"
        self.report += f"This is the calories for easy: {self.easy_cal}cal/day (0,25kg/week). \n"
        self.report += f"This is the calories for normal: {self.normal_cal}cal/day (0,5kg/week). \n"
        self.report += f"This is the calories for extreme: {self.extreme_cal}cal/day (1kg/week)."
        return self.report

    def suggestion(self):
        print("----------------------------")
        print("----------------------------")
        self.proposal += "Information: \n"
        self.proposal += "------------ \n"
        self.proposal += "If you want to maintain your weight and " \
                         "you don't train anything write maintain at the 3rd paragraph. \n"
        self.proposal += "If you want to gain weight but you don't train anything " \
                         "pick the Easy option. \n"
        self.proposal += "If you want to lose weight but you don't train anything " \
                         "pick the Easy option."
        return self.proposal

    def tips_bulk(self):
        print("----------------------------")
        print("----------------------------")
        self.bulk += "Underneath you'll find tips about bulking (weight gaining)" \
                     " if you do sports or go to the gym: \n"
        self.bulk += "-------- \n"
        self.bulk += "If you want to lean bulk take the Normal option. \n"
        self.bulk += "If you want to cheat bulk take the Extreme option."
        return self.bulk

    def cut_tips(self):
        print("----------------------------")
        print("----------------------------")
        self.cut += "Underneath you'll find tips about cutting (weight losing)" \
                    " if you do sports or go to the gym: \n"
        self.cut += "-------- \n"
        self.cut += "If you want to cut take the Easy option. \n"
        self.cut += "If you want to intense cut take the Normal option."
        return self.cut
