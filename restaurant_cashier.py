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
class Dishes(Menu):
    def __init__(self, name, price, preparation_time, ready_availability=0):
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
        return self._ready_availability
    
    @ready_availability.setter
    def ready_availability(self, value):
        self._ready_availability = value
    
# Creating sub class of Parent Class Dishes
class Specials(Dishes):
    def __init__(self, name, price, preparation_time, ready_availability=0):
        super().__init__(name, price, preparation_time, ready_availability)

# Sub class of sub class Specials
class Biryani(Specials):
    def __init__(self):
        super().__init__("Biryani", 150, 8, 0)


class SevenCurry(Specials):
    def __init__(self):
        super().__init__("Seven Curry", 129, 15, 0)


class Pizza(Dishes):
    def __init__(self, name, price, preparation_time=10, ready_availability=0):
        super().__init__(name, price, preparation_time, ready_availability)


class MozzarellaPizza(Pizza):
    def __init__(self):
        super().__init__("Mozzarella Pizza", 249, 10, 0)


class ClassicPizza(Pizza):
    def __init__(self):
        super().__init__("Classic Pizza", 209, 10, 0)

#Sub class Burger of Parent class Dishes
class Burger(Dishes):
    def __init__(self, name, price, preparation_time=3, ready_availability=0):
        super().__init__(name, price, preparation_time, ready_availability)


class VegBurger(Burger):
    def __init__(self):
        super().__init__("Veggie Burger", 79, 3, 0)


class ChickenBurger(Burger):
    def __init__(self):
        super().__init__("Chicken Burger", 99, 3, 0)


class BeefBurger(Burger):
    def __init__(self):
        super().__init__("Beef Burger", 109, 3, 0)


class FriedRice(Dishes):
    def __init__(self):
        super().__init__("Fried Rice", 150, 8, 0)


class FriedNoodles(Dishes):
    def __init__(self):
        super().__init__("Fried Noodles", 125, 5, 0)


#Creating another Parent Class Cashier
class Cashier:
    def __init__(self, name="Cashier"):
        self._name = name

    
    #Cashier's method is to create orders and send them to Kitchen system

    def CreateOrder(self, alphabet_array, current_alphabet_index, current_number): #Passing variables


        checkout = False # Initialise checkout to False
        
        #create a 'menu_dishes' dictionary

        menu_dishes = {
            "biryani": Biryani,
            "seven curry": SevenCurry,
            "mozzarella pizza": MozzarellaPizza,
            "classic pizza": ClassicPizza,
            "veggie burger": VegBurger,
            "chicken burger": ChickenBurger,
            "beef burger": BeefBurger,
            "fried rice": FriedRice,
            "fried noodles": FriedNoodles,
        }

        #Prompt user to input menu
        print("You may choose the following:")
        for dish_name, dish_class in menu_dishes.items(): #display the available menu
            dish_instance = dish_class()
            print(f"{dish_instance.name} => Rs {dish_instance.price}")

        order = [] # list called order
        _vat, total = 1.15, 0 #initialise value added tax and total

        #while checkout is false, user is free to input more menu dishes

        while not checkout:
            food_input = input("Enter menu item to order (or type 'exit' to finish): ").strip().lower()

            if food_input.lower() == "exit": #once user enters "exit",
                checkout = True #checkout is initiated to true and no more menu dishes can be entered
                continue

            if food_input in menu_dishes: #while checkout is still false, user can keep entering
                dish = menu_dishes[food_input]()
                order.append(dish)
                print(f"Added: {dish.name} - Rs {dish.price}")

                total += dish.price #update total

            else:
                print("Invalid selection. Please try again.")


        current_number += 1 #current_number is incremented


        if current_number >= 9999:
            current_number = 1           #current number is reset back to 1 when current_number reaches 9999
            current_alphabet_index += 1  #while current_alphabet_index also moves from alphabet 'A' to 'B', the cycle keeps going
        
        # ---Fixed a bug where the current_alphabet_index would exceed length of alphabet_array---
        if current_alphabet_index > (len(alphabet_array)-1):
            current_alphabet_index = 0
        
        order_no = f"{alphabet_array[current_alphabet_index]}{str(current_number).zfill(4)}"

        print("\nYour Order Summary:")

        with open("invoice.txt","w") as invoice_file: #writes order details to new file / overwrites existing file

            for item in order:
                print(f"- {item.name}: Rs {item.price}")
                invoice_file.write(f"{item.name}: Rs {item.price}\n")
            
            total = round(total * _vat, 2)
            print(f"VAT : {_vat}")
            print(f"Total (VAT inc.) : Rs {total}")
            

            invoice_file.write(f"VAT : Rs {_vat} | Total (VAT inc.) : Rs {total}\n")

            print(f"Thank you for ordering! ORDER #{(order_no)}")
            invoice_file.write(f"Thank you for ordering! ORDER #{(order_no)}\n")


#main program

#initialising alphabet array

alphabet_text = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet_array = alphabet_text.upper().split()


cashier = Cashier() #creating instance

 #passing variables to cashier's method
cashier.CreateOrder(alphabet_array, current_alphabet_index = 0, current_number = 0)