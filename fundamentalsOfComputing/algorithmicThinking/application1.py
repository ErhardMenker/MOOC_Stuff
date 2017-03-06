'''
This application analyzes theoretical physics paper citations in graph form
'''

"""
Provided code for Application portion of Module 1

Imports physics citation graph 
"""

#import modules
import urllib2
import matplotlib.pyplot as plt

#########################################################################################
# Code for loading citation graph

CITATION_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_phys-cite.txt"

def load_graph(graph_url):
    """
    Function that loads a graph given the URL
    for a text representation of the graph
    
    Returns a dictionary that models a graph
    """
    graph_file = urllib2.urlopen(graph_url)
    graph_text = graph_file.read()
    graph_lines = graph_text.split('\n')
    graph_lines = graph_lines[ : -1]
    
    print "Loaded graph with", len(graph_lines), "nodes"
    
    answer_graph = {}
    for line in graph_lines:
        neighbors = line.split(' ')
        node = int(neighbors[0])
        answer_graph[node] = set([])
        for neighbor in neighbors[1 : -1]:
            answer_graph[node].add(int(neighbor))

    return answer_graph

citation_graph = load_graph(CITATION_URL)

#########################################################################################

#########################################################################################

'''
Question 1: Create a normalized in degree distribution and plot it log log
'''

# Compute_In_Degrees() helper function
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
	

# create an unnormalized in-degree distribution
def in_degree_distribution(digraph):
	
	'''
	function that maps a directed graph represented as a dictionary called digraph and creates a dictionary creating the unnormalized degree distribution
	'''
	
	#create a dictionary showing how many in_degrees there are for an arbitrary node using compute_in_degrees() helper function
	in_degrees = compute_in_degrees(digraph)
	
	#initialize an output dictionary showing how many in degrees each node has
	unnorm_dist = dict()
	
	#loop through the keys of the in_degrees dictionary
	for val in in_degrees.itervalues():
		#iterate the my_dict entry by 1 (either the previous value or 0 if this degree in the distribution has not been iterated through yet)
		unnorm_dist[val] = unnorm_dist.get(val, 0) + 1
		
	#remove zero node entry from the dictionary
	if 0 in unnorm_dist:
		del unnorm_dist[0]
		
	return unnorm_dist
	
print in_degree_distribution(citation_graph)


# create a normalized in-degree distribution
def norm_in_degree_distribution(digraph):
	
	'''
	function that normalizes an unnormalized degree distribution
	'''
	
	#calculate unnormalized distribution
	unnorm_dist = in_degree_distribution(digraph)
	
	#initialize an accumulator
	tot = 0
	#sum up how many nodes total have in-degree >= 1
	for count in unnorm_dist.itervalues():
		tot += count
	
	#initialize a normalized dictionary
	norm_dist = dict()
	
	for key, val in unnorm_dist.items():
		#normalize how many nodes have a given length 
		val /= float(tot)
		norm_dist[key] = val

	return norm_dist

	
norm_dist = norm_in_degree_distribution(citation_graph)

'''
plot this normalized edge distribution
'''

def plot_norm(norm_dist):

	#initialize the x and y axes to be filled
	x_axis = list()
	y_axis = list()

	#extract the dictionary key-value pairs and put them in x and y axis lists, respectively
	for key, val in norm_dist.items():
		x_axis.append(key)
		y_axis.append(val)

	#scale the x and y axes as log scales
	plt.yscale('log')
	plt.xscale('log')	
	#plot these series
	plt.plot(x_axis, y_axis)

	#input the title and x_axis/y_axis values
	plt.title('Citation Log-Log Normalized Distribution of Pairwise Distances')
	plt.xlabel('Node Length Amount')
	plt.ylabel('Node Length Probability')

	#show resulting plot
	plt.show()
	
#print plot_norm(norm_dist)

#########################################################################################

#########################################################################################

'''
Question 2: Analyze the ER Algorithm for directed graphs
'''

import random

def in_degree_er(node_num, p):
	all_outflows = dict()
	for idx_i in range(node_num):
		outflow_i_set = set()
		for idx_j in range(node_num):
			if idx_i == idx_j:
				continue
			else:
				a = random.random()
				if a < p:
					outflow_i_set.add(idx_j)
		all_outflows[idx_i] = outflow_i_set
	
	norm = norm_in_degree_distribution(all_outflows)
	
	print norm
	
	#initialize the x and y axes to be filled
	x_axis = list()
	y_axis = list()

	#extract the dictionary key-value pairs and put them in x and y axis lists, respectively
	for key, val in norm.items():
		x_axis.append(key)
		y_axis.append(val)

	#scale the x and y axes as log scales
	plt.yscale('log')
	plt.xscale('log')
	
	#label the graph
	title = "Log-Log Normalized Distribution of Pairwise Distances for p =" + str(p)
	plt.title(title)
	plt.xlabel('Node Length Amount')
	plt.ylabel('Node Length Probability')	
	
	#plot these series
	plt.plot(x_axis, y_axis)
	
	plt.show()
	

#print "p=0.9:", in_degree_er(1000, 0.9)
#print "p=0.5:", in_degree_er(1000, 0.5)
#print "p=0.1:", in_degree_er(1000, 0.1)
			
#########################################################################################

#########################################################################################'

'''
Question 3: Construct the DPA algorithm
'''

# general imports
import random


class DPATrial:
    """
    Simple class to encapsulate optimized trials for DPA algorithm
    
    Maintains a list of node numbers with multiple instances of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a DPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_node trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that the number of instances of
        each node number is in the same ratio as the desired probabilities
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for dummy_idx in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors

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

#function to create a DPA algorithm plot	
def graph_DPA(m, n):
	
	'''
	create a graph of a dpa algorithm plot
	'''
	
	#create a connected graph at the first m nodes
	core_graph = make_complete_graph(m)
	
	#iterate through the remaining n - m nodes
	for new_node in range(m, n):
		DPA_instance = DPATrial(m)
		#find out which nodes j will connect to the iterated node
		new_connects = DPA_instance.run_trial(m)
		new_set = set({}) 
		for connect in new_connects:
			new_set.add(connect)
		#to the connected graph, add the new entry with the new connections
		core_graph[new_node] = new_set
		#add the node just added to the graph
		print core_graph
		m += 1
		
	norm_dist = norm_in_degree_distribution(core_graph)
	print norm_dist
	return plot_norm(norm_dist)
	
graph_DPA(5, 12000)