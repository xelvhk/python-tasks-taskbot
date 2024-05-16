#Задание 1
#date = input('Введите дату: ')
#task = input('Введите задачу: ')
#print(date, task)

#Задание 2
#dates = []
#tasks = []
#i = 0
#j = 0
#while i < 3:
#    date = input('Введите дату: ')
#    task = input('Введите задачу: ')
#    dates.append(date)
#    tasks.append(task)
#    i += 1
#while j < 3:
#    print(dates[j], tasks[j])
#    j += 1

#Задание 3
todolist = {}
i = 0
while i < 3:
    date = input('Введите дату: ')
    task = input('Введите задачу: ')
    todolist[date] = task
    i += 1
    
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