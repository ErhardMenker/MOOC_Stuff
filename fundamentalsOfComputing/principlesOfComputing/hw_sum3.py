def appendsums(lst): 
    """ 
    Repeatedly append the sum of the current last three elements 
    of lst to lst. 
    """
    for i in range(25):
        lst_work = lst
        lst_sub = lst_work[len(lst) - 3:]
        summation = sum(lst_sub)
        lst_work.append(summation)
    return sum(lst_sub)

sum_three = [0, 1, 2]
appendsums(sum_three)
print sum_three[20]