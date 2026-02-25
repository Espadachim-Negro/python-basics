tasks = []

while True:
    print("\n1. Добавить задачу")
    print('2. Показать все задачи')
    print('3. Удалить задачу')
    print('4. Отметить выполненной')
    print('5. Выход')
    choice=input("Выбери:")

    if choice =='1':
        task=input("Новая задача:")
        tasks.append(task)

    elif choice =='2':
        if tasks:
            for i , task in enumerate(tasks,1):
                print(f"{i}. {task}")
        else:
            print('Список пуст')
    
    elif choice =='3':
        if tasks:
            num = int(input('Номер задачи:')) - 1
            if 0<=num < len(tasks):
                removed = tasks.pop(num)
                print(f'Удалено:{removed}')
            else:
                print('Неверный номер')
            
    elif choice == '4':
        if tasks:
            num = int(input("Номер вывполненной задачи:")) - 1
            if 0<=num<len(tasks):
                tasks[num] += '[DONE]'
                print('Отмечено как выполненное')

            else:
                print('Неверный номер ')
        elif choice==5:
            break