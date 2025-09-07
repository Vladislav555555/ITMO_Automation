def all_days(years: int, months: int) -> int:

    total_months = years * 12 + months
    total_days = total_months * 29
    print(f"Количество дней: {total_days}")

a = int(input("Введите количество лет: "))
b = int(input("Введите количество месяцев: "))

all_days(a, b)