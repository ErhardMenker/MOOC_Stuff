"""
88%!!!
"""
"""
Mini-max Tic-Tac-Toe Player
"""

import poc_ttt_gui
import poc_ttt_provided as provided

# Set timeout, as mini-max can take a long time
import codeskulptor
codeskulptor.set_timeout(60)

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}

def mm_move(board, player):
    
    """
    Make a move on the board.
    
    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    
    #find a list of empty board square tuples from the original board
    empty_squares = board.get_empty_squares()
    
    #initialize a dictionary that maps moves to one step ahead boards
    next_states = dict()
    
    #fill in next_states with all possible states of the board after player moves
    for empty in empty_squares:
        #clone the board to fill in that level at
        board_clone = board.clone()
        board_clone.move(empty[0], empty[1], player)
        #tack this new possible board state to the list of all possible one move ahead board states
        next_states[empty] = board_clone
    
    inconclusive_games = list()
    look_for_draw = 0
    
    #go through each game state's move and fill in the remaning values by recursive call if the game is not over
    for move in next_states:
        developed_board = next_states[move]
        print developed_board
        #if this board choice is a winner, select it!
        if developed_board.check_win() != None and SCORES[player] * SCORES[developed_board.check_win()] == 1:
            print SCORES[player] * SCORES[developed_board.check_win()]
            return SCORES[developed_board.check_win()], move
        #if this board has a losing option, swith the Boolean to look for draws
        if developed_board.check_win() != None and SCORES[player] * SCORES[developed_board.check_win()] == -1:
            look_for_draw = 1
        #if this board is inconclusive, append it to the inconclusive_games list to be called again
        if developed_board.check_win() == None:
            inconclusive_games.append(developed_board)
    
    #if there is a path for opponent to win, be satisfied with a draw
    if look_for_draw:
        for move in next_states:
            if developed_board.check_win() != None and SCORES[player] * SCORES[developed_board.check_win()] == 0:
                return 0, move
    
    #switch the player and see how he will play next hand for empty options
    player = provided.switch_player(player)
    for board in inconclusive_games:
        mm_move(board, player)

def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)
    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

#print mm_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.EMPTY, provided.PLAYERX], [provided.EMPTY, provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY, provided.EMPTY]]), provided.PLAYERO) 
#print mm_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.EMPTY, provided.EMPTY]]), provided.PLAYERX) 
#print mm_move(provided.TTTBoard(3, False, [[provided.EMPTY, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.PLAYERX, provided.EMPTY], [provided.PLAYERO, provided.EMPTY, provided.EMPTY]]), provided.PLAYERO)
#print  mm_move(provided.TTTBoard(2, False, [[provided.EMPTY, provided.EMPTY], [provided.EMPTY, provided.EMPTY]]), provided.PLAYERO)
#print mm_move(provided.TTTBoard(3, False, [[provided.PLAYERX, provided.PLAYERX, provided.PLAYERO], [provided.EMPTY, provided.PLAYERX, provided.PLAYERX], [provided.PLAYERO, provided.EMPTY, provided.PLAYERO]]), provided.PLAYERO)

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)        
# poc_ttt_gui.run_gui(3, provided.PLAYERO, move_wrapper, 1, False)