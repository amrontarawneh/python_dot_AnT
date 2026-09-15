num1 = float(input("Enter number 1: "))
num2 = float(input("Enter number 2: "))
num3 = float(input("Enter number 3: "))
num4 = float(input("Enter number 4: "))
num5 = float(input("Enter number 5: "))

total = num1 + num2 + num3 + num4 + num5
average = total / 5
largest = max(num1, num2, num3, num4, num5)

print("Total:", total)
print("Average:", average)
print("Largest:", largest)