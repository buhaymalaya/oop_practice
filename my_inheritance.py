# instructions: create a parent class as a base for a breakfast meal
# then, produce child classes inheriting from parent class
# lastly, polymorphise a function from the parent class
# ie) frying egg instead of boiling egg

class Breakfast:
    def __init__(self, eggs, rice, adobo, coconut):
        self.eggs = eggs
        self.rice = rice
        self.adobo = adobo
        self.coconut = coconut


    def boiled(self):
        return "boiled eggs"
    
    def fried_rice(self):
        return "fried rice"
    
    def leftover_adobo(self):
        return "leftover"
    
    def beverage(self):
        return "young"
    
class College(Breakfast):
    def __init__(self, eggs, rice, adobo, coconut):
        super().__init__(eggs, rice, adobo, coconut)

    def rice(self):
        return "microwaved"
    
    def coconut(self):
        return "canned"
    

class Boomerang_Kid(Breakfast):
    def __init__(self, eggs, rice, adobo, coconut):
        super().__init__(eggs, rice, adobo, coconut)

    def adobo(self):
        return "homecooked"


moms = Breakfast(3, "1 cup", "pork", "green")
print(moms.boiled(), moms.beverage(), moms.fried_rice(), moms.leftover_adobo(), moms.rice, moms.adobo, moms.coconut)