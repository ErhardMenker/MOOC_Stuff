###Graphs and Representations

#An graph is a collection of nodes and the edges that connect them.
#Formally, "v" is the set of all node elements in the graph, and "e" is the collection of edge pairs.
#If the order of the edge's flow does not matters, the graph is undirected.
#If the order of the edge's flow does matter, the graph is directed.
#In an undirected graph, the order of the edges does not matter. In directed graphs, the order of the edge pairs matters ((a,b) means node a flows to b but does not imply b to a).
#The degree of a node in an undirected graph is how many other nodes that node is directly connected to.
#The in-degree of a node in a directed graph is how many other nodes map to it (inflows) and the out-degree is how many other nodes it maps out to (outflows).
#In Rice algorithmic thinking courses, edges cannot map to themselves (self-loops) nor can multiple of the same edge between nodes exist (parallel edges).
#In a directed graph, if node a flows to b and b flows to a, that is NOT a parallelized edge.
#Representing edges pairs in list "e" can be computationally expensive. Adjacency lists/matrices can reduce this cost.
#An adjacency list lists out each node and all of its adjacent nodes.
#Adjacency lists can be redundant in the case of undirected graphs by listing both connection flows between the same two nodes.
#An adjacency matrix for a graph with n nodes has n rows and n columns, with one row and one column representing a node in the graph.
#Adjacency matrix entries are dichotomous. For a row with node i and a column with node j, the entry is 1 if i and j are connected and 0 if not.
#For an undirected graph, the matrix is symmetric because i and j being connected implies j and i are connected. However, this is not the case for undirected graphs because nodes i and j being connected does not imply j and i are.
#For a directed graph, adjacency matrix entry i,j is 1 if node i outflows to node j.
#If a graph is sparse (there are not many connections), it is better to use an adjacency list because many connections do not need to be listed.
#If a graph is dense (there are many connections), it is better to use an adjacency matrix so all of those connections can be noted by writing 1s instead of rewriting out every connection in the adjacency list. 