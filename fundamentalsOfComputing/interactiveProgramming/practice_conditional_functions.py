def triangle_area(base, height):
    """
    function to return a triangle's area as a function of measurement inputs
    """
    area = 0.5 * base * height
    return area
area = triangle_area(4,2) #returns area, so this is the variable that the output must be assigned to to view results
print(area)
area = triangle_area(12,4)
print(area)


def is_claire(name):
    """
    program to return whether person is "Claire"
    """
    if name == "Claire": 
        return "Found that ho!"
    else:
        return "I can't find her!"

present = is_claire("Claire") #returns a string, so setting any variable equal to that string will do (ie present or name)
print(present)
name = is_claire("Jeremy God Damn Peterson") 
print(name)
