temp = float(input('Какая погода на улице?:'))
if temp >=15 and temp <=30:
    print('Нормальная погода - гуляй!')
elif temp >30:
    print('Лучше останься дома - слишком жарко!')
else:
    print('Оденься по теплее!')