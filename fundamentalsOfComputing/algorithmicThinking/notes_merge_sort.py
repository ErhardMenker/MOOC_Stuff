### MergeSort (Divide and Conquer)

# MergeSort is a sorting algorithm that is O(n*log(n)).
# Divide and conquer keeps breaking down a problem into sub problems and then combines them at the end.

# MergeSort is a divide-and-conquer algorithm that uses recursion to divide by cutting the list into half and sort those halfs by again...
# ...breaking them into two halves until the base case of end nodes of one element lists. The conquering occurs by going back up the tree and...
# ...merging/sorting the child nodes back together by looking at the smallest index of the sub-lists on the way buck up the tree.

# MergeSort's running time is a recurrence, where T(n) = 2 * T(n / 2) + O(n) and T(1) = O(1)
# A recurrence run time must have a finite base case in order to be evaluated.
# Comparison based algorithms cannot beat O(n*log(n))