import matplotlib.pyplot as plt

def visualize_maze(maze, solution):
    """
    Visualizes the maze and the solution path.
    
    :param maze: The maze represented as a 2D list.
    :param solution: The solution path represented as a 2D list.
    """
    plt.imshow(maze, cmap='gray_r')
    plt.imshow(solution, cmap='autumn', alpha=0.5)
    plt.title("Maze Visualization")
    plt.show()
