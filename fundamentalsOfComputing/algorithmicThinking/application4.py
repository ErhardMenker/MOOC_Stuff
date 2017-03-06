'''
Application 4: Dynamic Programming
'''

"""
Provide code for Application 4
"""

DESKTOP = True

import math
import random
import urllib2
import matplotlib.pyplot as plt
import re
import string


# URLs for data files
PAM50_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_PAM50.txt"
HUMAN_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_HumanEyelessProtein.txt"
FRUITFLY_EYELESS_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_FruitflyEyelessProtein.txt"
CONSENSUS_PAX_URL = "http://storage.googleapis.com/codeskulptor-alg/alg_ConsensusPAXDomain.txt"
WORD_LIST_URL = "http://storage.googleapis.com/codeskulptor-assets/assets_scrabble_words3.txt"


###############################################
# provided code

def read_scoring_matrix(filename):
    """
    Read a scoring matrix from the file named filename.  

    Argument:
    filename -- name of file containing a scoring matrix

    Returns:
    A dictionary of dictionaries mapping X and Y characters to scores
    """
    scoring_dict = {}
    scoring_file = urllib2.urlopen(filename)
    ykeys = scoring_file.readline()
    ykeychars = ykeys.split()
    for line in scoring_file.readlines():
        vals = line.split()
        xkey = vals.pop(0)
        scoring_dict[xkey] = {}
        for ykey, val in zip(ykeychars, vals):
            scoring_dict[xkey][ykey] = int(val)
    return scoring_dict


def read_protein(filename):
    """
    Read a protein sequence from the file named filename.

    Arguments:
    filename -- name of file containing a protein sequence

    Returns:
    A string representing the protein
    """
    protein_file = urllib2.urlopen(filename)
    protein_seq = protein_file.read()
    protein_seq = protein_seq.rstrip()
    return protein_seq


def read_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    """
    # load assets
    word_file = urllib2.urlopen(filename)
    
    # read in files as string
    words = word_file.read()
    
    # template lines and solution lines list of line string
    word_list = words.split('\n')
    print "Loaded a dictionary with", len(word_list), "words"
    return word_list


'''
Code from Project 4
'''

### Matrix Functions ###

def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    '''
    builds a matrix given the scoring criteria for all possible alignments
    '''
    scoring_matrix = dict()
    alphabet = alphabet.union(set(["-"]))
    # traverse the matrix and fill it in
    for letter_row in alphabet:
        row_dict = dict()
        for letter_col in alphabet:
            # case 2: only of the elements is a dash; dash_score
            if (letter_row == "-") or (letter_col == "-"):
                row_dict[letter_col] = dash_score
            # case 2: the characters are non-dashes and equivalent
            elif letter_row == letter_col:
                row_dict[letter_col] = diag_score
            # case 3: the characters are non-dashes and not equivalent
            else:
                row_dict[letter_col] = off_diag_score
        # append on this new row to the outputted dictionary
        scoring_matrix[letter_row] = row_dict
        
    return scoring_matrix
    
    
def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    '''
    builds an alignment matrix for two sequences seq_x & seq_y
    '''
    # trivial case
    if (len(seq_x) == 0) or (len(seq_y) == 0):
        return [[0]]
    
    alignment_matrix = []
    # set s[0, 0] to 0
    alignment_matrix.append([0])
    
    # fill in the zeroth column
    for idx_i in range(1, len(seq_x) + 1):
        if global_flag:
            alignment_matrix.append([alignment_matrix[idx_i - 1][0] + scoring_matrix[seq_x[idx_i - 1]]["-"]])
        else:
            alignment_matrix.append([max(alignment_matrix[idx_i - 1][0] + scoring_matrix[seq_x[idx_i - 1]]["-"], 0)])
    
    # fill in the zeroth row
    row0 = alignment_matrix[0]
    for idx_j in range(1, len(seq_y) + 1):
        if global_flag: 
            row0.append(alignment_matrix[0][idx_j - 1] + scoring_matrix["-"][seq_y[idx_j - 1]])
        else:
            row0.append(max(alignment_matrix[0][idx_j - 1] + scoring_matrix["-"][seq_y[idx_j - 1]], 0))
    
    # fill in the entries with positive i & j
    for idx_i in range(1, len(seq_x) + 1):
        for idx_j in range(1, len(seq_y) + 1):
            if global_flag:
                alignment_matrix[idx_i].append(max(alignment_matrix[idx_i - 1][idx_j - 1] + scoring_matrix[seq_x[idx_i - 1]][seq_y[idx_j - 1]], alignment_matrix[idx_i - 1][idx_j] + scoring_matrix[seq_x[idx_i - 1]]["-"], alignment_matrix[idx_i][idx_j - 1] + scoring_matrix["-"][seq_y[idx_j - 1]]))
            else:
                alignment_matrix[idx_i].append(max(alignment_matrix[idx_i - 1][idx_j - 1] + scoring_matrix[seq_x[idx_i - 1]][seq_y[idx_j - 1]], alignment_matrix[idx_i - 1][idx_j] + scoring_matrix[seq_x[idx_i - 1]]["-"], alignment_matrix[idx_i][idx_j - 1] + scoring_matrix["-"][seq_y[idx_j - 1]], 0))
            
    return alignment_matrix
        

### Alignment Functions ###

def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    '''
    computes the optimal global alignent given two sequences and scoring/alignment matrices
    '''
    # initialize the output alignments to empty strings
    (align_x, align_y) = ("", "")
    # initialize the coordinates to the bottom right of the matrix
    (idx_i, idx_j) = (len(seq_x), len(seq_y))
    
    while (idx_i != 0) and (idx_j != 0):
        # elements from i & j are matched together
        if alignment_matrix[idx_i][idx_j] == (alignment_matrix[idx_i - 1][idx_j - 1] + scoring_matrix[seq_x[idx_i - 1]][seq_y[idx_j - 1]]):
            align_x = seq_x[idx_i - 1] + align_x
            align_y = seq_y[idx_j - 1] + align_y
            idx_i -= 1
            idx_j -= 1
        # element from i is matched with "-" instead of j element
        elif alignment_matrix[idx_i][idx_j] == (alignment_matrix[idx_i - 1][idx_j] + scoring_matrix[seq_x[idx_i - 1]]["-"]):    
            align_x = seq_x[idx_i - 1] + align_x
            align_y = "-" + align_y
            idx_i -= 1
        # element from j is matched with "-" instead of i element
        elif alignment_matrix[idx_i][idx_j] == (alignment_matrix[idx_i][idx_j - 1] + scoring_matrix["-"][seq_y[idx_j - 1]]):
            align_x = "-" + align_x
            align_y = seq_y[idx_j - 1] + align_y
            idx_j -= 1
    
    while idx_i > 0:
        align_x = seq_x[idx_i - 1] + align_x
        align_y = "-" + align_y
        idx_i -= 1
        
    while idx_j > 0:
        align_x = "-" + align_x
        align_y = seq_y[idx_j - 1] + align_y
        idx_j -= 1
        
    return (alignment_matrix[len(seq_x)][len(seq_y)], align_x, align_y)
    

def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix): 
    '''
    output the best alignment for a local gene pair
    '''
    # find the indices that have the maximum score in the alignment_matrix
    max_score = float("-inf")
    for row_idx in range(len(alignment_matrix)):
        for col_idx in range(len(alignment_matrix[row_idx])):
            iter_score = alignment_matrix[row_idx][col_idx]
            if iter_score > max_score:
                (max_score, idx_i, idx_j) = (iter_score, row_idx, col_idx)
    
    # initialize the local alignment strings
    (align_x, align_y) = ("", "")
    
    while (idx_i != 0) and (idx_j != 0):
        # stop the traceback if a zero value is found
        if alignment_matrix[idx_i][idx_j] == 0:
            break
        # elements from i & j are matched together
        elif alignment_matrix[idx_i][idx_j] == (alignment_matrix[idx_i - 1][idx_j - 1] + scoring_matrix[seq_x[idx_i - 1]][seq_y[idx_j - 1]]):
            align_x = seq_x[idx_i - 1] + align_x
            align_y = seq_y[idx_j - 1] + align_y
            idx_i -= 1
            idx_j -= 1
        # element from i is matched with "-" instead of j element
        elif alignment_matrix[idx_i][idx_j] == (alignment_matrix[idx_i - 1][idx_j] + scoring_matrix[seq_x[idx_i - 1]]["-"]):    
            align_x = seq_x[idx_i - 1] + align_x
            align_y = "-" + align_y
            idx_i -= 1
        # element from j is matched with "-" instead of i element
        elif alignment_matrix[idx_i][idx_j] == (alignment_matrix[idx_i][idx_j - 1] + scoring_matrix["-"][seq_y[idx_j - 1]]):
            align_x = "-" + align_x
            align_y = seq_y[idx_j - 1] + align_y
            idx_j -= 1
        
    return (max_score, align_x, align_y)
            
    
'''
Question 1 - 3, Comparing alignments apple-to-apples
'''

# load in the data with URLs defined up top
human = read_protein(HUMAN_EYELESS_URL)
fruitfly = read_protein(FRUITFLY_EYELESS_URL)
consensus = read_protein(CONSENSUS_PAX_URL)
m_score = read_scoring_matrix(PAM50_URL)

# compute the local alignment of human and fruitfly genes
human_fruitfly_align = compute_local_alignment(human, fruitfly, m_score, compute_alignment_matrix(human, fruitfly, m_score, False))
(human_align, fruitfly_align) = (human_fruitfly_align[1], human_fruitfly_align[2])

# human-consensus alignment
human_align = re.sub('-', '', human_align)
human_consensus_align = compute_global_alignment(human_align, consensus, m_score, compute_alignment_matrix(human_align, consensus, m_score, True))

# fruitfly-consensus alignment
fruitfly_align = re.sub("-", "", fruitfly_align)
fruitfly_consensus_align = compute_global_alignment(fruitfly_align, consensus, m_score, compute_alignment_matrix(fruitfly_align, consensus, m_score, True))

def seq_accuracy(seq_x, seq_y):
    '''
    calculate the percentage of sequences that agree
    '''
    accurate = 0
    total = len(seq_x)
    for idx in range(len(seq_x)):
        (x, y) = (seq_x[idx], seq_y[idx])
        if x == y:
            accurate += 1
    
    return float(accurate) / float(total) 


#print "human-consensus accuracy: ", seq_accuracy(human_consensus_align[1], human_consensus_align[2])
#print "fruitfly-consensus accuracy: ", seq_accuracy(fruitfly_consensus_align[1], fruitfly_consensus_align[2])


'''
Question 4: Hypothesis Testing
'''

def generate_null_distribution(seq_x, seq_y, scoring_matrix, num_trials):
    '''
    create a scoring distribution for different alignments
    '''
    scoring_distribution = dict()
    for _ in range(num_trials):
        print "count:", _
        splitter = list(seq_y)
        random.shuffle(splitter)
        rand_y = ''.join(splitter)
        score = compute_local_alignment(seq_x, rand_y, scoring_matrix, compute_alignment_matrix(seq_x, rand_y, scoring_matrix, False))[0]
        # increment the scoring distribution score entry by 1 if it is already in the dictionary, or set it to 1 otherwise
        scoring_distribution[score] = scoring_distribution.get(score, 0) + 1
    
    return scoring_distribution


def plot_null_dist():
    '''
    function to plot a normalized distribution
    '''
    nonnormal = generate_null_distribution(human, fruitfly, m_score, 1000)
    
    # normalize this distribution
    normal = dict()
    sum = 0
    for val in nonnormal.itervalues():
        sum += val
    for key in nonnormal:
        normal[key] = nonnormal[key] / float(sum)
    
    # place this normalized distribution into a list
    (x_list, y_list) = (list(), list())
    for key, value in normal.items():
        x_list.append(key)
        y_list.append(value)
    
    plt.bar(x_list, y_list, color="blue")
    plt.title("Probability Density of Local Alignment Scores")
    plt.xlabel("Local Alignment Score")
    plt.ylabel("Empirical Probability")
    plt.show()
    

#plot_null_dist()
    
def moments_dist(nonnormal_dist):
    '''
    calculate the mean/standard deviation of an unnormalized distribution
    '''
    # normalize the distribution
    # normalize this distribution
    normal = dict()
    sum = 0
    for val in nonnormal_dist.itervalues():
        sum += val
    for key in nonnormal_dist:
        normal[key] = nonnormal_dist[key] / float(sum)
    
    # calculate the mean
    mean = 0
    for val, prob in normal.items():
        mean += val * prob
    
    # calculate the standard deviation
    var = 0
    for val, prob in normal.items():
        var += prob * (val - mean) ** 2
        
    return "mean:", mean, "standard deviation:", math.sqrt(var), "z-score:", (875 - mean) / math.sqrt(var)
    

#nonnormal_dist = {39: 1, 40: 8, 41: 7, 42: 12, 43: 28, 44: 53, 45: 58, 46: 59, 47: 73, 48: 59, 49: 65, 50: 60, 51: 72, 52: 58, 53: 46, 54: 61, 55: 45, 56: 36, 57: 25, 58: 20, 59: 22, 60: 20, 61: 17, 62: 12, 63: 16, 64: 14, 65: 8, 66: 7, 67: 6, 68: 7, 69: 1, 70: 6, 71: 1, 73: 5, 74: 1, 75: 3, 76: 1, 78: 1, 79: 1, 80: 1, 81: 1, 83: 2, 86: 1}   
#print moments_dist(nonnormal_dist)
    
'''
Question 8
'''

def check_spelling(checked_word, dist, word_list):
    '''
    spell check function
    '''
    output = list()
    for word in word_list:
        m_score = build_scoring_matrix(set(string.ascii_lowercase), 2, 1, 0)
        m_align = compute_alignment_matrix(checked_word, word, m_score, True)
        if (len(checked_word) + len(word) - compute_global_alignment(checked_word, word, m_score, m_align)[0]) <= dist:
            output.append(word)
            
    return output

    
### spell check application
# download textfile to local folder and prep the dictionary list as a function input
fhand = open("assets_scrabble_words3.txt", "r")
my_dict = fhand.read()
my_dict = my_dict.split()
print check_spelling("humble", 1, my_dict)
print check_spelling("firefly", 2, my_dict)        
    
    
    
    