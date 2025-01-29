class Car:
    def __init__(self, brand, model, year, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.is_running = False

    def start(self):
        if not self.is_running:
            self.is_running = True
            print(f"{self.brand} {self.model} has started.")
        else:
            print(f"{self.brand} {self.model} is already running.")

    def stop(self):
        if self.is_running:
            self.is_running = False
            print(f"{self.brand} {self.model} has been turned off.")
        else:
            print(f"{self.brand} {self.model} is already off.")

    def info(self):
        print(f"Brand: {self.brand}, Model: {self.model}, Year: {self.year}, Color: {self.color}")

car1 = Car("Toyota", "Camry", 2020, "White")
car2 = Car("BMW", "X5", 2022, "Black")

car1.info()
car1.start()
car1.stop()

print()

car2.info()
car2.start()
car2.stop()
