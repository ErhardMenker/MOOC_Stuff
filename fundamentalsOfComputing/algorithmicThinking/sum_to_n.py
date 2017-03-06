def sum_to_n(n):
    '''
    recursive function that calculates n + n - 1 + ... + 2 + 1
    '''
    if n >= 2:
        return n + sum_to_n(n - 1)
    else:
        return 1
        
print sum_to_n(4)