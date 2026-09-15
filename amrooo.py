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
