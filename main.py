class Car:
    def __init__(self, make=None, model=None, year=None, price=None):
        self.make = make
        self.model = model
        self.year = year
        self.price = price

    def display_info(self):
        print(f"Car Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nPrice: ${self.price:.2f}\n")

    def apply_discount(self, percentage):
        if self.price:
            discount_amount = (percentage / 100) * self.price
            self.price -= discount_amount
            print(f"Discount of {percentage}% applied. New price: ${self.price:.2f}")
        else:
            print("Price not set, cannot apply discount.")

def main():
    n = int(input("Enter the number of cars: "))
    car_list = []

    for i in range(n):
        print(f"\nEnter details for Car {i + 1}:")
        make = input("Make: ")
        model = input("Model: ")
        year = int(input("Year: "))
        price = float(input("Price: "))

        car = Car(make, model, year, price)
        car_list.append(car)

    print("\nCar Details:")
    for car in car_list:
        car.display_info()


    if car_list:
        discount = float(input("Enter discount percentage for the first car: "))
        car_list[0].apply_discount(discount)
        car_list[0].display_info()

if __name__ == "__main__":
    main()

