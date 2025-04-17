from dijkstra_with_animation import dijkstra
from backtracking import solve_maze
from visualization import visualize_maze
from maze_generator import generate_maze
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
    # Generate a random maze
    width, height = 10, 10  # You can adjust the size of the maze
    maze = generate_maze(width, height)

    # Convert maze to graph for Dijkstra's algorithm
    graph = {}
    for y in range(height):
        for x in range(width):
            if maze[y][x] == 1:  # Only consider paths
                neighbors = []
                if x > 0 and maze[y][x - 1] == 1:
                    neighbors.append(((x - 1, y), 1))
                if x < width - 1 and maze[y][x + 1] == 1:
                    neighbors.append(((x + 1, y), 1))
                if y > 0 and maze[y - 1][x] == 1:
                    neighbors.append(((x, y - 1), 1))
                if y < height - 1 and maze[y + 1][x] == 1:
                    neighbors.append(((x, y + 1), 1))
                graph[(x, y)] = neighbors

    start_node = (1, 1)  # Starting point in the maze

    plt.figure()
    dijkstra(graph, start_node, visualize_callback=visualize_dijkstra)

    # Solve the maze using Backtracking algorithm
    solution = [[0] * width for _ in range(height)]
    if solve_maze(maze, 1, 1, solution):
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
