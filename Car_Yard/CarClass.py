from CarType import CarTypes
from abc import ABC


class Car(ABC):
    def __init__(self, price: int, year_of_prod: int, mile: int, color: str, company: str, id_plate: int,
                 car_type: CarTypes):
        self.price: int = price
        self.year_of_prod: int = year_of_prod
        self.mile: int = mile
        self.color: str = color
        self.company: str = company
        self.id_plate: int = id_plate
        self.car_type: CarTypes = car_type

    def car_info(self):
        print(f'''hello your new car as  follow : 
        company name : {self.company}
        Type of the Car : {self.car_type.name}
        Year of production : {self.year_of_prod}
        initial car mile : {self.mile}
        color : {self.color}
        Price : {self.price}
        The ID nuber of the car : !! --- {self.id_plate} --- !!
        Please remember the ID number for further activity ! ''')
