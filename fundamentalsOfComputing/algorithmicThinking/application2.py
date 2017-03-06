'''
Application Analyzing Graph Resilience
'''

# general imports
import urllib2
import random
import time
import math
from matplotlib import pyplot as plt
import sys

'''
Source in Homework 2 Functions
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
            if elem in unvisit:
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
    # print "attack_order:", attack_order
    
    # iterate through the nodes to be removed and append the new max connect to connect_idx
    count = 0 
    for rm_node in attack_order:
        #print "rm_node: ", rm_node
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
        
        count += 1
        print "node", count, "removed"
    
    # return the list of the largest connection of nodes after all iterations
    return connect_idx
 
 
"""
Provided code for Application portion of Module 2
"""

##########################################################
# Code for loading computer network graph

NETWORK_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_rf7.txt"
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
    
    
'''
Question 1 - 2
'''

# ER algorithm
def make_complete_graph(num_nodes, prob):
    
    ''' 
    this is a function that, for a given number of nodes, creates an undirected graph where... 
    ...all nodes are connected to one another with probability prob
    '''
    
    #initialize a dictionary where all the nodes map to all other nodes
    graph = dict()
    
    #loop through all node i possibilities 
    for node_i in range(num_nodes):
        #initialize this dictionary entry to the empty set
        graph[node_i] = set([])
        #initialize a set of nodes that node i can legally map to
        edges_of_i = set({})
        
        # loop through all node j possibilities
        for node_j in range(num_nodes):
            # loops are not allowed to self connect
            if node_i == node_j:
                continue
            # append it to the set of nodes that can be mapped to node i with given probability and if not in the set i
            elif (random.uniform(0, 1) < prob) and ((node_i < node_j) or (node_i not in graph[node_j])):
                edges_of_i.add(node_j) 
        
        #after all potential nodes that can be mapped to i are iterated through, finalize the dictionary entry for node id
        graph[node_i] = edges_of_i
        
    return graph
    
    
# UPA algorithm
class UPATrial:
    """
    Simple class to encapsulate optimizated trials for the UPA algorithm
    
    Maintains a list of node numbers with multiple instance of each number.
    The number of instances of each node number are
    in the same proportion as the desired probabilities
    
    Uses random.choice() to select a node number from this list for each trial.
    """

    def __init__(self, num_nodes):
        """
        Initialize a UPATrial object corresponding to a 
        complete graph with num_nodes nodes
        
        Note the initial list of node numbers has num_nodes copies of
        each node number
        """
        self._num_nodes = num_nodes
        self._node_numbers = [node for node in range(num_nodes) for dummy_idx in range(num_nodes)]


    def run_trial(self, num_nodes):
        """
        Conduct num_nodes trials using by applying random.choice()
        to the list of node numbers
        
        Updates the list of node numbers so that each node number
        appears in correct ratio
        
        Returns:
        Set of nodes
        """
        
        # compute the neighbors for the newly-created node
        new_node_neighbors = set()
        for _ in range(num_nodes):
            new_node_neighbors.add(random.choice(self._node_numbers))
        
        # update the list of node numbers so that each node number 
        # appears in the correct ratio
        self._node_numbers.append(self._num_nodes)
        for dummy_idx in range(len(new_node_neighbors)):
            self._node_numbers.append(self._num_nodes)
        self._node_numbers.extend(list(new_node_neighbors))
        
        #update the number of nodes
        self._num_nodes += 1
        return new_node_neighbors


def create_UPA(n, m):
    '''
    function to create UPA graphs
    '''
    # initialize a completed graph from nodes 0 to m - 1
    core_graph = make_complete_graph(m, 1)
    # initialize the remaining nodes
    for node in range(m, n):
        core_graph[node] = set([])
        
    #fill in the remaining nodes
    upa_inst = UPATrial(m)
    for nodes in range(m, n):
        upa_trial = upa_inst.run_trial(m)
        core_graph[nodes] = upa_trial
        for old_node in upa_trial:
            core_graph[old_node].add(nodes)
    return core_graph

       
# helper function to return a random attack order for the graph
def random_order(graph):
    '''
    this function returns the nodes in a graph in a random order
    '''
    # initialize a list to place the nodes
    my_nodes = list()
    # tack each node of the graph onto a list
    for node in graph:
        my_nodes.append(node)
    # shuffle this list of nodes
    random.shuffle(my_nodes)
    return my_nodes
    
    
def plot_resilience():
    '''
    function to plot resilience of computer network, ER, and UPA on one graph
    '''
    print "calculate network resilience"
    # network resilience
    ntwrk_resil = compute_resilience(load_graph(NETWORK_URL), random_order(load_graph(NETWORK_URL)))
    
    print "calculate ER resilience"
    # er resilience
    er_graph = make_complete_graph(1239, .004)
    er_resil = compute_resilience(er_graph, random_order(er_graph))
    
    print "calculate UPA resilience"
    # upa resilience
    upa_graph = create_UPA(1239, 3)
    upa_resil = compute_resilience(upa_graph, random_order(upa_graph))
    
    # list of x coordinates
    x_coords = range(1, len(ntwrk_resil) + 1)
    
    # create the plot
    plt.plot(x_coords, ntwrk_resil, label="Network Data")
    plt.plot(x_coords, er_resil, label = "ER Graph with p = .004")
    plt.plot(x_coords, upa_resil, label = "UPA Graph with m = 3")
    plt.title("Network Resilience for Different Graphs")
    plt.xlabel("Number of Nodes Removed")
    plt.ylabel("Largest Connected Component (Resilience)")
    
    plt.legend()
    plt.show()
    
#plot_resilience()

'''
Question 3
'''

############################################
# Provided code

def copy_graph(graph):
    """
    Make a copy of a graph
    """
    new_graph = {}
    for node in graph:
        new_graph[node] = set(graph[node])
    return new_graph

def delete_node(ugraph, node):
    """
    Delete a node from an undirected graph
    """
    neighbors = ugraph[node]
    ugraph.pop(node)
    for neighbor in neighbors:
        ugraph[neighbor].remove(node)
    
def targeted_order(ugraph):

	'''
	calculate the nodes from largest to smallest for quick attack
	'''
	
	# initialize a dictionary of possible degrees to be filled in
	degree_dist = dict()
	
	# initialize the values of the degree_dist to empty sets
	for idx in range(len(ugraph)):
		degree_dist[idx] = set([])
	
	# fill in the sets
	for node in ugraph:
		degree_tot = len(ugraph[node])
		degree_dist[degree_tot] = degree_dist[degree_tot].union(set([node]))
	# reverse the order from most connected to least and place in a list
	degree_list = sorted(degree_dist, reverse = True)
	
	order = list()
	# fill in the attack list
	for deg in degree_list:
		for node in degree_dist[deg]:
			order.append(node)
	
	return order
    
def undirected_degree(ugraph, node):
    '''
    helper function to calculate the degree of a node in a graph
    '''
    # count the nodes listed as that node's neighbor (way 1)
    count = len(ugraph[node])
    # go through the remaining nodes and see if node is connected to it (way 2)
    for iter_node in ugraph:
        if (iter_node != node) and (iter_node not in ugraph[node]) and (node in ugraph[iter_node]):
            count += 1
            
    return count
    
    
def fast_targeted_order(ugraph):
    '''
    the same as targeted_order(ugraph) but computationally faster
    '''
    DegreeSets = dict()
    for k in range(len(ugraph)):
        DegreeSets[k] = set([])
    for i in range(len(ugraph)):
        d = undirected_degree(ugraph, ugraph[i])
        DegreeSets[d] = DegreeSets[d].union(set([i]))
    L = list()
    for k in sorted(range(len(ugraph)), reverse=True):
        while DegreeSets[k] != set([]):
            u = random.sample(DegreeSets[k], 1)
            DegreeSets[k] = DegreeSets[k].difference(u)
            for elem in u:
                u = elem # convert one element list to numeric
            for v in ugraph[u]:
                d = undirected_degree(ugraph, ugraph[v])
                DegreeSets[d] = DegreeSets[d].difference(set([v]))
                DegreeSets[d - 1] = DegreeSets[d - 1].union(set([v]))
            L.append(u)
            delete_node(ugraph, u)

    return L

    
def plot_targets():
    '''
    function to plot run time of fast_targeted_order vs targeted_order
    '''
    (y_slow, y_fast) = (list(), list())
    # execute the targeting algorithms with inputs from 10 to 990, step 10
    for n in range(10, 1000, 10):
        print "n:", n
       
        #fast calculation
        # t_fast0 = time.time()
        # targeted_order(create_UPA(n, 5))
        # y_fast.append(time.time() - t_fast0)
       
        # slow calculation
        t_slow0 = time.time()
        targeted_order(create_UPA(n, 5))
        print time.time() - t_slow0
        y_slow.append(time.time() - t_slow0)
        
    #create the plot
    plt.plot(range(10, 1000, 10), y_slow, label="targeted_order")
    #plt.plot(range(10, 1000, 10), y_fast, label="fast_targeted_order")
    plt.title("Largest Connected Node Algorithms (Desktop Python)")
    plt.xlabel("Size of Input Graph")
    plt.ylabel("Run Time (Seconds)")
    
    plt.legend()
    plt.show()

plot_targets()


def plot_targeted_resilience():
    '''
    function to plot resilience of computer network, ER, and UPA on one graph
    '''
    print "calculate network resilience"
    # network resilience
    ntwrk_resil = compute_resilience(load_graph(NETWORK_URL), targeted_order(load_graph(NETWORK_URL)))
    
    print "calculate ER resilience"
    # er resilience
    er_graph = make_complete_graph(1239, .004)
    er_resil = compute_resilience(er_graph, targeted_order(er_graph))
    
    print "calculate UPA resilience"
    # upa resilience
    upa_graph = create_UPA(1239, 3)
    upa_resil = compute_resilience(upa_graph, targeted_order(upa_graph))
    
    # list of x coordinates
    x_coords = range(1, len(ntwrk_resil) + 1)
    
    # create the plot
    plt.plot(x_coords, ntwrk_resil, label="Network Data")
    plt.plot(x_coords, er_resil, label = "ER Graph with p = .004")
    plt.plot(x_coords, upa_resil, label = "UPA Graph with m = 3")
    plt.title("Targeted Network Resilience for Different Graphs")
    plt.xlabel("Number of Nodes Removed")
    plt.ylabel("Largest Connected Component (Resilience)")
    
    plt.legend()
    plt.show()
    
#plot_targeted_resilience()




