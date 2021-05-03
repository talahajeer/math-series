def fibonacci(n):
    """
    The function should return the nth value in the fibonacci series.
    """
    return sum_series(n)


def lucas(n):
    """
    The function should return the nth value in the lucas series.
    """
    return sum_series(n,2,1)


def sum_series(n,x=0,y=1):
    if n>= 0:
        if n == 0:
            return x
        elif n == 1:
            return y
        else:
            return sum_series(n-1,x,y) + sum_series(n-2,x,y)
    else:
        return "Negative num is not allowed"               