'''
Homework 1: Analyze the Basics of Graph and Brute Force
'''

##########################################################################################################################################################################################

#REPRESENTING DIRECTED GRAPHS

# Graph Instances
EX_GRAPH0 = {0: set({1, 2}), 1: set({}), 2: set({})}
EX_GRAPH1 = {0: set({1, 4, 5}), 1: set({2, 6}), 2: set({3}), 3: set({0}), 4: set({1}), 5: set({2}), 6: set({})}
EX_GRAPH2 = {0: set({1, 4, 5}), 1: set({2, 6}), 2: set({3, 7}), 3: set({7}), 4: set({1}), 5: set({2}), 6: set({}), 7: set({3}), 8: set({1, 2}), 9: set({0, 3, 4, 5, 6, 7})}


# Make_Complete_Graph() 
def make_complete_graph(num_nodes):
	
	''' 
	this is a function that, for a given number of nodes, creates a directed graph where all nodes are connected to one another
	'''
	
	#initialize a dictionary where all the nodes map to all other nodes
	graph = dict()
	
	#loop through all node pair possibilities 
	for node_i in range(num_nodes):
		#initialize a set of nodes that node i can legally map to
		edges_of_i = set({})
		
		for node_j in range(num_nodes):
			#if a node maps to itself, continue to the next iteration since self loops are prohibited
			if node_i == node_j:
				continue
			#if a node does not map to itself, append it to the set of nodes that can be mapped to node i
			else:
				edges_of_i.add(node_j)
		
		#after all potential nodes that can be mapped to i are iterated through, finalize the dictionary entry for node id
		graph[node_i] = edges_of_i
		
	return graph

##########################################################################################################################################################################################

##########################################################################################################################################################################################

# COMPUTING DEGREE DISTRIBUTIONS

# Compute_In_Degrees()
def compute_in_degrees(digraph):

	'''
	take a directed graph represented as a dictionary called digraph and create a dictionary showing how many in degrees exist for that node
	'''
	
	#initialize an output dictionary showing how many in degrees each node has
	my_dict = dict()
	
	#loop through each node (key) and initialize its in-degree value to zero
	for key in digraph:
		my_dict[key] = 0
	
	#iterate through the value set corresponding to every key in the inputted dictionary
	for val_set in digraph.itervalues():
		#go through each node that the iterated node shares an edge mapping out to in the val_set
		for elem in val_set:
			#increment the corresponding element's key by 1
			my_dict[elem] += 1
		
	return my_dict

	
#in_degree_distribution(digraph)
def in_degree_distribution(digraph):
	
	'''
	function that maps a directed graph represented as a dictionary called digraph and creates a dictionary creating the unnormalized degree distribution
	'''
	
	#initialize an output dictionary showing how many in degrees each node has
	my_dict = dict()
	
	#create a dictionary showing how many in_degrees there are for an arbitrary node
	in_degrees = compute_in_degrees(digraph)
	#loop through the keys of the in_degrees dictionary
	for val in in_degrees.itervalues():
		#iterate the my_dict entry by 1 (either the previous value or 0 if this degree in the distribution has not been iterated through yet)
		my_dict[val] = my_dict.get(val, 0) + 1
		
	return my_dict
		
##########################################################################################################################################################################################