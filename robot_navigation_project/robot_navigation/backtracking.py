def is_safe(maze, x, y):
    """
    Check if x and y are valid indexes for N*N maze.
    """
    return 0 <= x < len(maze) and 0 <= y < len(maze[0]) and maze[x][y] == 1

def solve_maze(maze, x, y, solution):
    """
    Solves the maze using backtracking.
    """
    if x == len(maze) - 1 and y == len(maze[0]) - 1:
        solution[x][y] = 1
        return True

    if is_safe(maze, x, y):
        solution[x][y] = 1

        if solve_maze(maze, x + 1, y, solution):
            return True

        if solve_maze(maze, x, y + 1, solution):
            return True

        solution[x][y] = 0
        return False

    return False
