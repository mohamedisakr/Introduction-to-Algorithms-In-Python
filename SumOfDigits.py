def CalculateDigitsSum(number):
    """ (int) -> int

    Return number's digits summation.

    >>> CalculateDigitsSum(2002)
    4
    >>> CalculateDigitsSum(123)
    6
    >>> CalculateDigitsSum(10401)
    6
    >>> CalculateDigitsSum(84001)
    13
    """
    base = 10
    digit = 0
    total = 0
    n = number
    while n > 0:
        digit = n % base
        total += digit
        n //= base
    return total;
