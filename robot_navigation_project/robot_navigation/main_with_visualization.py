import random
from dijkstra import dijkstra
from backtracking import solve_maze
from visualization import visualize_maze

def generate_random_maze(size=4):
    return [[random.choice([0, 1]) for _ in range(size)] for _ in range(size)]

def main():
    # Example graph for Dijkstra's algorithm with random weights
    graph = {
        'A': [('B', random.randint(1, 10)), ('C', random.randint(1, 10))],
        'B': [('A', random.randint(1, 10)), ('C', random.randint(1, 10)), ('D', random.randint(1, 10))],
        'C': [('A', random.randint(1, 10)), ('B', random.randint(1, 10)), ('D', random.randint(1, 10))],
        'D': [('B', random.randint(1, 10)), ('C', random.randint(1, 10))]
    }
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    print(f"Shortest distances from {start_node}: {distances}")

    # Generate a random maze for Backtracking algorithm
    maze = generate_random_maze()
    maze[0][0] = 1  # Ensure the start position is walkable
    maze[-1][-1] = 1  # Ensure the exit is walkable
    
    solution = [[0] * len(maze[0]) for _ in range(len(maze))]
    if solve_maze(maze, 0, 0, solution):
        print("Solution path:")
        for row in solution:
            print(row)
        visualize_maze(maze, solution)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
