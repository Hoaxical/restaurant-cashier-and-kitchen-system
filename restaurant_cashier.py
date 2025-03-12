# Create parent class Menu

class Menu:
    def __init__(self, name):
        self._name = name
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    

# Using Multilevel and Hierarchical Inheritance

#Dishes is a sub class/Child class of Menu

class Dishes(Menu):
    def __init__(self, name, price, preparation_time, ready_availability = 0):
        super().__init__(name)
        self._price = price
        self._preparation_time = preparation_time
        self._ready_availability = ready_availability
    
    @property
    def price(self):
        return self._price
    
    @price.setter
    def price(self, value):
        self._price = value

    @property
    def preparation_time(self):
        return self._preparation_time
    
    @property
    def ready_availability(self):
        return self.ready_availability()
    
    @ready_availability.setter
    def ready_availability(self, value):
        self._ready_availability = value
    
# Specials is a sub class of sub class Dishes
class Specials(Dishes):
    def __init__(self, name, price, preparation_time, ready_availability):
        super().__init__(name, price, preparation_time, ready_availability)

# Biryani, Seven Curry are sub classes of Specials
class Biryani(Specials):
    def __init__(self, name, price = 150, preparation_time = 8, ready_availability = 0):
        super().__init__("Biryani", preparation_time, ready_availability)

class SevenCurry(Specials):
    def __init__(self, name, price = 129, preparation_time = 15, ready_availability = 0):
        super().__init__("Seven Curry", price, preparation_time, ready_availability)

# Pizza is a sub class of Dishes
class Pizza(Dishes):
    def __init__(self, name, price, preparation_time = 10, ready_availability = 0):
        super().__init__(name, price, preparation_time, ready_availability)

#Mozzarella Pizza, Classic Pizza is a sub class of Pizza
class MozzarellaPizza(Pizza):
    def __init__(self, name, price = 249, preparation_time = 10, ready_availability = 0):
        super().__init__("Mozzarella Pizza", price, preparation_time, ready_availability)

class ClassicPizza(Pizza):
    def __init__(self, name, price = 209, preparation_time = 10, ready_availability = 0):
        super().__init__("Classic Pizza", price, preparation_time, ready_availability)

# Burger is a sub class of Dishes
class Burger(Dishes):
    def __init__(self, name, price, preparation_time = 3, ready_availability = 0):
        super().__init__(name, price, preparation_time, ready_availability)

# VegBurger, Chicken Burger, BeefBurger are sub classes of Burger
class VegBurger(Burger):
    def __init__(self, name = "Veggie Burger", price = 79, preparation_time=3, ready_availability = 0):
        super().__init__("Veggie Burger", price, preparation_time, ready_availability)

class ChickenBurger(Burger):
    def __init__(self, name, price = 99, preparation_time=3, ready_availability = 0):
        super().__init__("Chicken Burger", price, preparation_time, ready_availability)

class BeefBurger(Burger):
    def __init__(self, name, price = 109, preparation_time=3, ready_availability = 0):
        super().__init__("Beef Burger", price, preparation_time, ready_availability)

# FriedRice, FriedNoodles are sub classes of Dishes
class FriedRice(Dishes):
    def __init__(self, name, price = 150, preparation_time = 8, ready_availability = 0):
        super().__init__("Fried Rice", price, preparation_time, ready_availability)

class FriedNoodles(Dishes):
    def __init__(self, name, price = 125, preparation_time = 5, ready_availability = 0):
        super().__init__("Fried Noodles", price, preparation_time, ready_availability)








#temporary ///I am testing how I can add user prompts and how each attribute will work. 
class Cashier:
    def __init__(self, name ="Cashier"):
        self._name = name
    
    def CreateOrder(self):

        #For user prompt instead of burger1 = VegBurger(), I could make the user prompt the exact name of the dish's name. That would prompt the variable at class.

        burger1 = VegBurger() #I fixed the code. I need to assign the names at def__init__ when I declare class, not at super().__init__

        print (f"{burger1.name}: Rs {burger1.price}")







def main():
    cashier = Cashier()
    cashier.CreateOrder()


main()
        