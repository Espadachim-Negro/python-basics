<img width="1920" height="1080" alt="image" src="https://github.com/user-attachments/assets/ca7df166-3d21-4196-bd21-81f485da8813" /># python-basics
My first Python scripts from Automate the Boring Stuff

## Chapter 2 — Flow Control (if / elif / else)

Здесь я практикую условные операторы, сравнения и булевы значения из второй главы книги "Automate the Boring Stuff with Python".

Что изучил:
- Булевы значения: `True` / `False`
- Операторы сравнения: `==`, `!=`, `>`, `<`, `>=`, `<=`
- Логические операторы: `and`, `or`, `not`
- Условные конструкции: `if`, `elif`, `else`
- Отступы (indentation) — очень важно!

### Примеры скриптов из практики

- dishonestcapacity.py — калькулятор "нечестной ёмкости" (пример из книги)
- test3.py — мои эксперименты с if/else
- grade.py — оценка по баллам
- weather_advice.py - совет по погоде
- time.py - проверка времени суток

## Chapter 3 — Loops (while / for / range / break / continue)

Здесь я практикую циклы из третьей главы книги "Automate the Boring Stuff with Python".  
Циклы — это основа автоматизации: они позволяют повторять действия много раз (например, проверять элементы, ждать условий, генерировать данные).

Что изучил:
- `while` — повторяет код, пока условие истинно (`True`)
- `for` — перебирает элементы последовательности (списки, строки, range)
- `range(start, stop, step)` — генерирует числа (например, `range(1, 11)` → 1–10)
- `break` — выходит из цикла досрочно
- `continue` — пропускает остаток итерации и идёт дальше
- `import random` — случайные числа (очень полезно для тестов)

### Примеры скриптов из практики

-10 numbers.py - выводит числа от 1 до 10 при помощи цикла for и while
-exit.Example.py - бесконечный цикл пока пользователь не введёт exit
-guessTheNumber.py - угадываешь число от 1 до 20 при помощи подсказок, 6 попыток
-rpsGame.py - Игра камень ножницы бумага
