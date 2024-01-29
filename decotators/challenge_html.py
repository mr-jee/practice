from functools import wraps


def bold(func):
    """Bold Decorator"""

    @wraps(func)
    def wrapper():
        """Return HTML Bold Tags"""
        result = '<b>' + func() + '</b>'
        return result

    return wrapper


def italic(func):
    """Italic Decorator"""

    @wraps(func)
    def wrapper():
        """Return HTML italic Tags"""
        result = '<i>' + func() + '</i>'
        return result

    return wrapper



@bold
@italic
def printfib():
    '''return Fibonacci'''
    return 'Fibonacci'


print(printfib())
