from CarType import CarTypes


class Car:
    def __init__(self, price: int, year_of_prod: int, mile: int, color: str, company: str, type_car: str,
                 id_plate: int):
        self.price: int = price
        self.year_of_prod: int = year_of_prod
        self.mile: int = mile
        self.color: str = color
        self.company: str = company
        try:
            self.type_car: CarTypes = CarTypes[type_car]
        except KeyError:
            print('! ---- Car type not available at the moment  ---- !')
        self.id_plate = id_plate

    def car_info(self):
        print(f'''hello your new car as  follow : 
        company name : {self.company}
        type car : {self.type_car.name}
        Year of production : {self.year_of_prod}
        initial car mile : {self.mile}
        color : {self.color}
        Price : {self.price}
        The ID nuber of the car : !! --- {self.id_plate} --- !!
        Please remember the ID number for further activity ! ''')
