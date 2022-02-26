#Let's build a calculator!

number_1 = input("Number 1 :\n")
operation = input("Operation(+, -, *, /) :\n")
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
else:
  print("Wrong input!")
