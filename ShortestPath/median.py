# Import required libraries
import math
import heapq

# Function to find the approximate location of the warehouse
def find_location(arr):
    x = []
    y = []

    for a, b in arr:
        x.append(a)
        y.append(b)

    # Calculate the median x-coordinate and y-coordinate
    x_coordinate = sorted(x)[len(x) // 2]
    y_coordinate = sorted(y)[len(y) // 2]

    return [x_coordinate, y_coordinate]


# Function to calculate the Euclidean distance between two nodes (points)
def distance_nodes(a1, a2):
    square = ((a1[0] - a2[0])**2 + (a1[1] - a2[1])**2)
    return math.sqrt(square)


# Function to find the shortest path from the warehouse to all factories and among factories
def dijkstra_shortest_path(factories, warehouse, myarr):
    graph = {}  

    # Initialize the graph with the warehouse and factories as nodes
    graph[warehouse] = {}
    for factory in factories:
        graph[factory] = {}

    # Create edges between factories and the warehouse using distance_nodes function above
    for factory in factories:
        for other_factory in factories:
            if factory != other_factory and (factory, other_factory) not in myarr:
                dist = distance_nodes(factory, other_factory)
                graph[factory][other_factory] = dist

    # Implementing Dijkstra's algorithm to calculate shortest paths
    distances = {node: float('inf') for node in graph}
    distances[warehouse] = 0
    heap = [(0, warehouse)]

    while heap:
        current_dist, current_node = heapq.heappop(heap)
        if current_dist > distances[current_node]:
            continue

        for neighbor, weight in graph[current_node].items():
            distance = current_dist + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(heap, (distance, neighbor))

    return distances


# Example usage of the functions and calculating the sum of all shortest distances
factories = [(1, 2), (3, 4), (5, 6), (7, 8)]
warehouse = tuple(find_location(factories))
myarr = []  

# Find the shortest distances using Dijkstra's algorithm
shortest_distances = dijkstra_shortest_path(factories, warehouse, myarr)

# Calculate the sum of all shortest distances
total_distance = 0
for key, val in shortest_distances.items():
    total_distance += val

print(total_distance)


# Overall Time Complexity: O((V + E) * log(V)), where V is the number of vertices (factories + warehouse) and E is the number of edges (connections between factories). The main contributor to the time complexity is the Dijkstra's algorithm implementation, which performs heap operations in log(V) time for each edge (E).
# Overall Space Complexity: O(V + E), where V is the number of vertices (factories + warehouse) and E is the number of edges (connections between factories). The space is used to store the graph representation and the distances dictionary.
