# Python Object Oriented Programming by Joe Marini course example
# Using instance methods and attributes


class Book:
    # the "init" function is called when the instance is
    # created and ready to be initialized
    def __init__(self, title, author, pages, price):
        self.title = title
        # TODO: add properties
        self.author = author
        self.pages = pages
        self.price = price
        self.__secret = "This is a secret attribute"

    # TODO: create instance methods
    def get_price(self):
        if hasattr(self, "_discount_"):
            return self.price - (self._discount_ * self.price)
        else:
            return self.price
        return self.price

    def setdiscount(self, amount):
        self._discount_ = amount


# TODO: create some book instances
b1 = Book("War and Peace", "Leo Tolstoy", 1225, 39.95)
b2 = Book("The Catcher in the Rye", "JD Salinger", 234, 29.95)

# TODO: print the price of book1
print(b1.get_price())

# TODO: try setting the discount
print(b2.get_price())
b2.setdiscount(0.25)
print(b2.get_price())


# TODO: properties with double underscores are hidden by the interpreter
print(b2._Book__secret) # To use secret attr we need to use the <_class name> before that __attr
