#Задание 1
#help = """
#help - вывести на экран справку о программе;
#add - добавить новую задачу в список;
#show - вывести на экран все добавленные задачи;"""

#tasks = []
#ok = True
#while ok:
#  command = input("Введите команду: ")
#  if command == "help":
#    print(help)
#  elif command == "show":
#    print(tasks)
#  elif command == "add":
#    task = input("Введите название задачи: ")
#    tasks.append(task)
#    print("Задача добавлена")
#  elif command == "exit":
#    print("Спасибо за использование! До свидания!")
#    break
#  else: 
#    print("""К сожалению, такой команды нет! 
#Спасибо за использование! До свидания!""")
#    break

#Задание 2
help = """
help - вывести на экран справку о программе;
add - добавить новую задачу в список;
show - вывести на экран все добавленные задачи;"""

taskstoday = []
taskstomorrow = []
tasksother = []
ok = True
while ok:
  command = input("Введите команду: ")
  if command == "help":
    print(help)
  elif command == "show":
    print("Задачи на сегодня: ",taskstoday,"; Задачи на завтра: ",taskstomorrow,"; Остальные задачи: ",tasksother)
  elif command == "add":   
    date = input("Введите дату выполнения: ")
    task = input("Введите название задачи: ")
    if date == "Сегодня": 
      taskstoday.append(task)
    elif date == "Завтра":
      taskstomorrow.append(task)
    else:
      tasksother.append(task)
    print("Задача добавлена")
  elif command == "exit":
    print("Спасибо за использование! До свидания!")
    break
  else: 
    print("""К сожалению, такой команды нет! 
Спасибо за использование! До свидания!""")
    break