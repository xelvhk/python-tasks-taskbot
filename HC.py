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
