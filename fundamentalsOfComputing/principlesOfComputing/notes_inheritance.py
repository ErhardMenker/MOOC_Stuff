### Inheritance

# Classes can inherit methods and attributes from other more abstract/broader classes.
# Example: create a chess piece class that has a method returning a piece color, and then have actual piece type classes...
# ...that inherit that method of "chess piece" and also has methods returning the correct moves based on what type of piece it is per that subclass.
# Python allows ducktyping, meaning that as long as a method called on a class is defined, Python will execute that method.
# Inputting as an argument into a class the name of another class causes the newly defined class to inherit the structures of the inputted class.
# If a method in the inheriting class is redefined from the mother class, then the method is succesfully recreated to follow the new definition.
# In an inheriting class, the __method__ in the mother class needs to be redefined.

# Simple inheritance

# create mother Base class
class Base:
    def hello(self):
        print "hello"
        
    def message(self, msg):
        print msg
 
# create child Sub class inheriting Base 
class Sub(Base):
    def message(self, msg):
        print "sub:", msg
        
# create instance of Base class
baseobj = Base()
# prints "hello" as defined in the Base class
baseobj.hello()
# prints "sub:" <message> instead of just <message> because method was redefined in Sub class creation
baseobj.message("another message")


"""
Simple example of using inheritance.
"""

class Base:
    """
    Simple base class.
    """    
    def __init__(self, num):
        self._number = num

    def __str__(self):
        """
        Return human readable string.
        """
        return str(self._number)
        
class Sub(Base):
    """
    Simple sub class.
    """
    def __init__(self, num):
        pass
    
obj = Sub(42)
print obj

