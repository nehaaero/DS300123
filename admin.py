import json

class Admin:

    def __init__(self):
        self.data={}
        self.food_id=0
        try:
            with open ("food.json", "r") as file:
                self.data = json.load(file)
                self.food_id = max(self.data.keys()) + 1
        except:
            pass

    def add_food_item(self):
        name = input("enter food item name: ")
        quantity = input ("enter food item quantity: ")
        price = float(input("enter food item price in float: "))
        discount = float(input("enter food item discount in float: "))
        stock = int(input("enter food item stock in int: "))

        self.food_id+=1
        self.data[self.food_id] = {
            "name": name,
            "quantity": quantity,
            "price": price,
            "discount": discount,
            "stock": stock
        }
        with open ("food.json", "w") as file:
            json.dump(self.data,file)
        print("food item added successfully")

    def edit_food_item(self):
        food_id = int(input("enter food item id in int: "))
        if food_id in self.data:
            name = input ("enter food item name: ")
            quantity = input("enter food item quantity: ")
            price = float(input("Enter food item price in float: "))
            discount = float(input("Enter food item discount in float: "))
            stock = int(input("Enter food item stock in int: "))

            self.data[food_id] = {
                "name": name,
                "quantity": quantity,
                "price": price,
                "discount": discount,
                "stock": stock
            }
            with open("menu.json", "w") as file:
                json.dump(self.data, file)
            print("*** Food item updated successfully ***")
        else:
            print("Food item not found!")

    def view_food_items(self):
        print("Food ID\tName\t\tQuantity\t\tPrice\t\tDiscount\t\tStock")
        for food_id, food_item in self.data.items():
            print(f"{food_id}\t\t{food_item['name']}\t\t{food_item['quantity']}\t\t{food_item['price']}\t\t{food_item['discount']}\t\t{food_item['stock']}")

    def remove_food_item(self):
        food_id = int(input("Enter food item id in int: "))
        if food_id in self.data:
            del self.data[food_id]
            with open("menu.json", "w") as file:
                json.dump(self.data, file)
            print("Food item removed successfully!")
        else:
            print("Food item not found!")

admin = Admin()

while True:
    print("1. Add food item")
    print("2. Edit food item")
    print("3. View food items")
    print("4. Remove food item")
    print("5. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        admin.add_food_item()
    elif choice == 2:
        admin.edit_food_item()
    elif choice == 3:
        admin.view_food_items()
    elif choice == 4:
        admin.remove_food_item()
    elif choice == 5:
        break
    else:
        print("Invalid choice! Try again.")



def signUp():
    name = input("Enter a name : ")
    mobile = input("Enter a mobile# : ")
    email = input("Enter email : ")
    pwd = input("Creat a Password : ")

    with open('User_RegData.csv') as fr:
        data = fr.read()
        fileHasData = False
        if len(data) > 0:
            fileHasData = True
    with open('User_RegData.csv', 'a', newline='') as fw:
        w = csv.writer(fw)
        if not fileHasData:
            columns = ['UserID', 'Name', 'Mobile_Number', 'Email', 'Password']
            w.writerow(columns)
        w.writerow(['101', name, mobile, email, pwd])

signUp()
