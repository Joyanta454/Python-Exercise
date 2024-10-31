class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    def displayMehthod(self):
        print(f"ID: {self.id} \nName: {self.name}")

e1 = Employee(101, 'Joy')

e1.displayMehthod()



# Deleting the property of object
del e1.id
# Deleting the object itself
try:
    print(e1.id)
except NameError:
    print("e1.id is not defined")

del e1
try:
    e1.display()  # it will gives error after deleting e1
except NameError:
    print("e1 is not defined")