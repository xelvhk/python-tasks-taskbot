#====== Task 2. Leap year =============
year = int(input("Enter the year: "))
if year % 4 != 0:
  print(f"Year {year} is not leap")
elif year % 100 == 0:
  if year % 400 == 0:
    print(f"Year {year} is leap")
  else:
    print(f"Year {year} is not leap")
else:
  print(f"Year {year} is leap")
