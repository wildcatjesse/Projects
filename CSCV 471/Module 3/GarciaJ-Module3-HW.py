'''
Jesse Garcia
HomeWork Assignment 3
CSCV 471 Fall 2023
October 1, 2023
'''
import numpy as np
import pandas as pd
import random


class VacuumCleaner:
    '''
    The vacuum object will give its position, move, or clean a tile.
    '''
    def __init__(self, position):
        self.position = position
        self.status = 'OFF'

    def move(self, new_position):
        self.position = new_position

    def clean(self, environment):
        # clean the dirt at the current position
        pass


class Environment:
    '''
    Environment Object that handles all actions environment. From placing dirt on our grid in the beginning
    to the cleaning of the tile if it is dirtyas the vacuum goes through.
    '''
    def __init__(self, size=5):
        self.grid = [[0 for _ in range(size)] for _ in range(size)]  # Initialize a 5x5 grid
        self.dirt_positions = set()  # Initialize dirt positions

    def place_dirt(self, position):
        x, y = position
        self.grid[x][y] =1
        self.dirt_positions.add(position)


    def remove_dirt(self, position):
        x, y = position
        self.grid[x][y] = 0
        self.dirt_positions.remove(position)

    def has_dirt(self, position):
        return position in self.dirt_positions

    def display_grid(self):
        for row in self.grid:
            print(row)

def add_tuples(position):
    '''
    the function that will return the position that the vacuum will move to.
    I have set it so that it does not retun  anything less than (0,0) or (4,4), since those are the dimensions of a 5x5 grid.
    :param positon which is current position
    :return: the new postion
    '''
    direction = {
        'up': (-1, 0),
        'down': (1, 0),
        'left': (0, -1),
        'right': (0, 1)
    }
    arr1 = np.array(position)
    arr2 = random.choice(list(direction.values()))
    new_pos = tuple(np.add(arr1,arr2))
    # checking to see if the tuple is with the range and does not go out of bounds.
    is_in_range = all(0 <= x < 5 for x in new_pos)
    # loop to find a new position that is with in the bounds of griud, with the current position of the vacuum
    while not is_in_range:
        arr2 = random.choice(list(direction.values()))
        new_pos = tuple(np.add(arr1, arr2))
        is_in_range = all(0 <= x < 5 for x in new_pos)
    return new_pos

# actions is the counter for how many actions we need. In this case directions from assignment say 10
actions = 0
# this variable will store all visited locations as a set so there are no duplicates, and we \
# will use it to check to see whether we have already visited a tile
visited = set()


if __name__ == '__main__':
    # Creating our vacuum object at position 2,2 and recording that in our visited variable
    vacuum = VacuumCleaner((2, 2))
    visited.add(vacuum.position)
    # creating our environment object and creating 10 random tiles with dirt(10 is a number I chose)
    environment = Environment()
    # for loop has 2 variables, looping through a static number\
    # j and i just get a random number between 0 and 5, then we plug those random coordinated to the place_dirty method\
    # to get our dirty tiles
    for e in range(10):
        j = random.randrange(0, 5, 1)
        i = random.randrange(0, 5, 1)
        environment.place_dirt((j,i))


    print(f"Grid with dirt")
    environment.display_grid()
    # loop that is moving the vacuum, checks whether tile is dirty and acts accordingly.
    while actions <10:
        # checks to make sure the tile has not already beev visited
        if vacuum.position not in visited:
            # checks to see if tile has dirt, if it does, it vacuums then moves
            if environment.has_dirt(vacuum.position):
                vacuum.clean(environment.remove_dirt(vacuum.position))
                print(f'\n{vacuum.position} Tile was dirty. Vaccum just cleaned position: {vacuum.position}')
                visited.add(vacuum.position)
                environment.display_grid()
                vacuum.move(add_tuples(vacuum.position))
                print(f'moving to: {vacuum.position}')
                actions = actions + 1
            # Will go here if the tile was already clean. Then will move to the next.
            else:
                print(f'\n{vacuum.position}Tile is clean.Moving to new position:')
                vacuum.move(add_tuples(vacuum.position))
                print(vacuum.position)
                environment.display_grid()
                actions = actions + 1
        # will execute this if the tile had already been visited.
        else:
            print(f'\nAlready visited {vacuum.position}, moving to next position: ')
            vacuum.move(add_tuples(vacuum.position))
            print(vacuum.position)
            environment.display_grid()
            actions = actions + 1


