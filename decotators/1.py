def my_decorator(func):
    """Decorator function"""

    def wrapper():
        """Return string F_I_B_O_N_A_C_C_I"""
        return "F_I_B_O_N_A_C_C_I"

    return wrapper


@my_decorator
def pfib():
    """Return Fibonacci"""
    return 'Fibonacci'


print(pfib())
