from dijkstra_with_animation import dijkstra
from backtracking import solve_maze
from visualization import visualize_maze
import matplotlib.pyplot as plt # type: ignore
from matplotlib.animation import FuncAnimation # type: ignore

def visualize_dijkstra(graph, visited, distances):
    plt.clf()
    for node in graph:
        color = 'blue' if node in visited else 'gray'
        plt.scatter(node[0], node[1], color=color)
        plt.text(node[0], node[1], f"{node}: {distances[node]}", fontsize=12, ha='center')
    plt.title("Dijkstra's Algorithm Visualization")
    plt.pause(0.5)

def main():
    # Example graph for Dijkstra's algorithm
    graph = {
        (0, 0): [((0, 1), 1), ((1, 0), 4)],
        (0, 1): [((0, 0), 1), ((0, 2), 2), ((1, 1), 5)],
        (0, 2): [((0, 1), 2), ((1, 2), 1)],
        (1, 0): [((0, 0), 4), ((1, 1), 1)],
        (1, 1): [((1, 0), 1), ((0, 1), 5), ((1, 2), 2)],
        (1, 2): [((1, 1), 2), ((0, 2), 1)]
    }
    start_node = (0, 0)

    plt.figure()
    dijkstra(graph, start_node, visualize_callback=visualize_dijkstra)

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
        visualize_maze(maze, solution)
    else:
        print("No solution exists.")

if __name__ == "__main__":
    plt.ion()  # Turn on interactive mode
    main()
    plt.ioff()  # Turn off interactive mode
    plt.show()  # Show the final plot
