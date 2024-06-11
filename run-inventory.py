class Product:
    def __init__(self, name, quantity, product_id, price_per_unit):
        self.name = name
        self.quantity = quantity
        self.product_id = product_id
        self.price_per_unit = price_per_unit

    def get_info(self):
        print(f"\nProduct Information"
              f"\n--------------------"
              f"\nName: {self.name}"
              f"\nProduct ID: {self.product_id}"
              f"\nQuantity: {self.quantity}"
              f"\nPrice: R{self.price_per_unit}")

    def get_product_name(self):
        return self.name

    def get_value(self):
        return self.price_per_unit * self.quantity

    def update_quantity(self, new_quantity):
        self.quantity = new_quantity


class Inventory:
    def __init__(self):
        self.products = []
        test_product_1 = Product("Drill", 20, 100, 1199.99)
        test_product_2 = Product("Hammer", 7, 101, 75)
        self.add_product(test_product_1)
        self.add_product(test_product_2)

    def add_product(self, product):
        self.products.append(product)

    def show_product_name(self, product_id):
        for item in self.products:
            if item.product_id == product_id:
                return item.get_product_name()
        return "Error: Product not found"

    def get_product_info(self, product_id):
        for item in self.products:
            if item.product_id == product_id:
                return item.get_info()
        return "Error: Product not found"

    def show_all_products(self):
        if not self.products:
            print("No products in inventory.")
        else:
            for item in self.products:
                item.get_info()

    def total_product_value(self, product_id):
        total_value = 0
        for item in self.products:
            if item.product_id == product_id:
                total_value += item.get_value()
        return total_value

    def update_product_quantity(self, product_id, new_quantity):
        for item in self.products:
            if item.product_id == product_id:
                item.update_quantity(new_quantity)
                break

    def user_input_integer(self, message):
        while True:
            user_input = input(message)
            if user_input.isdigit():
                return int(user_input)
            else:
                print("Invalid input type. Please enter a valid entry.")


def main():
    inventory = Inventory()

    while True:
        print("\nProduct Menu"
              "\n------------------"
              "\n1) Add a product"
              "\n2) Display product info"
              "\n3) Calculate product total"
              "\n4) Update product quantity"
              "\n5) Show all products"
              "\n6) EXIT\n")

        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = int(choice)

            # Add a new product
            if choice == 1:
                name = input("Name of the product: ")
                product_id = inventory.user_input_integer("Product ID: ")
                quantity = inventory.user_input_integer("Quantity: ")
                price_per_unit = round(float(input("Price: R")), 2)
                new_product = Product(name, quantity, product_id, price_per_unit)
                inventory.add_product(new_product)
                print("PRODUCT ADDED SUCCESSFULLY\n")

            # Search for a product using product ID
            elif choice == 2:
                product_id = inventory.user_input_integer("Product ID: ")
                product_info = inventory.get_product_info(product_id)
                print(product_info, "\n")

            # Calculate total inventory value of a specific product
            elif choice == 3:
                product_id = inventory.user_input_integer("Product ID: ")
                product_total = inventory.total_product_value(product_id)
                product_name = inventory.show_product_name(product_id)
                print(f"{product_name} - Total Inventory Value: R{product_total}\n")

            # Update the quantity of a product
            elif choice == 4:
                product_id = inventory.user_input_integer("Product ID: ")
                new_quantity = int(input("Enter new quantity: "))
                inventory.update_product_quantity(product_id, new_quantity)
                product_name = inventory.show_product_name(product_id)
                print("Quantity updated successfully")
                print(f"New quantity of {product_name} is: {new_quantity}\n")

            # Display all products in inventory
            elif choice == 5:
                print(inventory.show_all_products())

            # Exit the program
            elif choice == 6:
                print("Exit Successful")
                break

            else:
                print(f"Invalid Choice: {choice}")

        else:
            print(f"Invalid input: '{choice}'. Please enter a valid integer choice\n")


if __name__ == "__main__":
    main()
