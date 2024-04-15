# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# m = input("Enter the operator:")
# if m == "+":
#   print(f"Сумма: {a+b}")
# elif m == "-":
#   print(f"Разность: {a-b}")
# elif m == "*":
#   print(f"Произведение: {a*b}")
# elif m == "/":
#   print(f"Частное: {a/b}")
# else:
#   print("Invalid operator")
# # print (f"Произведение: {a*b}, Сумма: {a+b}, Разность: {a-b}, Частное: {a/5}")

# year = int(input("Enter the year: "))

if year % 4 != 0:
  print(f"Год {year} не является високосным")
elif year % 100 == 0:
  if year % 400 == 0:
    print(f"Год {year} является високосным")
  else:
    print(f"Год {year} не является високосным")
else:
  print(f"Год {year} является високосным")

num = int(input("Enter the number: "))
a = num // 100
print(a)