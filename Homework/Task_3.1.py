def max(a: float, b: float) -> None:
    if a > b:
        print(a)
    else:
        print(b)
a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))
max(a, b)