### Breadth-First Search (BFS)

## BFS Motivation
# In solving the "small world problem," the brute-force algorithm is true and reasonable but cannot be executed over large networks because of...
# ...explosive computational growth as the number of nodes in the graph increases.
# Let dj be the distance between nodes 0 and j. BFS begins by looking at node 0 and looking at its neighbors which have distance 1, then labelin...
# ...as distance 2 all of the neighbors of node 0's neighbor, and so on...
# BFS processes nodes in a queue by accessing an element at the queue's head and analyzing its neighbors.
# BFS looping structure must be done via queue because of the sequential ordering of distance, as the outward search from the origin occurs we want...
# ...to make sure that all nodes of the closest distance have been searched.
# The elements of the queue are the neighbors of a node yet to be analyzed.
# Breadth-First search should initialize all of the distances to infinity and then iteratively find them.
# Nodes that are not reachable from node 0 will end up with infinity being returned.

## BFS Pseudocode
# Initialize Q to an empty queue
# Set all nodes in the graph equal to infinity
# Set the distance of the node of interest to itself equal to zero
# Enqueue node i (node of interest just initialized to zero)
# While Q is not empty queue do:
#	Dequeue node j from Q
#	for each neighbor h of j do:
#		if node h's distance from i is infinity do:
#			node h's neighbor's distance to i is one greater than node j's distance to id
#			enqueue node h in Q
# Return graph's dict representation

# Note that in the above pseudocode, if arbitrary node has no path to i, then it never loses its distance initialization of infinity.

## BFS Efficiency
# Successful execution of BFS requires an adjacency list/matrix in order to discern a node's neighbors.
# Loose asymptotic analysis shows that: BFS = O(n^2) for node amount n which is quite efficient, this algorithm runs in quadratic by nodes... 
# ...This comes from the fact that in the worst computational scenario, every node is connected to all other nodes so all n nodes operate on all n nodes.
# Tight analysis shows that: BFS = O(n + m) for number of edges m, since an extra edge must only be searched for in one additional operation.
# BFS can also be used to calculate all pairwise distances, but this is a cubic operation in the worst case scenario (since BFS on one node is squared,...
# ...but this is cubic since it is for all of these nodes instead of just one).