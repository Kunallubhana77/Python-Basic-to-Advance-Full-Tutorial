# Create a Restaurant class that stores menu items in a dictionary and prints the bill.

class Restaurant:
    def __init__(self):
        self.menu = {
            "Burger": 5.99,
            "Pizza": 8.99,
            "Pasta": 7.50,
            "Salad": 4.50,
            "Soda": 1.99
        }

    def show_menu(self):
        print("--- Menu ---")
        for item, price in self.menu.items():
            print(f"{item}: ${price}")

    def print_bill(self, orders):
        total = 0
        print("\n--- Bill ---")
        for item in orders:
            if item in self.menu:
                price = self.menu[item]
                total += price
                print(f"{item}: ${price}")
            else:
                print(f"{item} is not on the menu.")
        print("----------------")
        print(f"Total: ${total:.2f}")

# Testing the class
my_restaurant = Restaurant()
my_restaurant.show_menu()

customer_order = ["Burger", "Soda", "Pizza", "Ice Cream"]
my_restaurant.print_bill(customer_order)
