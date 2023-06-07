class People:
    def __init__(self, amount, education, happiness, labour, soldiers):
        self.amount = amount
        self.education = education
        self.happiness = happiness
        self.labour = labour
        self.soldiers = soldiers

    def update_amount(self, new_amount):
        self.amount = new_amount

    def update_education(self, new_education):
        self.education = new_education

    def update_happiness(self, new_happiness):
        self.happiness = new_happiness

    def update_labour_ready(self, new_labour):
        self.labour = new_labour

    def update_soldiers(self, new_soldiers):
        self.soldiers = new_soldiers
