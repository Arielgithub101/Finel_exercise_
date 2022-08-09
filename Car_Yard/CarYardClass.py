from CarClass import Car
from typing import List


class CarYard():
    car_gas_list:List[Car] = []
    car_elctric_list:List[Car] = []
    car_hybrid_list:List[Car] = []
    all_cars:List[Car] = []

    def __init__(self):
        pass

    def display_menu(self) -> None:

        flag = 'y'
        while flag == 'y':

            print(''' your option is :

            1) add new car :
            2) remove a car :
            3) display info car :
            4) display all gas info car :
            5) display all elctric info car :
            6) display all hybrid info car :
            7) display info car by color :
            8) display info car after given year :
            9) Exit 
            ''')
            user_choice:int = int(input("please enter numbrer of choice action -- > :"))
            match user_choice:
                case 1:
                    self.add_car()
                    flag:str = input('would you like to do anther action ? ---> y/n : ')

                case 2:
                    user_input:int = int(input("please enter id number -- > : "))
                    self.remove_car(user_input)
                    flag:str = input('would you like to do anther action ? ---> y/n : ')

                case 3:
                    user_input:int = int(input("please enter id number -- > : "))
                    self.display_specific_car(user_input)
                    flag:str = input('would you like to do anther action ? ---> y/n : ')

                case 4:
                    self.display_all_gas_cars()
                    flag:str = input('would you like to do anther action ? ---> y/n : ')

                case 5:
                    self.display_all_electric_cars()
                    flag:str = input('would you like to do anther action ? ---> y/n : ')

                case 6:
                    self.display_all_hybrid_cars()
                    flag:str = input('would you like to do anther action ? ---> y/n : ')

                case 7:
                    user_input:str = input("please enter color  -- > : ")
                    self.display_cars_by_color(user_input)
                    flag:str = input('would you like to do anther action ? ---> y/n : ')

                case 8:
                    user_input:int = int(input("please enter year -- > : "))
                    self.display_cars_by_year(user_input)
                    flag:str = input('would you like to do anther action ? ---> y/n : ')

                case 9:
                    print("thank you ! good by")
                    flag = 'n'

                case _:
                    print("invalid option,try again")


    def add_car(self) -> None:
        print('enter your car info ---> ')
        price:int = int(input('please enter car price : '))
        year_of_prod:int = int(input('please enter car year_of_prod : '))
        mile:int = int(input('please enter mile of the car : '))
        color:str = input('please enter car color : ')
        company:str = input('please enter car company : ')
        type_car:str = input('please enter the type car : ')
        new_car = Car(price, year_of_prod, mile, color, company, type_car)
        self.all_cars.append(new_car)
        if new_car.type_car == 'gas':
            self.car_gas_list.append(new_car)
        elif new_car.type_car == 'electric':
            self.car_elctric_list.append(new_car)
        elif new_car.type_car == 'hybrid':
            self.car_hybrid_list.append(new_car)
        print(' ')
        new_car.car_info()
        print(' ')
        return print('The new Car added !!')


    def remove_car(self, id:int) -> None:
        for car in self.all_cars:
            if id == car.id_car:
                car_obj:Car = car
                if car_obj in self.car_gas_list:
                    self.car_gas_list.remove(car_obj)
                    self.all_cars.remove(car_obj)
                    return print('car has been remove')
                elif car_obj in self.car_elctric_list:
                    self.car_elctric_list.remove(car_obj)
                    self.all_cars.remove(car_obj)
                    return print('car has been remove')
                elif car_obj in self.car_elctric_list:
                    self.car_hybrid_list.remove(car_obj)
                    self.all_cars.remove(car_obj)
                    return print('car has been remove')
        return print('Car not found')

    def display_specific_car(self,id:int)->None:
        for car in self.all_cars:
            if id == car.id_car:
                return print(car.car_info())
        return print('Car not found')

    def display_all_gas_cars(self)->None:
        if len(self.car_gas_list) == 0:
            return print('no gas car where founded')
        for car in self.car_gas_list:
            print(car.car_info())

    def display_all_electric_cars(self)->None:
        if len(self.car_elctric_list) == 0:
            return print('no electric car where founded')
        for car in self.car_elctric_list:
            print(car.car_info())

    def display_all_hybrid_cars(self)->None:
        if len(self.car_hybrid_list) == 0:
            return print('no hybrid car where founded')
        for car in self.car_hybrid_list:
            print(car.car_info())

    def display_cars_by_color(self, color:str)->None:
        valid_check:int = 0
        for car in self.all_cars:
            if car.color == color:
                valid_check = 1
                print(car.car_info())
        if valid_check:
            return print('all cars info by color is display')
        else:
            return print('car not found')

    def display_cars_by_year(self, year:int)->None:
        valid_check:int = 0
        for car in self.all_cars:
            if car.year_of_prod > year:
                valid_check = 1
                print(car.car_info())
        if valid_check:
            return print('all cars info by year is display')
        else:
            return print('car not found')
