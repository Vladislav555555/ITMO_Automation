class Test_PS:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def S(self):
        return self.w * self.h

    def P(self):
        return 2 * (self.w + self.h)

parametr1 = Test_PS(4, 5)
parametr2 = Test_PS(7, 3)
parametr3 = Test_PS(10, 2)

print(f"Прямоугольник : ширина = {parametr1.w}, высота = {parametr1.h}")
print(f"Площадь: {parametr1.S()}")
print(f"Периметр: {parametr1.P()}")
print("")
print(f"Прямоугольник : ширина = {parametr2.w}, высота = {parametr2.h}")
print(f"Площадь: {parametr2.S()}")
print(f"Периметр: {parametr2.P()}")
print("")
print(f"Прямоугольник : ширина = {parametr3.w}, высота = {parametr3.h}")
print(f"Площадь: {parametr3.S()}")
print(f"Периметр: {parametr3.P()}")






'''class Test_PS:
    def __init__(self, w, h):
        self.w = w
        self.h = h

    def S(self):
        return self.w * self.h

    def P(self):
        return 2 * (self.w + self.h)

parametr1 = Test_PS(4, 5)
parametr2 = Test_PS(7, 3)
parametr3 = Test_PS(10, 2)

PS = [parametr1, parametr2, parametr3]

for i, parametr in enumerate(PS, start=1):
    print(f"Прямоугольник {i}: ширина = {parametr.w}, высота = {parametr.h}")
    print(f"Площадь: {parametr.S()}")
    print(f"Периметр: {parametr.P()}")
    print() '''