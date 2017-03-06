'''
Homework 2: Analyze the BFS Algorithm
'''

##########################################################################################
# PHASE ONE

def bfs_visited(ugraph, start_node):
	
	'''
	take an undirected graph, ugraph, and starting node, start_node, and return all...
	...of the nodes visited by BFS of start_node
	'''
	
	# initialize a queue that begins with the start_node
	queue = [start_node]
	# initialize a visited set whose first element is the start_node
	visited = set([start_node])
	
	# continue to iterate through the queue as long as it is non-empty
	while queue != []:
		# extract the last element in the queue for search of its neighbors
		node_i = queue.pop()
		for neighbor in ugraph[node_i]:
			# add these neighbors to the queue and visited if not in visited set
			if neighbor not in visited:
				visited = visited.union(set([neighbor]))
				queue.insert(0, neighbor)
	
	# return the set of nodes where a finite path exists to node i
	return visited

# Application:
#print bfs_visited({0: set([1]), 1: set([0]), 2: set([])}, 2)

##########################################################################################
# PHASE TWO

def cc_visited(ugraph):

	'''
	return all elements in the graph that are connected
	'''
	
	# none of the points in ugraph have been visited yet; communicate this in a variable
	unvisit = list()
	for node in ugraph:
		unvisit.append(node)
	# initialize an empty list of connected components
	connect = list()
	
	while unvisit != []:
		# extract arbitrary element from unvisit
		node_i = unvisit[0]
		# neighbors is the set of nodes connected to node i
		neighbors = bfs_visited(ugraph, node_i)
		# append the connected nodes to the list of connected nodes
		connect.append(neighbors)
		# remove all of these connected nodes from unvisit
		for elem in neighbors:
			unvisit.remove(elem)

	# return the set of connected nodes
	return connect

	
def largest_cc_size(ugraph):

	'''
	return the size of the largest connected component in ugraph
	'''
	
	# find the island of connected nodes
	connect = cc_visited(ugraph)
	# iterate through and find the count of the largest
	maxm = 0
	for island in connect:
		if len(island) > maxm:
			maxm = len(island)
	
	return maxm
	
	
##########################################################################################
# PHASE THREE

def compute_resilience(ugraph, attack_order):

	'''
	remove nodes one at a time and measure the resilience of ugraph
	'''
	
	# initialize a list where the one entry is the largest CC with no nodes removed
	connect_idx = [largest_cc_size(ugraph)]
	
	# iterate through the nodes to be removed and append the new max connect to connect_idx
	for rm_node in attack_order:
		# create a new dictionary to be filled without the removed nodes
		ugraph_copy = dict()
		
		# append all nodes and edges that don't include the one to be removed
		for node, edges in ugraph.items():
			if node != rm_node:
				ugraph_copy[node] = edges
		
		# iterate through the edges at each node and pop out the node to be removed if it exists
		ugraph_copy1 = ugraph_copy.copy()
		for node, edges in ugraph_copy.items():
			if rm_node in edges:
				ugraph_copy1[node] = edges.difference(set([rm_node]))
			else:
				ugraph_copy1[node] = edges
		
		# convert ugraph to this new dictionary with the attack element completely removed
		ugraph = ugraph_copy1.copy()
		
		# append the list of the most connected nodes to connect_idx
		connect_idx.append(largest_cc_size(ugraph))
	
	# return the list of the largest connection of nodes after all iterations
	return connect_idx
	
	
compute_resilience({0: set([1]), 1: set([0]), 2: set([])}, [1, 2])
