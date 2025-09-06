def calculate_days(years: int, months: int) -> int:

    total_months = years * 12 + months
    total_days = total_months * 29
    print(f"Количество дней: {total_days}")

years_input = int(input("Введите количество лет: "))
months_input = int(input("Введите количество месяцев: "))

calculate_days(years_input, months_input)