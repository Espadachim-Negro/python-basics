hour=int(input('\nEnter hour (0-23):'))

if 6 <= hour < 12:
    print('Good morning!')
elif 12 <= hour <18:
    print('Good afternoon')
elif 18<= hour <22:
    print('Good evening')
elif 22<= hour <=23 or 0 <= hour <6:
    print('Good night')
else:
    print('This time of day does not exist!!! please try again.')