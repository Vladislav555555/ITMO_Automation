def calculate_days(years: int, months: int) -> None:
    """
    Вычисляет и выводит количество дней за заданное количество лет и месяцев,
    считая, что в каждом месяце 29 дней.
    """
    total_months = years * 12 + months  # Общее количество месяцев
    total_days = total_months * 29      # Общее количество дней
    print(f"Количество дней: {total_days}")

# Пример использования:
years_input = int(input("Введите количество лет: "))
months_input = int(input("Введите количество месяцев: "))

calculate_days(years_input, months_input)