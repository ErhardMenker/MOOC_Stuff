"""
Merge function for 2048 game.
"""

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    copy = list()
    for elem in line:
        copy.append(elem)
    
    for idx in range(len(line) - 1):
        #loop through remaining list and slide over non-zero values:
        for elem in copy[idx:]:
            if elem == 0:
                copy.remove(elem)
                copy.append(elem)
        index_0 = copy[idx]
        index_1 = copy[idx+1]
        #add consecutive equal entries, slide them over:
        if index_0 == index_1:
            copy[idx] = index_0 + index_1
            copy[idx + 1] = 0
           
    return copy