def diff_1(a: float, b: float) -> float:
    if abs(a - b) == 135:
        print("Yes")
    else:
        print("No")
k1 = float(input("Введите первое число: "))
k2 = float(input("Введите второе число: "))
diff_1(k1, k2)