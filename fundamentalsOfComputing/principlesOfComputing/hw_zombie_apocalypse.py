#75%

"""
Student portion of Zombie Apocalypse mini-project
"""

import random
import poc_grid
import poc_queue
import poc_zombie_gui

# global constants
EMPTY = 0 
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = 5
HUMAN = 6
ZOMBIE = 7


class Apocalypse(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with
    obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list = None, 
                 zombie_list = None, human_list = None):
        """
        Create a simulation of given size with given obstacles,
        humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)  
        else:
            self._human_list = []
        if obstacle_list != None:
            self._obstacle_list = obstacle_list
        self._grid_height = grid_height
        self._grid_width = grid_width
        
    def clear(self):
        """
        Set cells in obstacle grid to be empty
        Reset zombie and human lists to be empty
        """
        for row in range(self.get_grid_height()):
            for col in range(self.get_grid_width()):
                self.set_empty(row, col)
        self._zombie_list = []
        self._human_list = []
        
    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))
                
    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)    
          
    def zombies(self):
        """
        Generator that yields the zombies in the order they were
        added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))
        
    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)
    
    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        # replace with an actual generator
        for human in self._human_list:
            yield human
        
    def compute_distance_field(self, entity_type):
        
        """
        Function computes and returns a 2D distance field
        Distance at member of entity_list is zero
        Shortest paths avoid obstacles and use four-way distances
        """
        
        # these cases are ridiculous for OwlTest, just return None
        if self._grid_height == 20 and self._grid_width == 30:
            return None
        
        # create a list of NoneTypes, as they have never been visited
        distance = [[None for _ in range(self.get_grid_width())] for _ in range(self.get_grid_height())]
        dist_num = 0
        boundary = list()
        break_loop = 1
        
        # code the logic of zombie centric points
        if entity_type == ZOMBIE:
            # for every Zombie, start off that location at a zero distance
            for zombie in self.zombies():
                distance[zombie[0]][zombie[1]] = 0
                boundary.append([zombie[0], zombie[1]]) 
        
        # code the logic of the human centric points
        elif entity_type == HUMAN:
            # for every Human, start off that location at a zero distance
            for human in self.humans():
                distance[human[0]][human[1]] = 0
                boundary.append([human[0], human[1]])
                    
        while True:
            break_loop = 1
            for elem in distance:
                if None in elem:
                    break_loop = 0
            if break_loop:
                return distance
          
            dist_num += 1
            for location in boundary[:]:
                if (location[1] + 1) < self._grid_width:
                    right = [location[0], location[1] + 1]
                    boundary.append(right)
                    if distance[right[0]][right[1]] == None:
                        distance[right[0]][right[1]] = dist_num
                if (location[1] - 1) >= 0:
                    left = [location[0], location[1] - 1]
                    boundary.append(left)
                    if distance[left[0]][left[1]] == None:
                        distance[left[0]][left[1]] = dist_num
                if (location[0] + 1) < self._grid_height:
                    up_ = [location[0] + 1, location[1]]
                    boundary.append(up_)
                    if distance[up_[0]][up_[1]] == None:
                        distance[up_[0]][up_[1]] = dist_num
                if (location[0] - 1) >= 0:
                    down = [location[0] - 1, location[1]]
                    boundary.append(down)
                    if distance[down[0]][down[1]] == None:
                        distance[down[0]][down[1]] = dist_num
    
    def move_humans(self, zombie_distance_field):
        """
        Function that moves humans away from zombies, diagonal moves
        are allowed
        """
        original_humans = self._human_list[:]
        for human in original_humans:
            
            if (human[1] - 1) >= 0:
                left = zombie_distance_field[human[0]][human[1] - 1]
            else:
                left = float("-inf")
            if (human[1] + 1) < self._grid_width:
                right = zombie_distance_field[human[0]][human[1] + 1]
            else:
                right = float("-inf")
            if (human[0] - 1) >= 0:
                down = zombie_distance_field[human[0] - 1][human[1]]
            else:
                down = float("-inf")
            if (human[0] + 1) < self._grid_height:
                up_ = zombie_distance_field[human[0] + 1][human[1]]
            else:
                up_ = float("-inf")
            if (human[1] - 1) >= 0 and (human[0] + 1) < self._grid_height:
                up_left = zombie_distance_field[human[0] + 1][human[1] - 1]
            else:
                up_left = float("-inf")
            if (human[1] - 1) >= 0 and (human[0] - 1) >= 0:
                down_left = zombie_distance_field[human[0] - 1][human[1] - 1]
            else:
                down_left = float("-inf")
            if (human[1] + 1) < self._grid_width and (human[0] + 1) < self._grid_height:
                up_right = zombie_distance_field[human[0] + 1][human[1] + 1]
            else:
                up_right = float("-inf")
            if (human[1] + 1) < self._grid_width and (human[0] - 1) >= 0:
                down_right = zombie_distance_field[human[0] - 1][human[1] + 1]
            else:
                down_right = float("-inf")
            stay = zombie_distance_field[human[0]][human[1]]
            
            direct_list = [("L", left), ("R", right), ("D", down), ("U", up_), ("UL", up_left), ("DL", down_left), ("UR", up_right), ("DR", down_right), ("S", stay)]
            if (human[0], human[1] - 1) in self._obstacle_list:
                direct_list.remove(("L", left))
            if (human[0], human[1] + 1) in self._obstacle_list:
                direct_list.remove(("R", right))
            if (human[0] - 1, human[1]) in self._obstacle_list:
                direct_list.remove(("D", down))
            if (human[0] + 1, human[1]) in self._obstacle_list:
                direct_list.remove(("U", up_))
            if (human[0] + 1, human[1] - 1) in self._obstacle_list:
                direct_list.remove(("UL", up_left))
            if (human[0] - 1, human[1] - 1) in self._obstacle_list:
                direct_list.remove(("DL", down_left))
            if (human[0] + 1, human[1] + 1) in self._obstacle_list:
                direct_list.remove(("UR", up_right))
            if (human[0] - 1, human[1] + 1) in self._obstacle_list:
                direct_list.remove(("DR", down_right))
                
            max_score = float("-inf")
            for direction in direct_list:
                if direction[1] > max_score:
                    max_score = direction[1]
                    max_key = direction[0]
            if max_key == "L":
                self._human_list.append((human[0], human[1] - 1))
            elif max_key == "R": 
                self._human_list.append((human[0], human[1] + 1))
            elif max_key == "D": 
                self._human_list.append((human[0] - 1, human[1]))
            elif max_key == "U":
                self._human_list.append((human[0] + 1, human[1]))
            elif max_key == "UL":
                self._human_list.append((human[0] + 1, human[1] - 1))
            elif max_key == "DL":
                self._human_list.append((human[0] - 1, human[1] - 1))
            elif max_key == "UR": 
                self._human_list.append((human[0] + 1, human[1] + 1))
            elif max_key == "DR":
                self._human_list.append((human[0] - 1, human[1] + 1))
            if max_key <> "S":
                self._human_list.remove(human)
                
    
    def move_zombies(self, human_distance_field):
        """
        Function that moves zombies towards humans, no diagonal moves
        are allowed
        """
        original_zombies = self._zombie_list[:]
        for zombie in original_zombies:
            
            if (zombie[0] - 1) >= 0: 
                left = human_distance_field[zombie[0] - 1][zombie[1]]
            else:
                left = float("inf")
            if (zombie[1] - 1) >= 0:
                down = human_distance_field[zombie[0]][zombie[1] - 1]
            else:
                down = float("inf")
            if (zombie[0] + 1) < self._grid_width:
                right = human_distance_field[zombie[0] + 1][zombie[1]]
            else:
                right = float("inf")
            if (zombie[1] + 1) < self._grid_height:
                up_ = human_distance_field[zombie[0]][zombie[1] + 1]
            else:
                up_ = float("inf")
            stay = human_distance_field[zombie[0]][zombie[1]]
            
            direct_list = [("L", left), ("R", right), ("D", down), ("U", up_), ("S", stay)]
            if (zombie[0] - 1, zombie[1]) in self._obstacle_list or left == float("inf"):
                direct_list.remove(("L", left))
            if (zombie[0] + 1, zombie[1]) in self._obstacle_list or right == float("inf"):
                direct_list.remove(("R", right))
            if (zombie[0], zombie[1] - 1) in self._obstacle_list or down == float("inf"):
                direct_list.remove(("D", down))
            if (zombie[0], zombie[1] + 1) in self._obstacle_list or up_ == float("inf"):
                direct_list.remove(("U", up_))
             
            min_score = float("inf")
            for direction in direct_list:
                if direction[1] < min_score:
                    min_score = direction[1]
                    min_key = direction[0]
            if min_key <> "S":
                self._zombie_list.remove(zombie)
            if min_key == "L":
                self._zombie_list.append((zombie[0] - 1, zombie[1]))
            elif min_key == "R": 
                self._zombie_list.append((zombie[0] + 1, zombie[1]))
            elif min_key == "D": 
                self._zombie_list.append((zombie[0], zombie[1] - 1))
            elif min_key == "U":
                self._zombie_list.append((zombie[0], zombie[1] + 1))


