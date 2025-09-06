class Car:
    def __init__(self, color, type, year):
        self.color = color
        self.type = type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def car_year(self, year):
        self.year = year
        print(f"Год выпуска : {self.year}")

    def car_type(self, type):
        self.type = type
        print(f"Тип автомобиля : {self.type}")

    def car_color(self, color):
        self.color = color
        print(f"Цвет автомобиля : {self.color}")


Test = Car("Чёрный", "Купе", 2020)
Test.start()
Test.stop()
Test.car_year(2025)
Test.car_type("Седан")
Test.car_color("Серый") 