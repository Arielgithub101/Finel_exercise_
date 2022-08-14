from CarClass import Car
from typing import Dict


class CarYard:

    def __init__(self):
        self.all_car_dict: Dict[int, Car] = {}

    def display_all_cars_by_type(self, type_car: str) -> None:
        for car in self.all_car_dict.values():
            if car.type_car == type_car:
                car.car_info()

    def add_car(self, new_car: Car) -> None:

        if new_car.id_plate in self.all_car_dict:
            return print('car License plate already in system,try again')
        self.all_car_dict[new_car.id_plate] = new_car
        print(' ')
        new_car.car_info()
        print(' ')
        print('The new Car added !!')

    def remove_car(self, id_check: int) -> None:
        try:
            del self.all_car_dict[id_check]
            print('The car has been deleted from the database')
        except KeyError:
            print('try again id doesnt exist in the database')

    def display_specific_car(self, id_check: int) -> None:
        try:
            self.all_car_dict.get(id_check).car_info()
        except AttributeError:
            print('car not found')

    def display_all_gas_car(self) -> None:
        self.display_all_cars_by_type('gas')

    def display_all_electric_cars(self) -> None:
        self.display_all_cars_by_type('electric')

    def display_all_hybrid_cars(self) -> None:
        self.display_all_cars_by_type('hybrid')

    def display_cars_by_color(self, color: str) -> None:
        for item in self.all_car_dict.values():
            if item.color == color:
                item.car_info()

    def display_cars_by_year(self, year: int) -> None:
        for item in self.all_car_dict.values():
            if item.year_of_prod > year:
                item.car_info()
