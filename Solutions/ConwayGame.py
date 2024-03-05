"""
    '''
    Populates the game grid with live cells at the specified coordinates.
    
    Parameters:
    coord: A list of tuples. Each tuple represents the (x, y) coordinates of a live cell.

    Returns:
    The updated life_grid with the new live cells.
    '''
    # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
    # Set the corresponding elements in your grid to 1.
"""
import numpy as np
import matplotlib.pyplot as plt

class GameOfLife:
    
    # Initialize a 2D list with dimensions x_dim by y_dim filled with zeros.
    def __init__(self, x_dim, y_dim):
        self.x_dim = x_dim
        self.y_dim = y_dim
        self.life_grid = [[0] * y_dim for _ in range(x_dim)]
        
    # Implement a getter method for your grid.
    def get_grid(self):
        return self.life_grid
    
    # Implement a method to print out your grid in a human-readable format.
    def print_grid(self):
        for i in range(self.x_dim):
            for j in range(self.y_dim):
                print(self.life_grid[i][j], end=' | ')
            print()  # Start a new line after each row
            print('-' * (self.y_dim * 4))  # Print row separator
            
    # Given a list of 2D coordinates (represented as tuples/lists with 2 elements each),
    # set the corresponding elements in your grid to 1.              
    def populate_grid(self, coord):  
        for c in coord:
            row, col = c
            self.life_grid[row][col] = 1
        return self.life_grid
        
    # Implement the logic to update the game state according to the rules of Conway's Game of Life.
    def make_step(self):
        sum_grid = [[0] * self.y_dim for _ in range(self.x_dim)]

        for i in range(self.x_dim):
            for j in range(self.y_dim):
                # Calculate the sum of neighbors
                live_neighbors = 0

                # Iterate through the neighboring cells
                for a in range(i - 1, i + 2):
                    for b in range(j - 1, j + 2):
                        if a == i and b == j:
                            continue  # Skip the current cell
                        if 0 <= a < self.x_dim and 0 <= b < self.y_dim:
                            live_neighbors += self.life_grid[a][b]

                # Update the sum_grid
                sum_grid[i][j] = live_neighbors

        for i in range(self.x_dim):
            for j in range(self.y_dim):
                # Apply the Game of Life rules
                if self.life_grid[i][j] == 1:
                    if sum_grid[i][j] < 2 or sum_grid[i][j] > 3:
                        self.life_grid[i][j] = 0
                else:
                    if sum_grid[i][j] == 3:
                        self.life_grid[i][j] = 1
                    elif sum_grid[i][j] == 2:
                        self.life_grid[i][j] = self.life_grid[i][j]

        return self.life_grid
    
    # Implement a method that applies the make_step method n times.
    def make_n_steps(self, n):
        for _ in range(n):
            self.make_step()
        return self.life_grid
    
    # Draw the current state of the grid.
    def draw_grid(self):
        x = []
        y = []
        c = []

        for i in range(self.y_dim):
            for j in range(self.x_dim):
                if self.life_grid[j][i] == 1:
                    x.append(i)
                    y.append(j)
                    c.append(self.life_grid[j][i])

        x = np.array(x)
        y = np.array(y)
        c = np.array(c)

        fig, ax = plt.subplots(figsize=(self.y_dim, self.x_dim))
        ax.scatter(x, y, c=c, cmap='binary', s=200, edgecolors='black', marker='s')
        ax.set_xlim(0, self.y_dim)
        ax.set_ylim(0, self.x_dim)
        ax.invert_yaxis()

        plt.show()
    
    
# test init class
# game = GameOfLife(3, 4)
# print(game.x_dim)  # Output: 3
# print(game.y_dim)  # Output: 4
# print(game.life_grid)

# test get_grid
# grid = game.get_grid()
# print(grid)

# test print_grid
# game.print_grid()

# test populate_grid
# game = GameOfLife(4, 5)
# coords = [(0, 1), (1, 2), (2, 3)]
# game.populate_grid(coords)
# game.print_grid()

# test make_step
# game = GameOfLife(4, 5)
# coords = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
# game.populate_grid(coords)
# game.make_step()
# game.print_grid()

# test draw_grid
game = GameOfLife(4, 5)
coords = [(0, 1), (1, 2), (2, 0), (2, 1), (2, 2)]
game.populate_grid(coords)
game.make_n_steps(3)
game.draw_grid()
