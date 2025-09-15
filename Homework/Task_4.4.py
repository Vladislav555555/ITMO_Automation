class Car:
    def __init__(self, color, car_type, year):
        self.color = color
        self.car_type = car_type
        self.year = year

    def start(self):
        print("Автомобиль заведен")

    def stop(self):
        print("Автомобиль заглушен")

    def set_year(self, year):
        self.year = year
        print(f"Год выпуска: {self.year}")

    def set_type(self, car_type):
        self.car_type = car_type
        print(f"Тип автомобиля: {self.car_type}")

    def set_color(self, color):
        self.color = color
        print(f"Цвет автомобиля: {self.color}")



car = Car("Чёрный", "Купе", 2020)

car.start()
car.stop()
car.set_year(2025)
car.set_type("Седан")
car.set_color("Серый")