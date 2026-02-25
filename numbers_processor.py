numbers = []
while True:
    inp=input('Введи число или done:')
    if inp=='done':
        break
    numbers.append(float(inp))

if numbers:
    print('Сумма:', sum(numbers))
    print('Среднее:',sum(numbers)/len(numbers))
    print('Максимум:', max (numbers))
    print('Минимум:', min(numbers))
    print('Отсортированный список:',sorted(numbers))
    