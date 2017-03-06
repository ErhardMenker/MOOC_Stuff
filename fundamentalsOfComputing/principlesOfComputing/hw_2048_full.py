""" Phase 3 Work: Can print a temp list from any direction """


""" Phase 3 Work: Can print a temp list from any direction """


"""
Clone of 2048 game.
"""

#import poc_2048_gui
import random

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.
OFFSETS = {UP: (1, 0),
           DOWN: (-1, 0),
           LEFT: (0, 1),
           RIGHT: (0, -1)}

def merge(line):
    """
    Function that merges a single row or column in 2048.
    """
    copy = list()
    for elem in line:
        copy.append(elem)
    
    for idx in range(len(line) - 1):
        #loop through remaining list and slide over non-zero values:
        for elem in copy[idx:]:
            if elem == 0:
                copy.remove(elem)
                copy.append(elem)
        index_0 = copy[idx]
        index_1 = copy[idx+1]
        #add consecutive equal entries, slide them over:
        if index_0 == index_1:
            copy[idx] = index_0 + index_1
            copy[idx + 1] = 0
           
    return copy

class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        self._width = grid_width
        self._height = grid_height
        initial_up = [(0, cols) for cols in range(self._width)] 
        initial_down = [(self._height - 1, cols) for cols in range(self._width)]
        initial_left = [(rows, 0) for rows in range(self._height)]
        initial_right = [(rows, self._width - 1) for rows in range(self._height)]
        self._initial_dict = {"UP": initial_up, "DOWN": initial_down, "LEFT": initial_left, "RIGHT": initial_right}
        self._grid = ""
        self.reset()
       
    def reset(self):
        """
        Reset the game so the grid is empty except for two
        initial tiles.
        """
        #initialize grid to all zeros
        self._grid = [[0 for w_coord in range(self._width)] for h_coord in range(self._height)]
        #call in method to place in non-zero values
        self.new_tile()
        self.new_tile()
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        # initialize empty output string to be filled up with the representation
        output = ""
        for grid_line in self._grid:
            for grid_entry in grid_line:
                output = output + str(grid_entry) + " "
        return output
        

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        # replace with your code
        height = self._height
        return height

    def get_grid_width(self):
        """
        Get the width of the board.
        """
        width = self._width
        return width

    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # map the direction key to the proper initial tile and offset values
        if direction == 1:
            init_tiles = self._initial_dict["UP"]
            offset = OFFSETS[UP]
        elif direction == 2:
            init_tiles = self._initial_dict["DOWN"]
            offset = OFFSETS[DOWN]
        elif direction == 3:
            init_tiles = self._initial_dict["LEFT"]
            offset = OFFSETS[LEFT]
        elif direction == 4:
            init_tiles = self._initial_dict["RIGHT"]
            offset = OFFSETS[RIGHT]
        
        change = False
        for coords in init_tiles:
            temp = list()
            coords = list(coords)
            value = self.get_tile(coords[0], coords[1])
            temp.append(value)
            while True:
                coords[0] += offset[0]
                coords[1] += offset[1]
                if coords[0] < 0 or coords[1] < 0:
                    break
                try:
                    value = self.get_tile(coords[0], coords[1])
                    temp.append(value)
                except:
                    break
            reorder = merge(temp)
            if temp <> reorder:
                change = True
            #reorder the list and insert the new values in for an initial range in reverse order
            reorder.reverse()
            for val in reorder:
                coords[0] -= offset[0]
                coords[1] -= offset[1]
                self.set_tile(coords[0], coords[1], val)
        if change == True:
            self.new_tile()

           
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        for grid_list in self._grid:
            # if there is a zero anywhere in the grid, fill in random zero entry with 2 (90%) or 4 (10%)
            if 0 in grid_list:
                while True:
                    height_idx = random.randrange(self._height) 
                    width_idx = random.randrange(self._width)
                    if self.get_tile(height_idx, width_idx) == 0:
                        tile_list = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]
                        random.shuffle(tile_list)
                        self.set_tile(height_idx, width_idx, tile_list[0])
                        break
                break

    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value
        return value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """
        return self._grid[row][col]


#poc_2048_gui.run_gui(TwentyFortyEight(4, 5))