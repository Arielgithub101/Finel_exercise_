from CarClass import Car
from typing import Dict
from CarType import CarTypes


class CarYard:

    def __init__(self, all_car_dict: Dict[int, Car] = None):
        if all_car_dict is None:
            self.all_car_dict: Dict[int, Car] = {}
        else:
            self.all_car_dict: Dict[int, Car] = all_car_dict

    def __display_all_cars_by_type(self, type_car: CarTypes) -> None:
        for car in self.all_car_dict.values():
            if car.car_type is type_car:
                car.car_info()

    def add_car(self, new_car: Car) -> None:

        if new_car.id_plate in self.all_car_dict:
            return print('car License plate already in system,try again')
        self.all_car_dict[new_car.id_plate] = new_car
        print(' ')
        new_car.car_info()
        print(' ')
        print('The new Car added !!')

    def remove_car(self, id_remove: int) -> None:
        try:
            del self.all_car_dict[id_remove]
            print('The car has been deleted from the database')
        except KeyError:
            print('try again id doesnt exist in the database')

    def display_specific_car(self, id_check: int) -> None:

        try:
            self.all_car_dict[id_check].car_info()
        except KeyError:
            print('car not found')

    def display_all_gas_car(self) -> None:
        self.__display_all_cars_by_type(CarTypes.gas)

    def display_all_electric_cars(self) -> None:
        self.__display_all_cars_by_type(CarTypes.electric)

    def display_all_hybrid_cars(self) -> None:
        self.__display_all_cars_by_type(CarTypes.hybrid)

    def display_cars_by_color(self, color: str) -> None:
        for car in self.all_car_dict.values():
            if car.color == color:
                car.car_info()

    def display_cars_by_year(self, year: int) -> None:
        for car in self.all_car_dict.values():
            if car.year_of_prod > year:
                car.car_info()
