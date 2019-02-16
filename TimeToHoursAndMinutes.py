def CalculateHourMinute(timeInMinutes):
    """ (int) -> int, int
    Return how many hours and minutes in timeInMinutes.
    >>> h, m = CalculateHourMinute(150)
    >>> print(h, m)
    >>> h, m = CalculateHourMinute(120)
    >>> print(h, m)
    >>> h, m = CalculateHourMinute(200)
    >>> print(h, m)
    >>> h, m = CalculateHourMinute(30)
    >>> print(h, m)
    """
    minutesPerHour = 60 
    hours = int(timeInMinutes // minutesPerHour)
    minutes = timeInMinutes % minutesPerHour
    time = (hours, minutes)
    return time
    
    
