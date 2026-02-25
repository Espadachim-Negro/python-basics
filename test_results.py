results = ["Pass",'Fail','Pass','Error','Pass']

print('Все результаты:', results)
print('Количество тестов:', len(results))
print('Количество Pass:', results.count('Pass'))
print('Количество Fail/Error:', results.count('Fail') + results.count('Error'))

# Найти первый Fail
if 'Fail' in results:
    first_fail = results.index('Fail')
    print('Первый Fail на позиции:', first_fail +1)
