import json

class Employee:
    def __init__(self, name, dob, height, city, state):
        self.name = name
        self.dob = dob
        self.height = height
        self.city = city
        self.state = state

with open(r"C:\Users\ahmed\OneDrive\Desktop\NEW\Assignment-6\employee.json") as file:
     json_object = json.load(file)


emp = input("Enter the employee id (i.e '1', '2', '3', '4', '5'): ")
obj = Employee (json_object[emp]['name'], json_object[emp]['DOB'],json_object[emp]['height'],json_object[emp]['city'],json_object[emp]['state'])


print(json_object[emp]) 
print(obj.name) 
print(obj.dob) 
print(obj.height)
print(obj.city)
print(obj.state)



