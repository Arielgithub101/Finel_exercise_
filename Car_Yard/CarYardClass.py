from CarClass import Car
from typing import Dict


class CarYard:

    def __init__(self, all_car_dict: Dict[int, Car] = {}):
        self.all_car_dict: Dict[int, Car] = all_car_dict

    def add_car(self, new_car: Car) -> None:

        if self.all_car_dict.get(new_car.id_plate) is None:
            self.all_car_dict[new_car.id_plate] = new_car
            print(' ')
            new_car.car_info()
            print(' ')
            return print('The new Car added !!')
        else:
            return print('car License plate already in system,try again')

    def remove_car(self, id: int) -> None:

        if self.all_car_dict.get(id) is not None:
            del self.all_car_dict[id]
            return print('car removed')
        else:
            return print('car not found')

    def display_specific_car(self, id: int) -> None:

        if self.all_car_dict.get(id) is not None:
            return self.all_car_dict.get(id).car_info()
        else:
            return print('car not found')

    def display_all_gas_cars(self) -> None:
       CarYard.disply_info_by_param(self.all_car_dict,'gas')

    def display_all_electric_cars(self) -> None:
        CarYard.disply_info_by_param(self.all_car_dict, 'electric')

    def display_all_hybrid_cars(self) -> None:
        CarYard.disply_info_by_param(self.all_car_dict,'hybrid')

    def display_cars_by_color(self, color: str) -> None:
        CarYard.disply_info_by_param(self.all_car_dict,color)

    def display_cars_by_year(self, year: int) -> None:
        CarYard.disply_info_by_param(self.all_car_dict,year)

    @classmethod
    def disply_info_by_param(cls, info_dict: Dict[int, Car], param):

        if type(param) == int:
            for item in info_dict.values():
                if item.year_of_prod > param:
                    item.car_info()
        elif param == 'gas':
            for item in info_dict.values():
                if item.type_car == 'gas':
                    item.car_info()
        elif param == 'electric':
            for item in info_dict.values():
                if item.type_car == 'electric':
                    item.car_info()
        elif param == 'hybrid':
            for item in info_dict.values():
                if item.type_car == 'hybrid':
                    item.car_info()
        elif param != 'gas' and 'electric' and 'hybrid':
            for item in info_dict.values():
                if item.color == param:
                    item.car_info()
        else:
            return print('something went wrong please check your input again...')
