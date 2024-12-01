import utils
try:
    first = int(input("Введите число a: "))
except ValueError:
    print('Тебе по китайски написать? Введи ЧИСЛО, а не ещё что-то')
    first = int(input("Введите число a: "))
try:
    second = int(input("Введите число b: "))
except ValueError:
    print('Не ну ты смог выбесить даже строчку в командной строке... Введи ЧИСЛО!!!')
    second = int(input("Введите число b: "))
if second != 0:
    print(utils.mathematics(first, second))
else:
    print("На ноль делить, путь к тёмной стороне")   
