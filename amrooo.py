import math


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
text = "Hello"

print(hash(text))

def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Error in calculation")


def test():
    a = float(input("Enter first argument: "))
    b = float(input("Enter second argument: "))

    print(f"Result of a + b: {add(a, b)}")
    print(f"Result of a - b: {sub(a, b)}")
    print(f"Result of a * b: {mul(a, b)}")
    print(f"Result of a / b: {div(a, b)}")


#if __name__ == "__main__":
  #  test()
 #   import my math
#a= float(input("Enter a: "))
#b= float(input("Enter b: "))
#print(my_math.add(a, b))
# import tkinter as tk

# root = tk.Tk()
# root.title("Loop Demonstration")

# print("Step 1: This prints instantly during setup.")

# root.mainloop()

# print("Step 2: This WILL NOT print until you close the GUI window!")

# import tkinter as tk

# root = tk.Tk()
# root.geometry("500x400")

# 1. Upper and Lower Container Frames
# upper_frame = tk.Frame(root, bg="lightblue")
# upper_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# lower_frame = tk.Frame(root, bg="lightgray")
# lower_frame.pack(side=tk.TOP, fill=tk.BOTH, expand=True)

# 2. Text widget in Upper Frame
# text_widget = tk.Text(upper_frame, height=5)
# text_widget.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)

# 3. Three side-by-side frames inside Lower Frame
# sub_left = tk.Frame(lower_frame, bg="white")
# sub_left.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

# sub_mid = tk.Frame(lower_frame, bg="white")
# sub_mid.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

# sub_right = tk.Frame(lower_frame, bg="white")
# sub_right.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=5, pady=5)

# 4. Put different widgets into each of the 3 lower areas
# tk.Button(sub_left, text="Widget 1").pack(padx=10, pady=10)

# tk.Entry(sub_mid).pack(padx=10, pady=10)

# tk.Label(sub_right, text="Widget 3").pack(padx=10, pady=10)

# root.mainloop()
# import tkinter as tk

# def on_button_click():
    # print("Button was clicked!")

# def on_enter_key(event):
    # print("Enter key was pressed on the keyboard!")

# root = tk.Tk()
# root.title("Handling Events Example")
# root.geometry("300x200")

# 1. Using the command parameter for a button click
# btn = tk.Button(
    # root,
    # text="Click Me",
#  command=on_button_click

# btn.pack(pady=20)

# 2. Using bind() to listen for keyboard events on the root window
# The event is raised when the <Return> key is pressed.
# root.bind("<Return>", on_enter_key)

# root.mainloop()

# import tkinter as tk

# def on_button_click_granular(event):
    # Because we used .bind(), we can inspect the event object
    # print(f"Clicked at coordinates: X={event.x}, Y={event.y}")

# root = tk.Tk()
# root.geometry("300x200")

# btn = tk.Button(root, text="Granular Click Me")
# btn.pack(pady=50)

# Bind the left mouse click event to the button
# btn.bind("<Button-1>", on_button_click_granular)

# root.mainloop()
# import tkinter as tk

# def on_button_click_granular1(event):
    # Because we used .bind(), we can inspect the event object!
    # print(f"Clicked (1) at coordinates: X={event.x}, Y={event.y}")

# def on_button_click_granular2(event):
    # Because we used .bind(), we can inspect the event object!
    # print(f"Clicked (2) at coordinates: X={event.x}, Y={event.y}")

# root = tk.Tk()
# root.geometry("300x200")
# root.title("Testing Mouse Clicks")

# btn = tk.Button(root, text="Granular Click Me")
# btn.pack(pady=50)

# Bind the left mouse click event to the button
# btn.bind("<Button-1>", on_button_click_granular1)

# Bind the right mouse click event to the button
# btn.bind("<Button-3>", on_button_click_granular2)

# root.mainloop()
# import tkinter as tk

# root = tk.Tk()
# root.title("Tkinter Variables Example")
# root.geometry("300x200")

# Create a StringVar wrapper
# name_var = tk.StringVar()

# Entry box linked to the StringVar
# entry = tk.Entry(
    # root,
    # textvariable=name_var,
    # font=("Arial", 11)

# entry.pack(pady=20)

# Label also linked to the exact same StringVar
# Instant mirroring
# label = tk.Label(
    # root,
    # textvariable=name_var,
    # font=("Arial", 12, "bold")
# )
# label.pack(pady=10)

# root.mainloop()
# import tkinter as tk

# def get_input():
    # user_text = entry.get()  # Retrieve text from entry box
    # print(f"User entered: {user_text}")
    
    # entry.delete(0, tk.END)  # Clear the Entry box

# root = tk.Tk()
# root.title("User Input Example")
# root.geometry("300x200")

# entry = tk.Entry(root, width=25, font=("Arial", 22))
# entry.pack(pady=20)

# submit_btn = tk.Button(
    # root,
    # text="Submit Input",
    # command=get_input
# )
# submit_btn.pack(pady=5)

# root.mainloop()
# import tkinter as tk

# def get_input():
    # user_text = entry.get()  # Retrieve text from entry box
    # print(f"User entered: {user_text}")
    
    # entry.delete(0, tk.END)  # Clear the Entry box

# root = tk.Tk()
# root.title("User Input Example")
# root.geometry("300x200")

# entry = tk.Entry(root, width=25, font=("Arial", 22))
# entry.pack(pady=20)

# submit_btn = tk.Button(
    # root,
    # text="Submit Input",
    # command=get_input
# )
# submit_btn.pack(pady=5)

# root.mainloop()
# import tkinter as tk
# from tkinter import messagebox

# def trigger_alert():
    # Show a warning popup
    # messagebox.showwarning(
        # "Warning",
        # "Disk space is running low!"
    # )

# def confirm_action():
    # Ask a yes/no question
    # answer = messagebox.askyesno(
        # "Confirmation",
        # "Do you really want to exit?"
    # )

    # if answer:
        # root.quit()

# root = tk.Tk()
# root.title("Dialogs Example")
# root.geometry("300x200")

# warn_btn = tk.Button(
    # root,
    # text="Show Warning",
    # command=trigger_alert
# )
# warn_btn.pack(pady=15)

# exit_btn = tk.Button(
    # root,
    # text="Exit App",
    # command=confirm_action
# )
# exit_btn.pack(pady=5)

# root.mainloop()
# import tkinter as tk


# class MyApplication(tk.Tk):

    # def __init__(self):
        # super().__init__()

        # self.title("OOP Application Structure")
        # self.geometry("300x200")

        # Build UI components
        # self.create_widgets()

    # def create_widgets(self):
        # self.label = tk.Label(
            # self,
            # text="Welcome to Class-based Tkinter!",
            # font=("Arial", 10)
        # )
        # self.label.pack(pady=20)

        # self.btn = tk.Button(
            # self,
            # text="Click Me",
            # command=self.on_click
        # )
        # self.btn.pack(pady=10)

    # def on_click(self):
        # self.label.config(
            # text="Button Clicked via Class Method!"
        # )


# if __name__ == "__main__":
    # app = MyApplication()
    # app.mainloop()
#from flask import Flask, redirect, url_for

#app = Flask(__name__)

#@app.route("/")
#def home():
   # return "Hello! This is the main page <h1>HELLO</h1>"

#@app.route("/<name>")
#def user(name):
    #return f"Hello {name}"

#@app.route("/admin")
#def admin():
  #  return redirect(url_for("home"))

#if __name__ == "__main__":
   # app.run(debug=True)
    #from flask import Flask, render_template, request, redirect, url_for

#app = Flask(__name__)


#@app.route("/feedback", methods=["GET", "POST"])
#def feedback():
   # if request.method == "POST":
        # Extract form field values using the "name" attribute from HTML
       # username = request.form.get("username")
      #  message = request.form.get("message")

        # Process or print data
     #   print(f"Received feedback from {username}: {message}")

        # Redirect to avoid duplicate form submissions on page refresh
    #    return redirect(url_for("feedback_success"))

   # return render_template("feedback_form.html")


#@app.route("/success")
#def feedback_success():
   # return "<h2>Thank you for your feedback!</h2>"


#if __name__ == "__main__":
 #   app.run(debug=True)
import pandas as pd

df = pd.read_csv("ComputerSales.csv")

print("Columns:", df.columns.tolist())
print("Shape:", df.shape)
print(df.head(3))
print(df.info())

print("\nProduct Types & Count:")
print(df["Product Type"].value_counts())

print("\nTotal Profit by Product Type:")
print(df.groupby("Product Type")["Profit"].sum())
import pandas as pd

# Creating a sample dataset of employees
data = {
    'ID': [101, 102, 103, 104, 105, 106],
    'Name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Ethan', 'Fiona'],
    'Salary': [50000, 60000, 55000, 75000, 48000, 82000]
}

# Creating a DataFrame
df = pd.DataFrame(data)

# View the first 2 rows
print("\n--- head(2) ---")
print(df.head(2))

# View the last 2 rows
print("\n--- tail(2) ---")
print(df.tail(2))

# View information about the DataFrame
print("\n--- info() ---")
df.info()

# View summary statistics for numerical columns
print("\n--- describe() ---")
print(df.describe())
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read the CSV file
df = pd.read_csv('ComputerSales.csv')

# Example 1: Total Sales and Total Profit by Product Type
product_summary = df.groupby('Product Type')[['Sale Price', 'Profit']].sum()

print(product_summary)


# Example 2: Scatter plot of Age vs Sale Price by Product Type
plt.figure(figsize=(6, 5))

for p_type in df['Product Type'].unique():
    subset = df[df['Product Type'] == p_type]
    
    plt.scatter(
        subset['Age'],
        subset['Sale Price'],
        label=p_type
    )

plt.title('Age vs. Sale Price by Product Type')
plt.xlabel('Customer Age')
plt.ylabel('Sale Price ($)')

plt.legend()
plt.grid(True, linestyle='--', alpha=0.5)

plt.savefig('plot2.png')
plt.show()
plt.close()
import pandas as pd

# --- 1. Load the Data ---
df = pd.read_csv("sleep_vs_grades.csv")

print("--- Step 1: Data Loaded ---")
print(df.head())


# --- 2. Split Dataset ---
from sklearn.model_selection import train_test_split

X = df[["Sleep_Hours"]]
y = df["Exam_Grade"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

print("\n--- Step 2: Dataset Split ---")
print(f"Training samples: {X_train.shape[0]}")
print(f"Testing samples: {X_test.shape[0]}")


# --- 3. Initialize and Train the Model ---
from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("\n--- Step 3: Model Trained ---")
print(f"Learned Weight (Slope): {model.coef_[0]:.2f}")
print(f"Learned Bias (Intercept): {model.intercept_:.2f}")


# --- 4. Make Predictions on Test Data ---
y_pred = model.predict(X_test)

print("\n--- Step 4: Predictions Made ---")
print(y_pred)


# --- 5. Evaluate Model Performance ---
from sklearn.metrics import mean_squared_error, r2_score

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("\n--- Step 5: Evaluation ---")
print(f"Mean Squared Error (MSE): {mse:.2f}")
print(f"R-squared (R2) Score: {r2:.2f}")