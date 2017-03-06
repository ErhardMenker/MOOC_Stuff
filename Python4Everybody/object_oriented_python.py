## Intro to OOP
# An object is a bit of self-contained Code and Data.
# Unlike functions, objects don't have separate data for every instance of the function.
# Objects have boundaries and characteristics allowing un-needed detail to be ignored.
# The abstraction of OOP allows for hiding complexity of the underlying computational process.
# Strings, integers, dictionaries, and lists are all examples of objects.

## Terminology
# Classes are templates to which different object types can belong.
# Methods/messages are functions/capabilities that operate particularly to an object, as defined by its class.
# Fields/attributes are bits of data in a class (an object's length).
# The object/instance is an actual programming entity belonging to a class.
# The notation for calling a method of an instance is: 'instance.method()'
# In Python, the 'self' parameter is the instance of the object when the object of that class is created.

# The dir() function called on an object lists all of the methods/attributes available to that object's class.

## Object Example
# Class is called "PartyAnimal"
class PartyAnimal:

    x = 0
    # Creation of the "self" instance for any instances of this class
    def party(self):
        self.x = self.x + 1
        print("So far", self.x)

# an is an instance/object of PartyAnimal() class
an = PartyAnimal()
an.party()
an.party()
an.party()

## Object Lifecycle
# Multiple independent instances of an object can exist at once.
# Objects are created, used, and discarded.
# The constructor sets up some instance variables so proper initial variables exist when an object is created (commonly used).
# These are created using the '__init__(self,...)' notation.
# Constructors can have additional parameters that must be specified at later creation of instances of that class.

class PartyAnimal:
    x = 0
    name = ""
    def __init__(self, z):
        self.name = z
        print(self.name, "constructed")
        
    def party(self):
        self.x = self.x + 1
        print (self.name, "party count", self.x)
        
s = PartyAnimal("Sally")
s.party()

j = PartyAnimal("Jim")
j.party()
s.party()

# Destructors run when an object ceases to exist (rarely used)
# Destructors are created using the '__del__(self,...)' notation.

## Inheritance
# Inheritance is the use of creating additional attributes from an already existing class into a new one.
# Therefore, inherited classes extend the classes they inherited from.

# Create FootballFan class that inherits from the PartyAnimal class.
class FootballFan(PartyAnimal):
    points = 0
    def touchdown(self):
        self.points += 7
        self.party()
