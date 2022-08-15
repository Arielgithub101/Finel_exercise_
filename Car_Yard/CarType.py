from enum import Enum,unique

@unique
class CarTypes(Enum):
    gas = 1
    electric = 2
    hybrid = 3
