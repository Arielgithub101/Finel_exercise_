from typing import Callable


def deco_1(func: Callable) -> Callable:
    def inner(*parms, **dict_parms):
        print("The purpose of the decorator is to call the function twice")
        func(*parms, **dict_parms)
        func(*parms, **dict_parms)
        print("The call of this func has ended ")
    return inner


def deco_2(func: Callable) -> Callable:
    def inner(*parms, **dict_parms):
        print("The purpose of the decorator is to check if guven kust in func is not empty")
        if len(parms[0]) > 0:
            print('good , list not empty ->> colling the func')
            func(*parms, **dict_parms)
        else:
            raise ValueError('the length os the list is empty')
    return inner






if __name__ == "__main__":
    pass