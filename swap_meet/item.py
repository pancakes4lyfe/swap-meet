from datetime import datetime
today = datetime.today()

class Item():
    def __init__(self, category = None, condition = 0, year = 0):
        if category == None:
            category = ""
        self.category = category
        self.condition = condition
        self.year = year
        self.age = today.year - year

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition >= 5:
            condition_description = "Perfect!"
        elif self.condition >= 4:
            condition_description = "Excellent"
        elif self.condition >= 3:
            condition_description = "Good"
        elif self.condition >= 2:
            condition_description = "Fair"
        elif self.condition == 1:
            condition_description = "Poor"
        else:
            condition_description = "Terrible" 
        return condition_description