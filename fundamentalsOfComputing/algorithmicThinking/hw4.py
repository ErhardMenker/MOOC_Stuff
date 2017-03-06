'''
Project 4: Dynamic Programming
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
            
        
    
    
    
    
    
    
    
    
    
    
    