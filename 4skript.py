'''def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

for num in range(10):
    if is_even(num = num):
        print(num, "чётное")''' #ошибочное


def is_even(n):
    if n % 2 == 0:
        return True
    else:
        return False

for num in range(10):
    if is_even(num):
        print(num, "чётное")
# ошибка была в 8 строке, лишнее было написано num=num