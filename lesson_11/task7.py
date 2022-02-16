#7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число».
# Реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта.
# Для этого создаёте экземпляры класса (комплексные числа), выполните сложение и умножение созданных экземпляров.
# Проверьте корректность полученного результата

class ComplexNum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __add__(self, other):
        return ComplexNum(self.a + other.a, self.b + other.b)

    def __mul__(self, other):
        a = self.a
        b = self.b
        c = other.a
        d = other.b
        return ComplexNum(a*c - b*d, b*c +a*d)

    def __str__(self):
        return f"({self.a} + {self.b}i)"


num1 = ComplexNum(10,11)
num2 = ComplexNum(20,10)
print(num1+num2)
print(num1*num2)