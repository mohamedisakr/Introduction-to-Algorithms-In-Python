def GetNextEven(odd):
    """ (int) -> int

    Return the even number next to the odd number (parameter).

    >>> GetNextEven(7)
    8
    >>> GetNextEven(3)
    4
    >>> GetNextEven(17)
    18
    >>> GetNextEven(31)
    32
    """
    if odd % 2 != 0 : 
        nextEven = odd + 1
    return nextEven
