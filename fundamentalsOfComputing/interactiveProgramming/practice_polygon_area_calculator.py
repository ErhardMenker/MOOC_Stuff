import math
def polygon_area(side_number, side_length):
    area = ((1.0/4.0)*side_number*side_length**2)/math.tan(math.pi/side_number)
    return area
value_1 = polygon_area(5, 7)
value_2 = polygon_area(7, 3)
print ("sample comparison value is", value_1)
print ("actual quiz value is ", value_2)