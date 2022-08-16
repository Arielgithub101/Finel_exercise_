from CarClass import Car
from CarType import CarTypes


class Electric(Car):
    def __init__(self, price: int, year_of_prod: int, mile: int, color: str, company: str, id_plate: int):
        super().__init__(price, year_of_prod, mile, color, company, id_plate, CarTypes.gas)
