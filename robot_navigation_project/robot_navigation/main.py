from dijkstra import dijkstra
from backtracking import solve_maze

def main():
    # Example graph for Dijkstra's algorithm
    graph = {
        'A': [('B', 1), ('C', 4)],
        'B': [('A', 1), ('C', 2), ('D', 5)],
        'C': [('A', 4), ('B', 2), ('D', 1)],
        'D': [('B', 5), ('C', 1)]
    }
    start_node = 'A'
    distances = dijkstra(graph, start_node)
    print(f"Shortest distances from {start_node}: {distances}")

    # Example maze for Backtracking algorithm
    maze = [[1, 0, 0, 0],
            [1, 1, 0, 1],
            [0, 1, 0, 0],
            [0, 1, 1, 1]]
    solution = [[0] * len(maze[0]) for _ in range(len(maze))]
    if solve_maze(maze, 0, 0, solution):
        print("Solution path:")
        for row in solution:
            print(row)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    main()
