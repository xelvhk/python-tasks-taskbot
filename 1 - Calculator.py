#====== Task 1. Simple calculator =============
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
m = input("Enter the operator:")
if m == "+":
  print(f"Sum: {a+b}")
elif m == "-":
  print(f"Difference: {a-b}")
elif m == "*":
  print(f"Product: {a*b}")
elif m == "/":
  print(f"Quotient: {a/b}")
else:
  print("Invalid operator")
