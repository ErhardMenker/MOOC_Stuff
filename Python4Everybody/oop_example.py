class TEST_CLASS():

    # initializer
    def __init__(self, life, mssg):
        self.life = life
        self.mssg = mssg

    def get_life(self):
        return self.life

    def incrm_life(self):
        self.life += 1
        return self.life

    def print_mssg(self):
        return self.mssg

# create test_obj object that is of TEST_CLASS class
test_obj = TEST_CLASS(0, "bland message")

print test_obj # returns that test_obj is of TEST_CLASS class
print test_obj.life # returns: 0
print test_obj.mssg # returns: "bland message"

print test_obj.get_life() # returns 0
print test_obj.incrm_life() # returns 1
print test_obj.incrm_life() # returns 2
print test_obj.get_life() # returns 2

print test_obj.print_mssg() # returns "bland message"