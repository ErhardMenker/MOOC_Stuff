# Object-oriented program involves treating different classes of objects differently.
# An instance of a certain class is an "object" of that class (in EViews, a vector with random normals is a "vector object")
# Behaviors that can only operate a certain way on a given class are methods.
# Class methods are called using the notation: object_name.method()
# Calling the type() function on a value can make sure that the proper class is being called
# Classes of objects, therefore, have defined methods as follows:

class Character:
    # Note that the "self" (first listed) variable is created automatically
    
    def __init__(self, name, initial_health):
        # map certain class names to values
        self.name = name
        self.health = initial_health
        self.inventory = []
        
    def __str__(self):
        s  = "Name: " + self.name
        s += " Health: " + str(self.health)
        s += " Inventory: " + str(self.inventory)
        return s
    
    # These are different behaviors of Character class:
    
    def grab(self, item):
        self.inventory.append(item)
        
    def get_health(self):
        return self.health
    
def example():
    me = Character("Bob", 20)
    print(str(me))
    me.grab("pencil")
    me.grab("paper")
    print(str(me))
    print("Health:", me.get_health())
    
example()
