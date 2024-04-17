#====== Задание 1. Калькулятор =============
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

#====== Задание 2. Високосный год =============
# year = int(input("Enter the year: "))
# if year % 4 != 0:
#   print(f"Год {year} не является високосным")
# elif year % 100 == 0:
#   if year % 400 == 0:
#     print(f"Год {year} является високосным")
#   else:
#     print(f"Год {year} не является високосным")
# else:
#   print(f"Год {year} является високосным")

#====== Задание 3. Шахматная доска ============
# for i in range (4):
#   print('* * * * ')
#   print(' * * * *')

#====== Задание 4. Сумма цифр трехзначного числа =============
# num = int(input("Enter the number: "))
# while (num != 0):
#   if num > 99 and num < 1000:
#     first = num // 100
#     second = num % 100 // 10
#     third = num % 10
#     print(f"Sum of digits: {first + second + third}")
#   else:
#     print("Invalid number, try again")
#   num = int(input("Enter the new number or type 0 for exit: "))
# print("Ok, bye")
