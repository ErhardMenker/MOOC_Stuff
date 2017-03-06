""" Create Function to calculate distance from a point to the closest edge of a circle with radius r and center c """

# Initialize Globals

p = [4, 7]
c = [2, 9]
r = 2


# Define function
import math
def distance_nearest(p, c, r):
    val = math.sqrt((p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2) - r
    return val
    
print(distance_nearest(p,c,r))