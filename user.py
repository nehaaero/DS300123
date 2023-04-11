

class User:
    def __init__(self):
        self.full_name = ""
        self.phone_number = ""
        self.email = ""
        self.address = ""
        self.password = ""
        self.logged_in = False
        self.orders = []

    def register(self):
        self.full_name = input("Enter your full name: ")
        self.phone_number = input("Enter your phone number: ")
        self.email = input("Enter your email: ")
        self.address = input("Enter your address: ")
        self.password = input("Enter your password: ")

    def login(self):
        email = input("Enter your email: ")
        password = input("Enter your password: ")
        if email == self.email and password == self.password:
            self.logged_in = True
            print("Login successful!")
        else:
            print("Login failed. Please try again.")

    def place_new_order(self):
        food_list = [
            ("Tandoori Chicken (4 pieces)", 240),
            ("Vegan Burger (1 Piece)", 320),
            ("Truffle Cake (500gm)", 900),
        ]

        print("Select the items you want to order:")
        for i, food in enumerate(food_list):
            print(f"{i + 1}. {food[0]} [INR {food[1]}]")

        selected_items = list(map(int, input("Enter the item numbers separated by space: ").strip().split()))
        selected_food = [food_list[i - 1] for i in selected_items]
        print("You have selected:")
        for food in selected_food:
            print(f"- {food[0]} [INR {food[1]}]")

        confirm = input("Do you want to place the order? (yes/no)").strip().lower()
        if confirm == "yes":
            self.orders.append(selected_food)
            print("Order placed successfully!")

    def order_history(self):
        print("Your order history:")
        for order in self.orders:
            print("-" * 20)
            for food in order:
                print(f"- {food[0]} [INR {food[1]}]")

    def update_profile(self):
        print("Current profile:")
        print(f"Full Name: {self.full_name}")
        print(f"Phone Number: {self.phone_number}")
        print(f"Email: {self.email}")
        print(f"Address: {self.address}")

        update = input("What do you want to update? (full_name/phone_number/email/address/password): ").strip().lower()
        if update == "full_name":
            self.full_name = input("Enter your full name: ")
        elif update == "phone_number":
            self.phone_number = input("Enter your phone number: ")
        elif update == "email":
            self.email = input("Enter your email: ")
        elif update == "address":
            self.address = input("enter your adress")
        elif update == "password":
            self.password = input("Enter your pass:")
        else:
            print("invalid input,, please try again..")        
        print("profile updated sucessfully")


user = User()

# Register the user
user.register()

# Login to the application
user.login()

# Show the options to the user
while user.logged_in:
    print("What do you want to do?")
    print("1. Place New Order")
    print("2. Order History")
    print("3. Update Profile")
    print("4. Logout")

    option = int(input("Enter your choice: "))

    if option == 1:
        user.place_new_order()
    elif option == 2:
        user.order_history()
    elif option == 3:
        user.update_profile()
    elif option == 4:
        user.logged_in = False
        print("You have been logged out.")            