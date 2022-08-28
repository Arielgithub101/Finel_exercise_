from typing import Callable, Any


def deco_1_call_func_twice(func: Callable) -> Callable:
    def inner(*parms, **dict_parms):
        print("The purpose of the decorator is to call the function twice")
        func(*parms, **dict_parms)
        func(*parms, **dict_parms)
        print("The call of this func has ended ")

    return inner


def deco_2_booksList_check(func: Callable) -> Callable:
    def inner(*parms, **dict_parms):
        print("The purpose of the decorator is to check if given list in func is not empty")
        if len(parms[0]) > 0:
            print('good , list not empty ->> colling the func.....')
            func(*parms, **dict_parms)
        else:
            raise ValueError('the length os the list is empty')

    return inner


def deco_3_printer(func: Callable) -> Callable:
    def inner(*parms, **dict_parms):
        print("The purpose of the decorator is to print return value of func ")
        values = func(*parms, **dict_parms)
        if values:
            print('good , values is not none ->> colling the func')
            print(func(*parms, **dict_parms))

    return inner


def deco_4_factory_type_check(type: Any) -> Callable:
    def teyp_check(func: Callable):
        def inner(*parms):
            if isinstance(*parms, type):
                return func(*parms)
            else:
                print("Bad Type")

        return inner

    return teyp_check


if __name__ == "__main__":

    # from website https://teclado.com/30-days-of-python/python-30-day-29-exercise-solutions/


    @deco_1_call_func_twice
    def try_deco_1(a, b):
        print(f'this func try -> {a} + {b} = {a + b}')


    try_deco_1(4, 5)

    book = [1, 2, 3]
    print('---------------------------------------------------')


    @deco_2_booksList_check
    def try_deco_2(my_list):
        print(f'this func show list -> {my_list}')


    try_deco_2(book)

    print('---------------------------------------------------')


    @deco_3_printer
    def try_deco_3(a, b):
        print(f'returen values of this func is -> {a + b})')


    try_deco_3(1, 2)

    print('---------------------------------------------------')


# Ex from website https://www.learnpython.org/en/Decorators

    @deco_4_factory_type_check(int)
    def try_deco_4(num):
        return num


    print(try_deco_4(6))
