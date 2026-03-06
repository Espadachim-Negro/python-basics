'''numbers = [10, 20, 30, 40, 50]
sum = 0
for i in range(1, 6):
    sum = sum + numbers[i]
print("Сумма:", sum)'''#Ошибочное

numbers = [10, 20, 30, 40, 50]
sum = 0
for i in range(0, 5):
    sum = sum + numbers[i]
print("Сумма:", sum)
#ошибка была в 3 строке в диапзаоне! 