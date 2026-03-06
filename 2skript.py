'''count = 0
while count < 10:
    print(count)
    # забыли увеличить счётчик
print("Дошли до конца!")'''#Ошибочное


count = 0
while count < 10:
    count=count+1
    print(count)
print("Дошли до конца!")
#ошибка в 3 строке! она отсутсвовала поэтому count постоятно был равен 0