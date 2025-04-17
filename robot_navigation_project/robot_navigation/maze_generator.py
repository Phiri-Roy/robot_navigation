import random

def generate_maze(width, height):
    """
    Generates a random maze using the Recursive Backtracking algorithm.
    
    :param width: Width of the maze.
    :param height: Height of the maze.
    :return: A 2D list representing the maze (1 for path, 0 for wall).
    """
    maze = [[0] * width for _ in range(height)]
    
    def carve_passages_from(x, y):
        directions = [(0, 2), (2, 0), (0, -2), (-2, 0)]
        random.shuffle(directions)
        
        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height and maze[ny][nx] == 0:
                maze[y + dy // 2][x + dx // 2] = 1
                maze[ny][nx] = 1
                carve_passages_from(nx, ny)

    maze[1][1] = 1
    carve_passages_from(1, 1)
    return maze
