from dimension_validate import *

def square_perimeter(side):
    """
    'square_perimeter' calculates a square's perimeter given a side length:
    >>> square_perimeter(4)
    16

    :param side: the side length
    :return: the perimeter (same units as side length)
    """
    if (dim_validate(side)):
        return 4*side
    else:
        raise ValueError("side is less than 0: "+side)
