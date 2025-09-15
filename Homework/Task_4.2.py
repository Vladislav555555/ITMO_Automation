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
            print("Ошибка. На ноль делить нельзя!")
        else:
            result = a / b
            print(f"Деление: {a} / {b} = {result}")

    def subtraction(self, a, b):
        result = a - b
        print(f"Вычитание: {a} - {b} = {result}")


calculator = Math(0, 0)
calculator.addition(17, 8)
calculator.multiplication(59, 3)
calculator.division(8, 7)
calculator.subtraction(12, 6)