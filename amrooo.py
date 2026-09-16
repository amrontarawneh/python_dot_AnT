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
