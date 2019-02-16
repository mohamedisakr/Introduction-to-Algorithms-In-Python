def IsPalindrome(word):
    """ (str) -> bool

    Return True if and only if word is a palindrome.

    >>> IsPalindrome('2002')
    True
    >>> IsPalindrome('0220')
    True
    >>> IsPalindrome('10401')
    True    
    """

    return word == word[::-1];
