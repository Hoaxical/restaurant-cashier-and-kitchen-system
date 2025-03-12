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
        return self._ready_availability  # Fixed reference
    
    @ready_availability.setter
    def ready_availability(self, value):
        self._ready_availability = value
    

class Specials(Dishes):
    def __init__(self, name, price, preparation_time, ready_availability=0):
        super().__init__(name, price, preparation_time, ready_availability)


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



class Cashier:
    def __init__(self, name="Cashier"):
        self._name = name
    
    def CreateOrder(self, alphabet_array, current_alphabet_index, current_number):


        checkout = False
        
        menu_dishes = {
            "Biryani": Biryani,
            "Seven Curry": SevenCurry,
            "Mozzarella Pizza": MozzarellaPizza,
            "Classic Pizza": ClassicPizza,
            "Veggie Burger": VegBurger,
            "Chicken Burger": ChickenBurger,
            "Beef Burger": BeefBurger,
            "Fried Rice": FriedRice,
            "Fried Noodles": FriedNoodles,
        }

        print("You may choose the following:")
        for dish_name, dish_class in menu_dishes.items():
            dish_instance = dish_class()
            print(f"{dish_instance.name} => Rs {dish_instance.price}")

        order = []
        _vat, total = 1.15, 0

        while not checkout:
            food_input = input("Enter menu item to order (or type 'exit' to finish): ").strip()

            if food_input.lower() == "exit":
                checkout = True
                continue

            if food_input in menu_dishes:
                dish = menu_dishes[food_input]()
                order.append(dish)
                print(f"Added: {dish.name} - Rs {dish.price}")

                total += dish.price

            else:
                print("Invalid selection. Please try again.")


        current_number += 1


        if current_number >= 9999:
            current_number = 1
            current_alphabet_index += 1
        
        # Fixed a bug where the current_alphabet_index would exceed length of alphabet_array
        if current_alphabet_index > (len(alphabet_array)-1):
            current_alphabet_index = 0
        
        order_no = f"{alphabet_array[current_alphabet_index]}{str(current_number).zfill(4)}"

        print("\nYour Order Summary:")

        with open("invoice.txt","w") as invoice_file:

            for item in order:
                print(f"- {item.name}: Rs {item.price}")
                invoice_file.write(f"{item.name}: Rs {item.price}\n")
            
            total = round(total * _vat, 2)
            print(f"VAT : {_vat}")
            print(f"Total (VAT inc.) : Rs {total}")
            

            invoice_file.write(f"VAT : Rs {_vat} | Total (VAT inc.) : Rs {total}\n")

            print(f"Thank you for ordering! ORDER #{(order_no)}")
            invoice_file.write(f"Thank you for ordering! ORDER #{(order_no)}\n")



alphabet_text = "a b c d e f g h i j k l m n o p q r s t u v w x y z"
alphabet_array = alphabet_text.upper().split()


cashier = Cashier()

cashier.CreateOrder(alphabet_array, current_alphabet_index = 25, current_number = 9999)