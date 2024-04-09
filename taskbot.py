from random import choice

import telebot

token = '_____'
bot = telebot.TeleBot(token)

RANDOM_TASKS = ['Выучить Python', 'Прочитать книгу', 'Прогуляться', 'Сделать зарядку']

todos = dict()
categories=[]

HELP = '''
Список доступных команд:
- show  - напечать все задачи на заданную дату (Пример - /show сегодня)
- add - добавить задачу (Пример - /add сегодня почитать книгу)
- random - добавить на сегодня случайную задачу
- help - Напечатать help
- cats - Узнать категории дел
'''


def add_todo(date, task):
    date = date.lower()
    if todos.get(date) is not None:
        todos[date].append(task)
    else:
        todos[date] = [task]


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, HELP)


@bot.message_handler(commands=['random'])
def random(message):
    task = choice(RANDOM_TASKS)
    category = 'случайные'
    add_todo('сегодня', task)
    categories.append(category)
    bot.send_message(message.chat.id, f'Задача {task} добавлена на сегодня в категорию {category}')


@bot.message_handler(commands=['add'])
def add(message):
    _, date, tail, category = message.text.split(maxsplit=3)
    task = ' '.join([tail])
    if len(task) > 2:
        add_todo(date, task)
        categories.append(category)
        bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date} в категорию @{category}')
    else:
        task = choice(RANDOM_TASKS)
        add_todo(date, task)
        category = 'случайные'
        categories.append(category)
        bot.send_message(message.chat.id, 'В задаче меньше 3 символов, поэтому добавим случайную задачу')
        bot.send_message(message.chat.id, f'Задача {task} добавлена на дату {date} в категорию @{category}')

@bot.message_handler(commands=['show'])
def print_(message):
    date = message.text.split()[1].lower()
    if date in todos:
        tasks = ''
        for task in todos[date]:
            tasks += f'{date} {task}\n'
    else:
        tasks = 'Такой даты нет'
    bot.send_message(message.chat.id, tasks)

@bot.message_handler(commands=['cats'])
def cats_(message):
    bot.send_message(message.chat.id,f'Список категорий дел: {categories}')

bot.polling(none_stop=True)
