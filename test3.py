'''# Приветствие + возраст
name=input("Как тебя зовут?")
print("Привет,",name +"! Ты круто начал python.")

age_text=input('Сколько тебе лет?')
age = int(age_text) # превращаем текст в число
print('Через год тебе будет', age + 1, 'лет')
print('Имя большими буквами:', name.upper())
print('Имя маленькими буквами:',name.lower())

# Калькулятор
a=float(input('Первое число:'))
b=float(input('Второче число:'))

print('Сумма:', a+b)
print('Разница:', a-b)
print('Умножение:', a*b)
print('Деление:',a/b )
print('Остаток:', a%b)

# Файл 3: tasks.py (TODO-лист)
task1 = input('Задача1:')
task2 = input('Задача2:')
task3 = input('Задача3:')

print("\nТвои задачи сегодня:")
print("1. " + task1)
print("2. " + task2)
print('3. ' + task3)

print("Все задачи одной строкой:", task1+'|'+ task2 + '|' + task3)
print("Общая длина:", len(task1+task2+task3))'''

# Файл 4: text_game.py (игра со строкой)
text=input('Напиши любое предложение:')
print('Длина текста:',len(text))
print('Всё большими буквами:',text.upper())
print('Количество "а":',text.lower().count('а'))
print('Количество пробелов:',text.count(' '))
