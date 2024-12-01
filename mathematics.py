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
try:
    print("Сумма чисел: ", first + second, 
    "\n" "Разность чисел: ", first - second, 
    "\n" "Результат умножения: ", first * second, 
    "\n" "Частное от деления чисел: ", first // second, 
    "\n" "Результат деления: ", first % second, 
    "\n" "Число а в степени b", first ** second )
except ZeroDivisionError:
        print('Не ну ты совсем ёбобо, на ноль делить')
        