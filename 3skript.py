'''def add_item(item, basket=[]):
    basket.append(item)
    return basket

print(add_item("яблоко"))     # ['яблоко']
print(add_item("банан"))      # ['яблоко', 'банан']  ← сюрприз!
print(add_item("груша"))      # ['яблоко', 'банан', 'груша']''' #Ошибочное

def add_item(item, basket=None):
    if basket is None:
        basket = []
    basket.append(item)
    return basket
    

print(add_item("яблоко"))     
print(add_item("банан"))      
print(add_item("груша"))      
# Ошибка в первой строке так как переменной basket присваивается список - изменяемый обьект