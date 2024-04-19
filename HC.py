#====== Task 1. Simple calculator =============
# a = int(input("Enter the first number: "))
# b = int(input("Enter the second number: "))
# m = input("Enter the operator:")
# if m == "+":
#   print(f"Sum: {a+b}")
# elif m == "-":
#   print(f"Difference: {a-b}")
# elif m == "*":
#   print(f"Product: {a*b}")
# elif m == "/":
#   print(f"Quotient: {a/b}")
# else:
#   print("Invalid operator")

#====== Task 2. Високосный год =============
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

#====== Task 3. Chessboard ============
# for i in range (4):
#   print('* * * * ')
#   print(' * * * *')

#====== Task 4. Sum of digits of a three-digit number =============
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

#========= Task 5. Training schedule ==========
# dist = 10
# days = 0
# while (dist < 25):
#   dist = dist + dist * 0.1
#   days += 1
#   print(f'{days} days, {dist} km')
# print(f"The athlete needs {days} days")

#========= Task 6. Identifying positive and negative numbers ==========
# num = int(input('Enter the number: '))
# while (num != 0):
#   if num > 0:
#     print('number is positive')
#   elif num < 0:
#     print('number is negative')
#   num = int(input('Enter the new number or  type 0 for exit'))
# print('It's 0, bye')

#========= Task 7. Multiples of 3 ==========
# for i in range(3, 100, 3):
#   print(i)
#========= Task 8. Multiples of 3. Reverse order ==========
# for i in range(99, 0, -3):
#   print(i)
#========= Task 9. Adding and removing elements from list with append and remove methods ==========
# first_arr = []
# for i in range (10):
#   if i % 2 == 0:
#     first_arr.append(i)
# print(first_arr)

# # for i in range (len(first_arr)):
# #   if i == len(first_arr) - 1:
# #     first_arr.remove(first_arr[i])
# # print(first_arr)

# sum = 0
# for i in range (len(first_arr)):
#   sum+=first_arr[i]
# print(sum)
