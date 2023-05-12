#ДЗ на понедельник (Ivanov_Lesson_14.py):
# Простейший калькулятор c введёнными двумя числами вещественного типа.
# Ввод с клавиатуры: операции + - * / и два числа. Операции являются функциями.
# Обработать ошибку: “Деление на ноль”
# Ноль использовать в качестве завершения программы (сделать как отдельную операцию).
# Работу загружаем в репозиторий гита. Скидываем ссылку НА ФАЙЛ!

def summa(a, b):
    return a + b
def subtrac(a, b):
    return a - b
def multipl(a, b):
    return a * b
def divis(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return('Ошибка деления на 0')

def calc():
    while True:
        y = ['-', '+', '/', '*']
        a = input('Введите первую переменную: ')
        b = input('Введите вторую переменную: ')
        try:
            a = float(a)
            b = float(b)
        except ValueError:
            print('Ошибка переменной')
            continue
        x = str(input('Введите действие: '))
        if x not in y:
            print('Ошибка действия нет')
            continue
        if x == '-':
            subtrac(a, b)
            print(subtrac(a, b))
        elif x == '+':
            summa(a, b)
            print(summa(a, b))
        elif x == '*':
            multipl(a, b)
            print(multipl(a, b))
        elif x == '/':
            divis(a, b)
            print(divis(a, b))
        y = input('Введите 0 для завершения: ')
        if y == '0':
            return ('Программа завершена')

print(calc())


