from CarYardClass import CarYard
from CarClass import Car
from GasClass import Gas
from ElectricClass import Electric
from HybridClass import Hybrid
from enum import Enum


def display_menu(obj: CarYard) -> None:
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
        user_choice: int = int(input("please enter numbrer of choice action -- > :"))
        match user_choice:
            case 1:
                print('enter your car info ---> ')
                user_choice_type = int(input('enter your choice for car type --> gas = 1/electric = 2/hybrid = 3 : '))
                price: int = int(input('please enter car price : '))
                year_of_prod: int = int(input('please enter car year_of_prod : '))
                mile: int = int(input('please enter mile of the car : '))
                color: str = input('please enter car color : ')
                company: str = input('please enter car company : ')
                id_plate: int = int(input('please enter License plate for the car : '))
                if user_choice_type == 1:
                    new_car = Gas(price, year_of_prod, mile, color, company, id_plate)
                    obj.add_car(new_car)
                elif user_choice_type == 2:
                    new_car = Electric(price, year_of_prod, mile, color, company, id_plate)
                    obj.add_car(new_car)
                elif user_choice_type == 3:
                    new_car = Hybrid(price, year_of_prod, mile, color, company, id_plate)
                    obj.add_car(new_car)
                else:
                    print('Car type not available at the moment')
                flag: str = input('would you like to do anther action ? ---> y/n : ')

            case 2:
                user_input: int = int(input("please enter id number -- > : "))
                obj.remove_car(user_input)
                flag: str = input('would you like to do anther action ? ---> y/n : ')

            case 3:
                user_input: int = int(input("please enter id number -- > : "))
                obj.display_specific_car(user_input)
                flag: str = input('would you like to do anther action ? ---> y/n : ')

            case 4:
                obj.display_all_gas_car()
                flag: str = input('would you like to do anther action ? ---> y/n : ')

            case 5:
                obj.display_all_electric_cars()
                flag: str = input('would you like to do anther action ? ---> y/n : ')

            case 6:
                obj.display_all_hybrid_cars()
                flag: str = input('would you like to do anther action ? ---> y/n : ')

            case 7:
                user_input: str = input("please enter color  -- > : ")
                obj.display_cars_by_color(user_input)
                flag: str = input('would you like to do anther action ? ---> y/n : ')

            case 8:
                user_input: int = int(input("please enter year -- > : "))
                obj.display_cars_by_year(user_input)
                flag: str = input('would you like to do anther action ? ---> y/n : ')

            case 9:
                print("thank you ! good by")
                flag = 'n'

            case _:
                print("invalid option,try again")


print("------------ welcome to the Car yard !! --------")
start = CarYard()
display_menu(start)
