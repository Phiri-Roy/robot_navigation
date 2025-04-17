def dijkstra(graph, start):
    """
    Implements Dijkstra's algorithm to find the shortest path in a graph.
    
    :param graph: A dictionary representing the graph where keys are node names and values are lists of tuples (neighbor, weight).
    :param start: The starting node for the pathfinding.
    :return: A dictionary with the shortest distance from the start node to each node.
    """
    import heapq

    queue = []
    heapq.heappush(queue, (0, start))
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0

    while queue:
        current_distance, current_node = heapq.heappop(queue)

        if current_distance > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(queue, (distance, neighbor))

    return distances
