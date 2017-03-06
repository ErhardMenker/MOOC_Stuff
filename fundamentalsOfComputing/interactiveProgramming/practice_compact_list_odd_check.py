""" Outputs a list of a numerical inputted's list even numbers """

def is_even(number):
    """ Returns Boolean corresponding to whether number is even """
    return number % 2 == 0
  
# Initialize practice list to be iterated through:
my_list = [0, 2, 3, 4, 5, 7, 42, 69, 124309, 120981209830]
  
print([number for number in my_list if is_even(number)])