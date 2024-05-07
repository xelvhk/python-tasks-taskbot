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

#====== Task 2. Leap year =============
# year = int(input("Enter the year: "))
# if year % 4 != 0:
#   print(f"Year {year} is not leap")
# elif year % 100 == 0:
#   if year % 400 == 0:
#     print(f"Year {year} is leap")
#   else:
#     print(f"Year {year} is not leap")
# else:
#   print(f"Year {year} is leap")

#====== Task 3. Chessboard. V.1 ============
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
#   num = int(input('Enter the new number or  type 0 for exit: '))
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

#========= Task 10. Sum of list elements ==========
# sum = 0
# for i in range (len(first_arr)):
#   sum+=first_arr[i]
# print(sum)

#========= Task 11. Case inversion ==========
# word = "HeLLo"
# result = ""
# for i in word:
#   if i.isupper():
#     result += i.lower()
#   else:
#     result += i.upper()
# print(result)

#========= Task 12. URL normalization ==========
# url = input("Введите URL: ")
# result = ""
# if "https://" in url:
#   result = url
# elif "http://" in url:
#   result = "https://" + url[7:]
# else:
#   result = "https://" + url
# print(result)

#========= Task 13. Сreating a dictionary to record word lengths ==========
# dict = {}
# for i in range(int(input("Number of words? "))):
#   word = input("Enter a word: ")
#   dict[word] = len(word)
# print(dict)


#========= Task 14. Сhecking for closing parentheses ==============
# def isBalanced():
#   balance = 0
#   text = str(input("Enter the string: "))
#   for i in range(len(text)):
#     if text[i] == "(":
#       balance += 1
#     elif text[i] == ")":
#       balance -= 1
#   print(balance)
  
#   if balance < 0:
#     return "not all parentheses are open"
#   elif balance == 0:
#     return "all ok"
#   else:
#     return "not all parentheses are closed"

# print(isBalanced())

#========= Task 15. Happy ticket ==============
# def happy_ticket():
#   ticket = input("Enter the ticket number:")
#   left_part = ticket[3:]
#   right_part = ticket[:3]

#   if sum(map(int, left_part)) == sum(map(int, right_part)):
#     return "Yeah!"
#   else:
#     return "Don't worry. Choose the nesxt one"

# print(happy_ticket())
