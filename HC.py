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

#========= Task 16. Searching for nearest coordinates ==============
# def div_coordinate(coord1,coord2):
#   part_one = abs(coord1[0] - coord2[0])
#   part_two = abs(coord1[1] - coord2[1])
#   return (part_one + part_two)

# locations = [
#   ['Library',10,2],
#   ['Cinema',3,20],
#   ['Hexlet College',15,10]
# ]

# def find_location():
#   x = int(input("Введите первую координату:"))
#   y = int(input("Введите вторую координату:"))
#   coordinates = [x,y]
#   result = []
#   nearest = 1000000
#   for i in range(len(locations)):
#     if div_coordinate(coordinates,locations[i][1:]) < nearest:
#       nearest = div_coordinate(coordinates,locations[i][1:])
#       result = locations[i]
#   return result

# print(find_location())
