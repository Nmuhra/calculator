#Let's build a calculator!
from cmath import sqrt

number_1 = input("Number 1 :\n")
operation = input("Operation(+, -, *, /), Trig :\n").lower()
number_2 = input("Number 2 :\n")

#different operations:
if operation == "+":
  print(int(number_1) + int(number_2))
if operation == "-":
  print(int(number_1) - int(number_2))
if operation == "*":
  print(int(number_1) * int(number_2))
if operation == "/":
  print(int(number_1) / int(number_2))  
if operation == "trig":
  print(sqrt(number_1**2 + number_2**2))
else:
  print("Wrong input!")
