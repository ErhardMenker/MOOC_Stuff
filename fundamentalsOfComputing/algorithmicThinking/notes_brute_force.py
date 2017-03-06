###Brute Force

#A brute force is an algorithm that checks every possible case, following directly from the problem's definition.
#A brute force algorithm is easy to understand and implement, but can be computationally inefficient for large data structures.
#To see the length of the distance between two nodes in a graph of k nodes, loop through a length of 1,2,...,(k-1) and see if the graphs are connected at that length.
#Brute force analysis of distance in a graph's case assumes there is a graph A and two designated nodes i and j. The distance is d(i,j).
#The input of a graph in this brute force case is the number of nodes and edges.
#The worst brute force case for a graph search is when the graphs aren't connected. This takes about 13 million searches for a graph with 10 nodes, so brute force fails here for even fast computers for a graph with thousands of nodes.
#The growth of the graph search brute force algorithm is exponential, a doubling of nodes much more than doubles search time.
#The growth of an algorithm explains how an increase in input size increases required executions.
