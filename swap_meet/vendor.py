class Vendor():
    def __init__(self, inventory = None):
        if inventory == None:
            inventory = []
        self.inventory = inventory
    
    def add(self, new_item):
        self.inventory.append(new_item)
        return new_item
    
    def remove(self, item):
        self.inventory.remove(item)
        return item