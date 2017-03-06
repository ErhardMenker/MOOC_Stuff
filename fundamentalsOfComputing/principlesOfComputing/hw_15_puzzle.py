#Completed Puzzle Perfectly!!!
"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

import poc_fifteen_gui

class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid != None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    #####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    ########################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers        
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return (row, col)
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """
        #return False if 0 not in target location
        if self.get_number(target_row, target_col) != 0:
            return False
        #return False if rows below target location are not in solved location
        for col in range(self.get_width()):
            for row in range(target_row + 1, self.get_height()):
                if self.current_position(row, col) != (row, col):
                    return False
        #return False if columns to the right of target location are not solved
        for col in range(target_col + 1, self.get_width()):
            if self.current_position(target_row, col) != (target_row, col):
                return False
        #if none of the invariant conditions are broken, return True
        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """
        #initialize empty string to be string concatenated with moves
        moves = ""
        #check to see whether starting (target_row, target_col) is a solved position by invariance
        assert self.lower_row_invariant(target_row, target_col), "starting position not solved"
        #find row and column where the value belonging in target initially resides
        (init_row, init_col) = self.current_position(target_row, target_col)
        
        #if the target tile is in current row:
        boolean = True
        if target_row == init_row:
            moves += (target_col - init_col) * "l"
            moves += (target_col - init_col - 1) * "urrdl"
            boolean = False
        
        #execute a switch to find out what category the initial puzzle is in
        #row_offset offsets situations in which moving the tile into the proper column also moved it down a row
        row_offset = -1
        while boolean:
           
            #move zero tile up to the same row as the target tile
            moves += (target_row - init_row) * "u" 
                
            #if the target tile is in a higher row (but not in first row) and in a rightward column, bring it over by cycling it left
            if target_col < init_col and init_row > 0:
                moves += (init_col - target_col) * "r"
                moves += (init_col - target_col - 1) * "ulldr"
                moves += "ul"
                row_offset = 0
            
            #if the target tile is in a higher row (but not in first row) and in a leftward column, bring it over by cycling it right
            elif target_col > init_col and init_row > 0:
                moves += (target_col - init_col) * "l"
                moves += (target_col - init_col - 1) * "urrdl"
                moves += "ur"
                row_offset = 0
                
            #if the target tile is in the zeroeth row and to the right, cycle it without going off grid
            elif target_col < init_col and init_row == 0:
                moves += (init_col - target_col) * "r"
                moves += (init_col - target_col - 1) * "dllur"
                moves += "dlu"
                
            #if the target tile is in the zeroeth row and to the left, cycle it without going off grid
            elif target_col > init_col and init_row == 0:
                moves += (target_col - init_col) * "l"
                moves += (target_col - init_col - 1) * "drrul"
                moves += "dru"
            
            #now we are one row above the target tile in its solved row, bring it down
            moves += (target_row - init_row + row_offset) * "lddru"
            moves += "ld"
            break
          
        #update the puzzle and return the moves if ending invariant condition is satisfied 
        self.update_puzzle(moves)
        assert self.lower_row_invariant(target_row, target_col - 1), "ending position not solved"
        return moves
        
    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """
        
        assert self.lower_row_invariant(target_row, 0), "starting position not solved"
        
        #gather coordinates where the target puzzle initially exists at function call
        (init_row, init_col) = self.current_position(target_row, 0)
        
        #move the zero tile up 1 and to the right 1
        moves = "ur"
        
        #boolean to determine if the puzzle has been solved (indicates if further logic should be executed)
        solved = False
        
        #move the zero tile to zeroth column with target tile one to the right on same row
        while True:
            
            #if target now is in desired spot after moving "ur", move zero tile back to zeroth column before moving back for harmony with other cases
            if self.get_number(target_row - 1, 0) == self.get_number(init_row, init_col):
                moves += "l"
                #switch the puzzle's solved Boolean and exit loop
                solved = True
                break
            
            #if target tile is in zeroth column and hasn't been solved, bring it to right spot
            if init_col == 0:
                #go under the target puzzle
                moves += "l"
                #move above the target puzzle
                moves += (target_row - init_row - 1) * "u"
                #cycle the puzzle down
                moves += (target_row - init_row - 2) * "rddlu"
                moves += "rdl"
                break
                
            #if target tile is not in zeroth column and zeroth row, solve as in if block above
            if init_col > 0 and init_row > 0:
                moves += "l"
                #get on the same row as the target puzzle
                moves += (target_row - init_row - 1) * "u"
                #move to the right of the target on same row
                moves += init_col * "r"
                #cycle target to the zeroth column
                moves += (init_col - 1) * "ulldr"
                #move above the target puzzle
                moves += "ul"
                #cycle the puzzle down
                moves += (target_row - init_row - 2) * "rddlu"
                moves += "rdl"
                break
                
            #if target tile is not in zeroth column but in zeroth row, solve as in if block above
            if init_col > 0 and init_row == 0:
                moves += "l"
                #get on the same row as the target puzzle
                moves += (target_row - init_row - 1) * "u"
                #move to the right of the target on same row
                moves += init_col * "r"
                #cycle target to the zeroth column
                moves += (init_col - 1) * "dllur"
                #move above the target puzzle
                moves += "dlu"
                #cycle the puzzle down
                moves += (target_row - init_row - 2) * "rddlu"
                moves += "rdl"
                break
                
            #throw an assertion error if we haven't executed the loop by now
            assert "A" != "A", "while loop should have executed by now"
        
        if not solved:
            moves += "ruldrdlurdluurddlu"
            
        #move the zero tile to the end, update puzzle and return move string
        moves += (self.get_width() - 1) * "r"
        self.update_puzzle(moves)
        #check that the invariant holds at the new zero tile location before returning th emoves
        assert self.lower_row_invariant(target_row - 1, self.get_width() - 1), "solve_col0_tile() failed to properly solve inputted tile"
        return moves

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """

        #return False if the zero tile is not at (0, target_col)
        if self.get_number(0, target_col) != 0:
            return False
        
        #return False if any tiles below or to the right of (0, target_col) are not solved
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                #if in upper left 2 by 2 grid or to left of zero grid on same row, don't check whether cell is solved
                if row == 0 and col == target_col:
                    continue
                elif row > 1 or col >= target_col:
                    #this is triggered iff this tile has not been solved
                    if self.current_position(row, col) != (row, col):
                        return False
                    
        #return True if we have made it this far and everything is solved
        return True
                    

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """
        
        #return False if the zero tile is not at (0, target_col)
        if self.get_number(1, target_col) != 0:
            return False
        
        #return False if any tiles below or to the right of (0, target_col) are not solved
        for row in range(self.get_height()):
            for col in range(self.get_width()):
                #if in upper left 2 by 2 grid, to the left of zero grid on row 1 or in row 0, don't check whether cell is solved
                if (row == 0 or row == 1) and col == target_col:
                    continue
                elif row > 1 or col >= target_col:
                    #this is triggered iff this tile has not been solved
                    if self.current_position(row, col) != (row, col):
                        return False
                    
        #return True if we have made it this far and everything is solved
        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """
        
        #check to see whether row 0 is prepped for the row 0 solver
        assert self.row0_invariant(target_col), "board not ready for solve_row0_tile() method"

        #find coordinates of target tile
        (init_row, init_col) = self.current_position(0, target_col)
        
        #initialize a moves strings and move left and down
        moves = "ld"
        
        while True:
        
            #if row 0 is solved for target_col because of initial tile placement, moves are complete
            if init_row == 0 and init_col == target_col - 1:
                break

            #get zero tile one row above target tile in column (init_col - 1):
            
            #if target tile is one row above zero tile and in same column, just move the zero tile up 1
            if init_row == 1 and init_col == target_col - 1:
                moves += "u"
            
            #if target tile is in the zeroth row and leftwards, cycle it over
            elif init_row == 0 and init_col < target_col - 1:
                #move the zero tile onto the same row 0 as the target tile
                moves += "u"
                #move the zero tile one left of the target tile until tile locations swap
                moves += (target_col - init_col - 1) * "l"
                #cycle it over
                moves += (target_col - init_col - 2) * "drrul"
                #place the zero tile one above the target tile in the same column
                moves += "dru"
                
            #if target tile is in the first row and leftwards, cycle it over 
            elif init_row == 1 and init_col < target_col - 1:
                #move the zero tile one left of the target tile until tile locations swap
                moves += (target_col - init_col - 1) * "l"
                #cycle it over
                moves += (target_col - init_col - 2) * "urrdl" 
                #place the zero tile one above the target tile in the same column
                moves += "ur"
            
            #zero tile is one above the target tile, implement 3 X 2 puzzle sollution
            moves += "dlurrdluldrruld"
            break
        
        #update puzle by moves string
        self.update_puzzle(moves)
        #see if row 1 invariant is True for one column leftwards
        assert self.row1_invariant(target_col - 1), "solve_row0_tile() method failed"
        return moves
        
        
    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """
        
        #check to see whether row 1 is prepped before solving
        assert self.row1_invariant(target_col), "starting position not prepped to call row one solver"
        
        #find coordinates of target tile
        (init_row, init_col) = self.current_position(1, target_col)
        
        #initialize a moves string
        moves = ""
        
        #if target tile is on the first row, just cycle it over
        if init_row == 1:
            #bring the zero puzzle to the left of the target puzzle
            moves += (target_col - init_col) * "l"
            #cycle the puzzle over
            moves += (target_col - init_col - 1) * "urrdl"
            #place the zero tile in the proper spot
            moves += "ur"
        
        #if target tile is on the zeroth row, bring it down before cycling it over
        elif init_row == 0:
            #bring the zero puzzle up to the target row level
            moves += "u"
            #bring the zero puzzle to the left of the target puzzle
            moves += (target_col - init_col) * "l"
            #cycle the puzzle over
            moves += (target_col - init_col - 1) * "drrul"
            #bring the target puzzle down a row to the solved spot with zero tile in proper spot
            if target_col > init_col:
                moves += "dru"
        
        self.update_puzzle(moves)
        assert self.row0_invariant(target_col), "row 1 not properly solved for"
        return moves
    
    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """
        
        #initialize a moves string
        moves = ""
        
        #find the zero tile location
        (row0, col0) = self.current_position(0, 0)
        #move the zero tile into the upper left corner (its ending spot)
        moves += col0 * "l"
        moves += row0 * "u"
        self.update_puzzle(moves)

        #if the 2 X 2 puzzle has not been solved, complete another cycling iteration
        while self.current_position(0, 0) != (0, 0) or self.current_position(0, 1) != (0, 1) or self.current_position(1, 0) != (1, 0) or self.current_position(1, 1) != (1, 1):
            moves += "rdlu"
            self.update_puzzle("rdlu")

        return moves

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        
        #initialize an empty moves string
        moves = str()

        #find where the zero tile is
        (row0, col0) = self.current_position(0, 0)
        #move the zero tile to the bottom right corner
        moves += (self.get_width() - col0 - 1) * "r" 
        moves += (self.get_height() - row0 - 1) * "d"
        self.update_puzzle(moves)
        
        #solve the phase 1 methods
        row = self.get_height() - 1
        while row > 1:
            #solve the interior puzzles
            for col in sorted(range(1, self.get_width()), reverse=True):
                moves += self.solve_interior_tile(row, col)
            #solve the row's col0
            moves += self.solve_col0_tile(row)
            row -= 1
        
        #solve the phase 2 methods
        col = self.get_width() - 1
        while col > 1:
            moves += self.solve_row1_tile(col)
            moves += self.solve_row0_tile(col)
            col -= 1
            
        #solve the phase 3 method
        moves += self.solve_2x2()
        return moves
        
        
# Start interactive simulation
poc_fifteen_gui.FifteenGUI(Puzzle(4, 4))
