"""
Stack class with tests to show how this class operates
"""

class Stack():
    """
    A simple implementation of a FILO stack.
    """

    def __init__(self):
        """ 
        Initialize the stack.
        """
        self._lst = list()

    def __len__(self):
        """
        Return number of items in the stack.
        """
        count = 0
        for elem in self._lst:
            count += 1
        return count

    def __str__(self):
        """
        Returns a string representation of the stack.
        """
        strng = ""
        for elem in self._lst:
            strng = strng + " , " + str(elem)
        return "current stack: " + strng
        

    def push(self, item):
        """
        Push item onto the stack.
        """
        self._lst.append(item)

    def pop(self):
        """
        Pop an item off of the stack
        """
        if len(self._lst) > 0:
            return self._lst.pop(len(self._lst) - 1)

############################
# test code for the stack

my_stack = Stack()
my_stack.push(72)
my_stack.push(59)
my_stack.push(33)
my_stack.pop()
my_stack.push(77)
my_stack.push(13)
my_stack.push(22)
my_stack.push(45)
my_stack.pop()
my_stack.pop()
my_stack.push(22)
my_stack.push(72)
my_stack.pop()
my_stack.push(90)
my_stack.push(67)
while len(my_stack) > 4:
    my_stack.pop()
my_stack.push(32)
my_stack.push(14)
my_stack.pop()
my_stack.push(65)
my_stack.push(87)
my_stack.pop()
my_stack.pop()
my_stack.push(34)
my_stack.push(38)
my_stack.push(29)
my_stack.push(87)
my_stack.pop()
my_stack.pop()
my_stack.pop()
my_stack.pop()
print my_stack
my_stack.pop()
print my_stack
my_stack.pop()
print my_stack.pop()