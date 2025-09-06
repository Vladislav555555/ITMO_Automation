class Math:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def addition(self, a, b):
        result = a + b
        print(f"Сложение: {a} + {b} = {result}")

    def multiplication(self, a, b):
        result = a * b
        print(f"Умножение: {a} * {b} = {result}")

    def division(self, a, b):
        if b == 0:
            print("Ошибка. На ноль делить нельзя !")
        else:
            result = a / b
            print(f"Деление: {a} / {b} = {result}")

    def subtraction(self, a, b):
        result = a - b
        print(f"Вычитание: {a} - {b} = {result}")

Test = Math(0, 0)
Test.addition(17, 8)
Test.multiplication(59, 3)
Test.division(8, 7)
Test.subtraction(12, 6)
