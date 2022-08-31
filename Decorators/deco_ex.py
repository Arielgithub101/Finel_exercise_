from typing import Callable, Type,Any


def call_func_twice(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("The purpose of the decorator is to call the function twice")
        func(*args, **kwargs)
        func(*args, **kwargs)
        print("The call of this func has ended ")

    return inner


def list_length_check(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("The purpose of the decorator is to check if given list in func is not empty")
        if args[0]:
            print('good , list not empty ->> colling the func.....')
            func(*args, **kwargs)

    return inner


def printer(func: Callable) -> Callable:
    def inner(*args, **kwargs):
        print("The purpose of the decorator is to print return value of func ")
        values = func(*args, **kwargs)
        if values is not None:
            print('good , values is not none ->> colling the func')
            print(values)

    return inner


def factory_deco(type_var: Type) -> Callable:
    def type_check(func: Callable[[any],any]):
        def inner(a):
            if isinstance(a, type_var):
                return func(a)
            else:
                print("Bad Type")

        return inner

    return type_check


if __name__ == "__main__":
    # from website https://teclado.com/30-days-of-python/python-30-day-29-exercise-solutions/

    @call_func_twice
    def try_deco_1(a, b):
        print(f'this func try -> {a} + {b} = {a + b}')


    try_deco_1(4, 5)

    print('---------------------------------------------------')
    book = [1, 2, 3]


    @list_length_check
    def try_deco_2(my_list):
        print(f'this func show list -> {my_list}')


    try_deco_2(book)

    print('---------------------------------------------------')


    @printer
    def try_deco_3(*args, **kwargs):
        return False


    try_deco_3()

    print('---------------------------------------------------')


    # Ex from website https://www.learnpython.org/en/Decorators

    @factory_deco()
    def try_deco_4(num):
        return num


    print(try_deco_4(4))
