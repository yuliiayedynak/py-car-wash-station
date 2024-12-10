class Car:
    def __init__(self,
                 comfort_class: int,
                 clean_mark: int,
                 brand: str) -> None:
        self.comfort_class = comfort_class
        self.clean_mark = clean_mark
        self.brand = brand


class CarWashStation:
    def __init__(self,
                 distance_from_city_center: float,
                 clean_power: int,
                 average_rating: float,
                 count_of_ratings: float) -> None:
        self.distance_from_city_center = round(distance_from_city_center, 1)
        self.clean_power = clean_power
        self.average_rating = round(average_rating, 1)
        self.count_of_ratings = round(count_of_ratings, 1)

    def serve_cars(self, cars: list[Car]) -> float:
        full_washing_price = 0.0
        for car in cars:
            if car.clean_mark < self.clean_power:
                full_washing_price += self.calculate_washing_price(car)
                self.wash_single_car(car)
        return round(full_washing_price, 1)

    def calculate_washing_price(self, car: Car) -> float:
        return round(car.comfort_class
                     * (self.clean_power - car.clean_mark)
                     * self.average_rating
                     / self.distance_from_city_center, 1)

    def wash_single_car(self, car: Car) -> None:
        car.clean_mark = self.clean_power

    def rate_service(self, rating: int) -> None:
        if 1 <= rating <= 5:
            sum_of_ratings = (self.average_rating
                              * self.count_of_ratings
                              + rating)
            self.count_of_ratings += 1
            self.average_rating = round(sum_of_ratings
                                        / self.count_of_ratings, 1)
