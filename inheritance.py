# super class = parent class
# why parent? avoid redundancies
# parent = inheritance
# inherit by placing parent inside child parenthesis
# also - def __init__ with same parameters as parent
# underneath super().__init__(parameters above without self)

class Dog:
    def __init__(self, name, age, friendliness):
        self.name = name
        self.age = age
        self.friendliness = friendliness
    
    def likes_walks(self):
        return True
    
class Pug(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)


class Mutt(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

class Pit(Dog):
    def __init__(self, name, age, friendliness):
        super().__init__(name, age, friendliness)

juicy = Pug('Juicy', 12, True)
print(juicy.name, juicy.age, juicy.friendliness)
print(juicy.likes_walks())