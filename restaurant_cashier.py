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

    
    # Cashier's method is to process client orders and generate invoice.
    # After user inputs menu, order details and invoice number is generated and written to
    # file named 'invoice.txt'. The file is overwritten everytime a new order is created.
    

    def ProcessOrder(self, alphabet_array, current_alphabet_index, current_number): #Passing variables

        checkout = False # Initialise checkout to False
        

        # When the user enters what dish he wants from the menu, the user input will
        # be compared against a dictionary called 'menu_dishes'. If the input matches the items
        # in dictionary, the program will create an Instance and store it's necessary data in a list.

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

        # I initialized _vat to 1.15 to ease Total (Vat Inc.) calculation later on. Assume
        # VAT is 15%.

        _vat, total = 1.15, 0 #initialise value added tax and total

        #while checkout is false, user is free to input more menu dishes

        while not checkout:
            food_input = input("Enter menu item to order (or type 'checkout' to finish): ").strip().lower()
            

            if food_input.lower() == "checkout": #once user enters "exit",
                checkout = True #checkout is initiated to true and no more menu dishes can be entered
                continue

            if food_input in menu_dishes: #while checkout is still false, user can keep entering
                try:
                     
                    dish = menu_dishes[food_input]()
                    
                    # THE PROGRAM SHOULD NOT ALLOW NEGATIVE OR Number '0' FOR QUANTITY.
                    
                    try:
                        food_quantity = int(input(f"Enter quantity of {menu_dishes[food_input]().name}: "))
                    
                        if food_quantity <= 0:  # Reject negative or zero quantity
                           
                           print("Cannot accept negative or zero quantity.")
                           
                           continue
                
                        pass  # if the input is valid, exit loop

                    except ValueError: #TO CHECK IF THIS ERROR HANDLING IS GOOD OR NOT --- PASSED
                            
                        print("Cannot accept negative quantity value.")

                    order.append((dish, food_quantity))
                    qty_total = dish.price * food_quantity
                    print(f"Added: {food_quantity}x {dish.name} - Rs {qty_total}")

                    total += qty_total 
                    print(f"Sub-Total: Rs {total}")
                
                except ValueError:
                    print("Invalid selection. Please try again.")

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

        #I used built-in library to generate current date and time to add to the invoice.txt
        from datetime import datetime
        current_time = datetime.now()

        formatted_datetime = current_time.strftime("%Y-%m-%d %H:%M:%S")

        with open("invoice.txt","w") as invoice_file: #writes order details to new file / overwrites existing file

            for item, quantity in order: 
                print(f" {quantity}x {item.name}: Rs {item.price * quantity}")
                invoice_file.write(f"{quantity}x {item.name}: Rs {item.price * quantity}\n")
            
            total = round(total * _vat, 2)
            print(f"VAT : 15%")
            print(f"Total (VAT inc.) : Rs {total}")
            

            invoice_file.write(f"VAT : 15% | Total (VAT inc.) : Rs {total}\n\n")

            print(f"Ordered at {formatted_datetime}")
            invoice_file.write(f"Ordered at {formatted_datetime}\n\n")
            
            print(f"Thank you for ordering! ORDER #{(order_no)}")
            invoice_file.write(f"Thank you for ordering! ORDER #{(order_no)}\n")
    
        return current_alphabet_index, current_number

# ------------------ main program starts here -------------------------

#----------------------------------------------------------------------

# For Order Number generation, I wish to use alphabet before 4 digits.
# Once the 4 digits reach 9999, the alphabet cycles to the next.
# For example, 'A9999', becomes 'B0001'.

# Initialise alphabet array
alphabet_text = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet_array = alphabet_text.upper().split()

current_alphabet_index = 0
current_number = 0

cashier = Cashier()  # Create an instance of the Cashier class

while True:  # Keep looping until the user stops the cashier
    cashier_on_off = int(input("Press 1 to start Cashier | Press 2 to stop Cashier: "))
    
    if cashier_on_off == 2:  # Stop the cashier if user inputs 2
        print("Cashier stopped.")
        break

    elif cashier_on_off == 1:  # Start the cashier if user inputs 1

        #fixed issue where current_lphabet_index and current_number would reset
        #after cuser re-inputs 1 -- returned values from ProcessOrder() are now
        #assigned to the respective variables, that is passed back onto the method.

        current_alphabet_index, current_number = cashier.ProcessOrder(
            alphabet_array, current_alphabet_index, current_number
        )
    else:
        print("Invalid input. Please press 1 to start or 2 to stop.")





# FOR KITCHEN SYSTEM
# SEND ORDER DETAILS TO KITCHEN

# CREATE PARENT CLASS KITCHEN
# UPDATE READY_AVAILABILITY VALUES USING SETTERS
# #AND THEN USE PREPARATION_TIME AND AVAILABILITY AS WEIGHTAGE TO SET A DYNAMIC QUEUE FOR THE KITCHEN SYSTEM TO ORDER PREP 
