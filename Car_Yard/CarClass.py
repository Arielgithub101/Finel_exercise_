class Car:
    id_car:int = 1
    def __init__(self,price:int, year_of_prod:int, mile:int, color:str, company:str, type_car:str):
        self.price: int = price
        self.year_of_prod: int = year_of_prod
        self.mile: int = mile
        self.color: str = color
        self.company: str = company
        self.type_car: str = type_car
        self.id_car: int = self.id_car
        Car.set_id()
    @classmethod
    def set_id(cls):
        cls.id_car += 1


    def car_info(self):
        print(f'''hello your new car as follow : 
        compeny name : {self.company}
        type car : {self.type_car}
        Year of prudaction : {self.year_of_prod}
        initial car mile : {self.mile}
        color : {self.color}
        Price : {self.price}
        The ID nuber of the car : !! --- {self.id_car} --- !!
        please remmeber the id num for futher action ! ''')

