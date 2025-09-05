def year(a :int) -> int:
    if a in (12, 1, 2):
        print("Зима")
    elif a in (3, 4, 5):
        print("Весна")
    elif a in (6, 7, 8):
        print("Лето")
    elif a in (9, 10, 11):
        print("Осень")
    else:
        print("Ощибка. Попробуйте ввести число от 1 до 12")
month = int(input("Введите номер месяца: "))
year(month)