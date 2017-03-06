""" Passable, but last function is dodgy """

"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided


# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 5         # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player
    
# Add your functions here.

def mc_trial(board, player):
    
    """
    goes through a board and produces a random possible final outcome
    """
    
    # provide a list of square coordinates in TTT area
    empty_spaces = board.get_empty_squares()
    # fill in these square coordinates iteratively until none exist
    while len(empty_spaces) >= 1:
        select = random.choice(empty_spaces)
        empty_spaces.remove(select)
        board.move(select[0], select[1], player)
        player = provided.switch_player(player)

def mc_update_scores(scores, board, player):
    
    """
    updates the scores based on whether square was selected by a winner or loser
    """
    
    # check which player won
    winner = board.check_win()
    # if the game was draw or incomplete, break out of function
    if winner == provided.DRAW or winner == provided.EMPTY:
        return None
    row = -1
    for score_row in scores:
        row += 1
        col = -1
        for score in range(len(score_row)):
            col += 1
            # if square was chosen by a winner, add to its value
            if (board.square(row, col) == provided.PLAYERX and winner == provided.PLAYERX) or (board.square(row, col) == provided.PLAYERO and winner == provided.PLAYERO):
                scores[row][col] += 1
                #print "row: ", row, "col: ", col, "score: ", scores[row][col]
            # if square was chosen by a loser, subtract from its value
            elif (board.square(row, col) == provided.PLAYERX and winner == provided.PLAYERO) or (board.square(row, col) == provided.PLAYERO and winner == provided.PLAYERX):
                scores[row][col] -= 1
                
def get_best_move(board, scores):
    
    """
    selects the best move given a list of scores
    """
    
    empty_spaces = board.get_empty_squares()
    # break out of function if there are no empty squares
    if len(empty_spaces) == 0:
        return None
    best_score = None
    row = -1
    for score_row in scores:
        row += 1
        col = -1
        for score in range(len(score_row)):
            col += 1
            # if the score is best in this row and column, tentatively make it...
            # ...the best row and column and record the best score for future comparison
            if scores[row][col] > best_score and board.square(row, col) == provided.EMPTY:
                best_score = scores[row][col]
                row_star = row
                col_star = col
    return (row_star, col_star)

def mc_move(board, player, trials):
    
    """
    Fills the board by the amount of trials and compiles scores,...
    ...returns best move given scoring system after all these trials
    """
    
    # initialize a scoring matrix of zeros
    scores = list()
    scores_list = list()
    for dim in range(board.get_dim()):
        scores.append(0)
    for dim in range(board.get_dim()):
        scores_list.append(scores)
    # for every trial...
    for trial in range(trials):
        board_copy = board.clone()
        # ...fill the board with moves
        mc_trial(board_copy, player)
        # ...score the board
        mc_update_scores(scores_list, board_copy, player)
    # given this updated scoreboard, make the best move
    return get_best_move(board, scores_list)
    
print mc_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERO, NTRIALS)

# Test game with the console or the GUI.  Uncomment whichever 
# you prefer.  Both should be commented out when you submit 
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)        
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)
