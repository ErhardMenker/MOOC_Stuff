###Paths and Distances
#Two nodes are connected/neighbors if there are edges that directly connect them.
#The degree of a node in an undirected graph is the number of neighbors it has.
#The in-degree of a node in a directed graph is the number of neighbors flowing in to that node.
#The out-degree of a node in a directed graph is the number of neighbors flowing out of that node.
#Because there are in-degrees and out-degrees of directed graphs, adjacency lists have an extra column than undirected graphs.
#Designated nodes are selected nodes i and j being compared.
#In a graph of k nodes, there is a path of length (k - 1) between designated nodes i and j iff there are k connected nodes that lead from node i to j.
#The distance between two nodes is the smallest amount of edges that connects the two nodes.
#The algorithm that determines the distance is to start with 1,2,...(k - 1) given k nodes, and see if a length n that order can connect the two nodes.
#The small-world problem can be understood as having a graph input and a distribution of pairwise distances output.
#The degree distribution of a graph is the probability distribution that a random connection between two nodes includes that node.  
 