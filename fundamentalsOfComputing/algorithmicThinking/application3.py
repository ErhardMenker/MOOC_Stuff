"""
Application 3 - Cluster Analysis
"""

#### Import Cluster class and functions from ./hw3.py

### Cluster Class from Rice

import math

class Cluster:
    """
    Class for creating and merging clusters of counties
    """
    
    def __init__(self, fips_codes, horiz_pos, vert_pos, population, risk):
        """
        Create a cluster based the models a set of counties' data
        """
        self._fips_codes = fips_codes
        self._horiz_center = horiz_pos
        self._vert_center = vert_pos
        self._total_population = population
        self._averaged_risk = risk
        
        
    def __repr__(self):
        """
        String representation assuming the module is "alg_cluster".
        """
        rep = "alg_cluster.Cluster("
        rep += str(self._fips_codes) + ", "
        rep += str(self._horiz_center) + ", "
        rep += str(self._vert_center) + ", "
        rep += str(self._total_population) + ", "
        rep += str(self._averaged_risk) + ")"
        return rep


    def fips_codes(self):
        """
        Get the cluster's set of FIPS codes
        """
        return self._fips_codes
    
    def horiz_center(self):
        """
        Get the averged horizontal center of cluster
        """
        return self._horiz_center
    
    def vert_center(self):
        """
        Get the averaged vertical center of the cluster
        """
        return self._vert_center
    
    def total_population(self):
        """
        Get the total population for the cluster
        """
        return self._total_population
    
    def averaged_risk(self):
        """
        Get the averaged risk for the cluster
        """
        return self._averaged_risk
   
        
    def copy(self):
        """
        Return a copy of a cluster
        """
        copy_cluster = Cluster(set(self._fips_codes), self._horiz_center, self._vert_center,
                               self._total_population, self._averaged_risk)
        return copy_cluster


    def distance(self, other_cluster):
        """
        Compute the Euclidean distance between two clusters
        """
        vert_dist = self._vert_center - other_cluster.vert_center()
        horiz_dist = self._horiz_center - other_cluster.horiz_center()
        return math.sqrt(vert_dist ** 2 + horiz_dist ** 2)
        
    def merge_clusters(self, other_cluster):
        """
        Merge one cluster into another
        The merge uses the relatively populations of each
        cluster in computing a new center and risk
        
        Note that this method mutates self
        """
        if len(other_cluster.fips_codes()) == 0:
            return self
        else:
            self._fips_codes.update(set(other_cluster.fips_codes()))
 
            # compute weights for averaging
            self_weight = float(self._total_population)                        
            other_weight = float(other_cluster.total_population())
            self._total_population = self._total_population + other_cluster.total_population()
            self_weight /= self._total_population
            other_weight /= self._total_population
                    
            # update center and risk using weights
            self._vert_center = self_weight * self._vert_center + other_weight * other_cluster.vert_center()
            self._horiz_center = self_weight * self._horiz_center + other_weight * other_cluster.horiz_center()
            self._averaged_risk = self_weight * self._averaged_risk + other_weight * other_cluster.averaged_risk()
            return self

    def cluster_error(self, data_table):
        """
        Input: data_table is the original table of cancer data used in creating the cluster.
        
        Output: The error as the sum of the square of the distance from each county
        in the cluster to the cluster center (weighted by its population)
        """
        # Build hash table to accelerate error computation
        fips_to_line = {}
        for line_idx in range(len(data_table)):
            line = data_table[line_idx]
            fips_to_line[line[0]] = line_idx
        
        # compute error as weighted squared distance from counties to cluster center
        total_error = 0
        counties = self.fips_codes()
        for county in counties:
            line = data_table[fips_to_line[county]]
            singleton_cluster = Cluster(set([line[0]]), line[1], line[2], line[3], line[4])
            singleton_distance = self.distance(singleton_cluster)
            total_error += (singleton_distance ** 2) * singleton_cluster.total_population()
        return total_error
		
### Closest Pair Functions

def slow_closest_pair(cluster_list):
	'''
	uses brute force to return the index of the two closest points and their distance
	'''
	# initialize the minimum distance to be infinity
	(min_dist, min_i, min_j) = (float("inf"), -1, -1)
	
	# loop through the clusters and find the smallest distance cluster pair
	for idx_i in range(len(cluster_list)):
		for idx_j in range(len(cluster_list)):
			# examine iff cluster i index is less than j index (avoid repeats and identities)
			if idx_i < idx_j: 
				# calculate the distance between the two clusters
				dist = cluster_list[idx_i].distance(cluster_list[idx_j])
				# if the distance is less than the minimum, redefine min_dist and the coordinates
				if dist < min_dist:
					(min_dist, min_i, min_j) = (dist, idx_i, idx_j)
					
	return (min_dist, min_i, min_j)
	

def closest_pair_strip(cluster_list, horiz_center, half_width):
	'''
	finds the index and distance of the closest points whose x-coord is sufficiently close to horiz_center
	'''
	# create an index list of the coordinates that are sufficiently close for the x-coordinate
	close_set = [(idx, cluster_list[idx]) for idx in range(len(cluster_list)) if abs(cluster_list[idx].horiz_center() - horiz_center) < half_width]
	
	# create a copy of the cluster list and sort it by vertical coordinate
	cluster_list_copy = cluster_list[:]
	cluster_list_copy.sort(key = lambda cluster: cluster.vert_center())
	
	sort_idx = list()
	# go through all of the clusters in the sorted cluster list and append the index if to the sorted index list if it met closeness criteria
	for cluster in cluster_list_copy:
		for key_val in close_set:
			if cluster == key_val[1]: 
				sort_idx.append(key_val[0])
			
	# initialize the minimum distance to infinity and the indices to irrational values
	(min_dist, min_i, min_j) = (float("inf"), -1, -1)

	# iteratively find the maximum
	for idx_i in range(len(sort_idx) - 1):
		for idx_j in range(idx_i + 1, min([idx_i + 4, len(sort_idx)])):
			# calculate the distance between the two clusters
			dist = cluster_list[sort_idx[idx_i]].distance(cluster_list[sort_idx[idx_j]])
			# if the distance is less than the minimum, redefine min_dist and the coordinates
			if dist <= min_dist:
				(min_dist, min_i, min_j) = (dist, min(sort_idx[idx_i], sort_idx[idx_j]), max(sort_idx[idx_i], sort_idx[idx_j]))
				
	return (min_dist, min_i, min_j)
			

def fast_closest_pair(cluster_list):
	'''
	calculate the minimum distance and indices from cluster list using divide-and-conquer
	'''
	# use the brute force method to find the closest points if there are no more than 3 clusters in list
	if len(cluster_list) <= 3:
		(min_dist, min_i, min_j) = slow_closest_pair(cluster_list)
	else:
		# cut the cluster list in half and find the minimum distance and indices for each half 
		(dist0, idx_i0, idx_j0) = fast_closest_pair(cluster_list[:len(cluster_list) / 2])
		(dist1, idx_i1, idx_j1) = fast_closest_pair(cluster_list[len(cluster_list) / 2:])
		# find the minimum distance between the two halves and reset the minima values to that half's values
		if dist0 <= dist1:
			(min_dist, min_i, min_j) = (dist0, idx_i0, idx_j0)
		else:
			# if the distance is smaller in the second half, add indices by half list length to rescale indices to refer to the original list
			(min_dist, min_i, min_j) = (dist1, idx_i1 + len(cluster_list) / 2, idx_j1 + len(cluster_list) / 2)
		# see if there are any points that reside on the boundary between the two halves with a smaller distance than anywhere else (min_dist)
		(boundary_dist, boundary_i, boundary_j) = closest_pair_strip(cluster_list, 0.5 * (cluster_list[len(cluster_list) / 2 - 1].horiz_center() + cluster_list[len(cluster_list) / 2].horiz_center()), min_dist)
		# set the minimum distance as the lower distance between the minima of the two halves and the boundary cases from closest_pair_strip()
		if boundary_dist < min_dist:
			(min_dist, min_i, min_j) = (boundary_dist, boundary_i, boundary_j)
			
	return (min_dist, min_i, min_j) 


def hierarchical_clustering(cluster_list, num_clusters):
	'''
	perform hierarchical clustering by placing every element in cluster_list into one of num_clusters clusters.
	'''
	# sort in non-decreasing order of horizontal coordinate
	cluster_list.sort(key = lambda cluster: cluster.horiz_center())
	
	# keep moving coordinates into more condense clusters until the number of clusters equals num_clusters
	while len(cluster_list) > num_clusters:
		#print "cluster length:", len(cluster_list)
		# find the indices in the list of the closest points
		(_, idx_i, idx_j) = fast_closest_pair(cluster_list)
		# merge these two closest clusters
		cluster_list[idx_i].merge_clusters(cluster_list[idx_j])
		# eliminate the sub that was merged into the larger cluster
		cluster_list.pop(idx_j)
		
	return cluster_list


def kmeans_utility(cluster, centers):
	'''
	find the minimum center index to the cluster
	'''
	min = float("inf")
	count = -1
	for center in centers:
		count += 1
		if center.distance(cluster) < min:
			min = center.distance(cluster)
			idx_star = count
			
	return idx_star
	
	
def kmeans_clustering(cluster_list, num_clusters, num_iterations):
	'''
	iteratively execute k-means clustering
	'''
	cluster_list_copy = cluster_list[:]
	# sort the cluster list by population in descending order
	cluster_list_copy.sort(key = lambda cluster: cluster.total_population(), reverse=True)
	# initialize centers to be num_clusters size list with num_clusters largest population clusters
	centers = [cluster_list_copy[idx] for idx in range(num_clusters)]
	
	# iterate through this process num_iterations times
	for _ in range(num_iterations):
		# initialize k clusters to have zero population/FIPS
		new_clstrs = [Cluster(set([]), 0, 0, 0, 0) for _ in range(num_clusters)]

		# find the closest center for each cluster list and append it to the output
		for cluster in cluster_list_copy:
			min_idx = kmeans_utility(cluster, centers)
			new_clstrs[min_idx].merge_clusters(cluster)
			
		# initialize centers to be num_clusters size list with num_clusters largest population clusters
		centers = new_clstrs[:]
	
	return new_clstrs
	

#### Efficiency

import time
import random
from matplotlib import pyplot as plt
import urllib2

def gen_random_clusters(num_clusters):
	'''
	generate num_clusters random clusters in the unit square
	'''
	clstr_output = list()
	for clstr in range(num_clusters):
		clstr_output.append(Cluster(None, random.random(), random.random(), None, None))
	
	return clstr_output

def fast_plot_prep(input_range):
	'''
	create a two element tuple with lists of x and y coords, respectively,
	showing the speed of fast_closest_pair() execution for different input sizes
	'''
	(x_axis, y_axis) = [list(), list()]
	for input in range(input_range[0], input_range[1] + 1):
		# append to the x_axis list the input size
		x_axis.append(input)
		# record the time before execution
		t0 = time.time()
		# execute the function
		fast_closest_pair(gen_random_clusters(input))
		# append the elapsed time to the y_axis
		y_axis.append(time.time() - t0)
		
	return (x_axis, y_axis)
	
def slow_plot_prep(input_range):
	'''
	create a two element tuple with lists of x and y coords, respectively,
	showing the speed of slow_closest_pair() execution for different input sizes
	'''
	(x_axis, y_axis) = [list(), list()]
	for input in range(input_range[0], input_range[1] + 1):
		# append to the x_axis list the input size
		x_axis.append(input)
		# record the time before execution
		t0 = time.time()
		# execute the function
		slow_closest_pair(gen_random_clusters(input))
		# append the elapsed time to the y_axis
		y_axis.append(time.time() - t0)
		
	return (x_axis, y_axis)
	
fast_points = fast_plot_prep((1, 200))
slow_points = slow_plot_prep((1, 200))
plt.plot(fast_points[0], fast_points[1], label="fast_closest_pair")
plt.plot(slow_points[0], slow_points[1], label="slow_closest_pair")
plt.title("Closest Point Run Time Based on Algorithm Size")
plt.xlabel("Cluster Input Size")
plt.ylabel("Running Time (Seconds)")
#plt.legend()
#plt.show()

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table

DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = DIRECTORY + "data_clustering/unifiedCancerData_3108.csv"
DATA_896_URL = DIRECTORY + "data_clustering/unifiedCancerData_896.csv"
DATA_290_URL = DIRECTORY + "data_clustering/unifiedCancerData_290.csv"
DATA_111_URL = DIRECTORY + "data_clustering/unifiedCancerData_111.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = urllib2.urlopen(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    #print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])] 
            for tokens in data_tokens]
			
			
def run_example():
    """
    Load a data table, compute a list of clusters and 
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    data_table = load_data_table(DATA_111_URL)
    
    singleton_list = []
    for line in data_table:
        singleton_list.append(Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
        
    #cluster_list = sequential_clustering(singleton_list, 15)	
    #print "Displaying", len(cluster_list), "sequential clusters"
	
    #cluster_list = hierarchical_clustering(singleton_list, 9)
    #print "Displaying", len(cluster_list), "hierarchical clusters"

    cluster_list = kmeans_clustering(singleton_list, 9, 5)	
    print "Displaying", len(cluster_list), "k-means clusters"
    return cluster_list
	

def compute_distortion(cluster_list, data_url):
    '''
    calculate the distortion for a list of clusters
    '''
    sum = 0
    for cluster in cluster_list:
        sum += cluster.cluster_error(load_data_table(data_url))
    return sum    
        
#print compute_distortion(run_example(), DATA_111_URL)

def plot_distortion(data_url):
    '''
    calculate the hierarchical and k-means distortion for clusters from
    6 through 20 and plot them in a graph
    '''
    data_table = load_data_table(data_url)
    # prep the cluster axes values
    (x_val, y_kmeans_distort, y_hierarch_distort) = (list(), list(), list())
    
    print "hierarchical"
    for clstr_num in range(6, 21):
        print "clstr_num", clstr_num
        singleton_list = []
        # replenish the singleton_list everytime to prevent against iterative mutation
        for line in data_table:
            singleton_list.append(Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
        # append the distortion of the hierarchical clustering for the given cluster number
        y_hierarch_distort.append(compute_distortion(hierarchical_clustering(singleton_list, clstr_num), data_url)) 
    
    # reload the data table and recreate the singleton list
    data_table = load_data_table(data_url)
    singleton_list = []
    for line in data_table:
        singleton_list.append(Cluster(set([line[0]]), line[1], line[2], line[3], line[4]))
    
    print "kmeans"
    for clstr_num in range(6, 21):
        print "clstr_num", clstr_num
        # append the x value (cluster number) for given iteration
        x_val.append(clstr_num)
        # append the distortion of the k-means clustering for the given cluster number
        y_kmeans_distort.append(compute_distortion(kmeans_clustering(singleton_list, clstr_num, 5), data_url))
    
    # plot the resulting values
    plt.close()
    plt.plot(x_val, y_kmeans_distort, label="K-means Clustering")
    plt.plot(x_val, y_hierarch_distort, label="Hierarchical Clustering")
    plt_title = "Cluster Size Impact on Distortion for " + data_url[-7:-4] + " Point Dataset"
    plt.title(plt_title)
    plt.xlabel("Size of Cluster")
    plt.ylabel("Distortion")
    plt.legend()
    plt.show()
       
plot_distortion(DATA_111_URL)    
plot_distortion(DATA_290_URL)
plot_distortion(DATA_896_URL)

	
	
	
	
	
	
	
	
	
	
	