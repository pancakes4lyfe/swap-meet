from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, condition = 0):
        self.category = "Clothing"
        self.condition = condition
        #super().__init__("Clothing", condition)
        self.description = self.condition_description()
    
    def __str__(self):
        return "The finest clothing you could wear."