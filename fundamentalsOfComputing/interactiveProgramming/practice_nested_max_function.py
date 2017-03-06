def max_2_numbers(a,b):
    if a >= b:
        max_number = a
    else:
        max_number = b
    return max_number

def max_3_numbers(a,b,c):
    subset = max_2_numbers(b,c)
    output = max_2_numbers(a, subset)
    return output

val = max_3_numbers(1,2,3)
print(val)