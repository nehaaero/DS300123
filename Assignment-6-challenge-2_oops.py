class dog:
    def __init__(self, name, age, coat_color):
        self.name = name
        self.age = age
        self.coat_color = coat_color

    def description(self):
        print(f"name of the dog is {self.name}\n  age of the dog is {self.age}\n  coat_color of the dog is {self.coat_color}")

    def get_info(self):
        print(f"name of the dog is {self.name}, age of the dog is {self.age}, 'Coat color of the dog is {self.coat_color}")


class JackRussellTerrier(dog):

    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def get_name(self):
        print("name of the JackRussellTerrier is", self.name)

    def get_age(self):
        print("age of the JackRussellTerrier is", self.age)

    def get_coat(self):
        print("coat_color of the JackRussellTerrier is", self.coat_color)


class Bulldog(dog):
    def __init__(self, name, age, coat_color):
        super().__init__(name, age, coat_color)

    def get_name(self):
        print("name of the Bulldog is", self.name)

    def get_age(self):
        print("age of the Bulldog is", self.age)    

    def get_coat(self):
        print("coat color of the Bulldog is", self.coat_color)                        

obj1 = Bulldog('Oscar', 1, "Brown")
obj2 = JackRussellTerrier('Simba', 2, "Golden")


obj1.description()
obj2.description()

