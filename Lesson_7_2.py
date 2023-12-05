from Lesson_7_1 import Car


class Taxi:
    def __init__(self, cars: [Car]):
        self.cars = cars

    def find_car(self, count_passengers: int, is_baby: bool):
        for car in self.cars:
            if not car.is_busy and car.is_baby_seat == is_baby and count_passengers <= car.count_passenger_seats:
                car.is_busy = True
                return car

        return None
