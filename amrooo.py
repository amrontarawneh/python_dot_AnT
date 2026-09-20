S = "Hello there!"

print(S)

print(S[0:6])      

print(S[7])        

print(S[-1])       

print(S[-2])       

print(S[4:])       

print(S[-5:])      
S= ['apple', 'orange', 'peach']
type(S)
print(S[0])
print(S[0:2])
print(S[-1])
print(S[0:-2])
print(S[-2])
print(S[-3:0])
print ("apple"in S)
print ("aPple"in S)
age =35
print(age)
print(type(age))
print(f"I am {age} years old")
print("happy".upper())
print(S[0].upper())
for i in range(1,10):
    print(i)
    print("OK ... done!")
choice = ""

#while choice != "exit":
  #  choice = input("Type 'greet' to say hi or 'exit' to quit: ").lower()

 #   if choice == "greet":
 #       print("Hello there!")

print("Mission accomplished!")
for num in range(1, 6):
    if num == 3:
        continue
    print(num)
    print("Mission accomplished")
    for num in range(1, 6):
        break
    if num == 3:
        continue
    print(num)
    print("Mission accomplished")
sum = 0
for num in range(1, 11):
    sum += num
    print(num)
print("***********")
print(f" sum of numbers range = {sum}")
emails =["a@b.com" , "c@d.com" , "a@b.com"]
unique_emails = set(emails)
print(len(unique_emails))
print(unique_emails)
for i in unique_emails:
    print(i)
    fruits = ['apple', 'banana', 'cherry']
fruits.append("orange")

print(abs(-10))       
print(round(3.6))     
print(pow(2, 3)) 
user_profile ={
     "username":"Amro",
     "level": 5,
     "is_active": True
 }
student_scores ={"Amro": 90, "mones": 5, "teeb": 5} # keys
for name in student_scores.keys():
    print(name)
    student_scores ={"Amro": 90, "mones": 5, "teeb": 5} # values
for name in student_scores.values():
    print(name)
student_scores ={"Amro": 90, "mones": 5, "teeb": 5} # items
for name in student_scores.items():
        print(name) 
student_scores ={"Amro": 90, "mones": 5, "teeb": 5} # items
for items in student_scores.items():
        print(items) 
        student_scores ={"Amro": 90, "mones": 5, "teeb": 5} # items
for k,v in student_scores.items():
        print(f"{k}: {v}") 

goods = ["TV", "Radio", "Washinmachine", "tablelamp"]

g = goods

print(g)

goods[-1] = "hairdryer"

print(goods)
print(g)
def double(x):
    return x * 2
print(double(5))
lambda_double = lambda x: x * 2
print(lambda_double(5))
x="Global"
def my_function():
    y="Local"
   
    print(x)
    print(y)

my_function()
#counter = 0

#def update_counter():
  #  counter = counter + 1

#update_counter()
counter = 0

def update_counter():
    global counter
    counter = counter + 1

update_counter()
print(counter)
#def get_user_age():
   # try:
     #   age = int(input("Enter your age: "))

     #   if age < 0:
      #      raise ValueError("Age cannot be negative.")

     #   if age > 120:
      #      print("Warning: That's a bit high, but we'll allow it!")

   # except ValueError as e:
     #   print(f"Invalid Input: {e}")
  #      return None

   # else:
   #     return age


#user_age = get_user_age()

#if user_age:
    #print(f"Registered age: {user_age}")
   # try:
     #   result = 10 / 0
    #except ZeroDivisionError:
       # print("Error: Division by zero is not allowed.")
class Car:
    # The 'blueprint' for all cars

    def __init__(self, brand, model, color):
        self.brand = brand
        self.model = model
        self.color = color

    def drive(self):
        print(f"The {self.color} {self.model} is now driving!")


# Creating Objects (Instances) from the Car class

car1 = Car("Tesla", "Model S", "Red")
car2 = Car("Ford", "Mustang", "Blue")


# Accessing attributes and methods

print(car1.brand)
# Output: Tesla

car2.drive()
# Output: The Blue Mustang is now driving!
class Student:

    def __init__(self, name, student_id, major="Undeclared"):
        # Initializing attributes
        self.name = name
        self.student_id = student_id
        self.major = major
        self.grades = []

        print(f"Record created for {self.name} (ID: {self.student_id})")


# Creating objects
student1 = Student("Marcus", "S10234", "Computer Science")

student2 = Student("Elena", "S10559")


# Accessing the initialized data
print(f"Student 1 Major: {student1.major}")
print(f"Student 2 Major: {student2.major}")
class BankAccount:

    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance

    # Getter method
    def get_balance(self):
        return f"Balance for {self.owner}: ${self._balance}"

    # Deposit method with validation
    def deposit(self, amount):
        if amount > 0:
            self._balance += amount
            print(f"Deposited ${amount}")
        else:
            print("Error: Deposit amount must be positive.")


# Usage
account = BankAccount("Alice", 1000)

print(account.get_balance())

account.deposit(500)
account.deposit(-50)
class Animal:

    def speak(self):
        # This is a placeholder
        pass


# Child Class 1
class Dog(Animal):

    def speak(self):
        return "Woof! Woof!"


# Child Class 2
class Cat(Animal):

    def speak(self):
        return "Meow!"


# Child Class 3
class Duck(Animal):

    def speak(self):
        return "Quack!"


# Polymorphism in action
animals = [Dog(), Cat(), Duck()]

for animal in animals:
    print(f"{type(animal).__name__} says: {animal.speak()}")
    
class Book:

    def __init__(self, title, author):
        self.title = title
        self.author = author

    def __str__(self):
        return f'"{self.title}" by {self.author}'


my_book = Book("Embedded Logic", "A. Engineer")

print(my_book)
class Component:
    total_produced = 0  # Class Attribute

    def __init__(self, part_type):
        self.part_type = part_type
        Component.total_produced += 1

    @classmethod
    def get_factory_stats(cls):
        return f"Total units manufactured: {cls.total_produced}"


c1 = Component("Resistor")
c2 = Component("Capacitor")
c3 = Component("Inductor")


print(Component.get_factory_stats())
class SignalConverter:

    @staticmethod
    def volts_to_millivolts(v):
        # Pure logic: doesn't need any object or class data
        return v * 1000


print(SignalConverter.volts_to_millivolts(3.3))
class Shelf:
    def __init__(self, items):
        self.items = items

    def __len__(self):
        return len(self.items)

    def __getitem__(self, index):
        return self.items[index]


my_shelf = Shelf(["Multimeter", "Oscilloscope", "Soldering Iron"])

print(len(my_shelf))
print(my_shelf[1])
with open("example.txt", "w") as file:
    file.write("Hello, Python world!\n")
    file.write("This is a practice file.")
    
with open("example.txt", "r") as file:
    content = file.read()

print("--- File Content ---")
print(content)