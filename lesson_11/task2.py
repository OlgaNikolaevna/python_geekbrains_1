# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
# Проверьте его работу на данных, вводимых пользователем.
# При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.

class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt

val1 = input("Введите числитель: ")
val2 = input("Введите знаменатель: ")

try:
    val1 = float(val1)
    val2 = float(val2)
    if val2 == 0:
        raise OwnError("Вы ввели 0!")
except ValueError:
    print("Вы ввели не число")
except OwnError as err:
    print(err)
else:
    print(f"Результат: {val1/val2}")