import heapq
import math

# ===========================
# 1. MAP DATA: LARGE MAP
# ===========================

taytay_graph = {
    'SM_Taytay': {'Tiangge': 10, 'NCBA': 15, 'Siena_College': 5, 'Robinsons_Cainta': 12, 'Highway_2000': 18},
    'Tiangge': {'SM_Taytay': 10, 'Public_Market': 5, 'Municipal_Hall': 8, 'Club_Manila_East': 6},
    'Public_Market': {'Tiangge': 5, 'Tres_Cruses': 12, 'Municipal_Hall': 4, 'Angono_Border': 18},
    'Municipal_Hall': {'Tiangge': 8, 'Public_Market': 4, 'NCBA': 10, 'Parola': 15, 'Barkadahan_Bridge': 20},
    'NCBA': {'SM_Taytay': 15, 'Municipal_Hall': 10, 'Tres_Cruses': 18},
    'Tres_Cruses': {'Public_Market': 12, 'NCBA': 18, 'Angono_Border': 14, 'Binangonan_Port': 35},
    'Siena_College': {'SM_Taytay': 5, 'Tikling': 20, 'Robinsons_Cainta': 10},
    'Club_Manila_East': {'Tiangge': 6, 'Tikling': 15, 'Muzon': 12},
    'Robinsons_Cainta': {'SM_Taytay': 12, 'Siena_College': 10, 'Junction_Cainta': 8, 'Greenwoods': 25},
    'Junction_Cainta': {'Robinsons_Cainta': 8, 'Ortigas_Ext': 10, 'Parola': 12, 'Sta_Lucia_Mall': 15},
    'Parola': {'Junction_Cainta': 12, 'Municipal_Hall': 15, 'Pasig_Border': 25, 'Barkadahan_Bridge': 10},
    'Ortigas_Ext': {'Junction_Cainta': 10, 'Tikling': 22, 'Pasig_Border': 18, 'Valley_Golf': 14},
    'Tikling': {'Siena_College': 20, 'Club_Manila_East': 15, 'Ortigas_Ext': 22, 'Ynares_Center': 15, 'Beverly_Hills': 12},
    'Ynares_Center': {'Tikling': 15, 'Antipolo_Cathedral': 10, 'Hinulugang_Taktak': 8, 'Shopwise_Antipolo': 5},
    'Antipolo_Cathedral': {'Ynares_Center': 10, 'Pinto_Art_Museum': 12, 'Teresa_Boundary': 25},
    'Angono_Border': {'Public_Market': 18, 'Tres_Cruses': 14, 'SM_Angono': 10, 'Angono_Petroglyphs': 22},
    'Pasig_Border': {'Parola': 25, 'Ortigas_Ext': 18, 'Rosario': 15},
    'Barkadahan_Bridge': {'Municipal_Hall': 20, 'Parola': 10, 'Napindan': 15},
    'Highway_2000': {'SM_Taytay': 18, 'Muzon': 10, 'Barkadahan_Bridge': 12},
    'Muzon': {'Club_Manila_East': 12, 'Highway_2000': 10, 'Angono_Border': 15},
    'Sta_Lucia_Mall': {'Junction_Cainta': 15, 'Marcos_Highway': 10},
    'Marcos_Highway': {'Sta_Lucia_Mall': 10, 'Masinag': 15},
    'Masinag': {'Marcos_Highway': 15, 'Sumulong_Highway': 12},
    'Sumulong_Highway': {'Masinag': 12, 'Valley_Golf': 15, 'Antipolo_Cathedral': 20},
    'Valley_Golf': {'Ortigas_Ext': 14, 'Sumulong_Highway': 15, 'Beverly_Hills': 10},
    'Beverly_Hills': {'Tikling': 12, 'Valley_Golf': 10, 'Hinulugang_Taktak': 18},
    'Hinulugang_Taktak': {'Ynares_Center': 8, 'Beverly_Hills': 18},
    'Shopwise_Antipolo': {'Ynares_Center': 5, 'Teresa_Boundary': 15},
    'Pinto_Art_Museum': {'Antipolo_Cathedral': 12, 'Shopwise_Antipolo': 10},
    'Teresa_Boundary': {'Antipolo_Cathedral': 25, 'Shopwise_Antipolo': 15, 'Morong': 30},
    'SM_Angono': {'Angono_Border': 10, 'Binangonan_Port': 20},
    'Angono_Petroglyphs': {'Angono_Border': 22, 'Binangonan_Port': 25},
    'Binangonan_Port': {'Tres_Cruses': 35, 'SM_Angono': 20, 'Angono_Petroglyphs': 25},
    'Greenwoods': {'Robinsons_Cainta': 25, 'Pasig_Border': 12},
    'Rosario': {'Pasig_Border': 15, 'Ortigas_Ext': 20},
    'Napindan': {'Barkadahan_Bridge': 15, 'Greenwoods': 20},
    'Morong': {'Teresa_Boundary': 30}
}

taytay_coords = {
    'SM_Taytay': (0, 10), 'Tiangge': (5, 8), 'Public_Market': (6, 5), 'Municipal_Hall': (4, 4), 
    'NCBA': (2, 2), 'Tres_Cruses': (10, 0), 'Siena_College': (1, 14), 'Club_Manila_East': (8, 12),
    'Robinsons_Cainta': (-4, 12), 'Junction_Cainta': (-8, 15), 'Parola': (-6, 5), 'Ortigas_Ext': (-10, 18),
    'Tikling': (12, 18), 'Ynares_Center': (18, 24), 'Antipolo_Cathedral': (22, 26), 'Angono_Border': (10, -8),
    'Pasig_Border': (-15, 10), 'Barkadahan_Bridge': (-2, 0), 'Highway_2000': (2, -2), 'Muzon': (8, 2),
    'Sta_Lucia_Mall': (-12, 25), 'Marcos_Highway': (-10, 30), 'Masinag': (-5, 32), 'Sumulong_Highway': (5, 30),
    'Valley_Golf': (2, 22), 'Beverly_Hills': (8, 22), 'Hinulugang_Taktak': (15, 28), 'Shopwise_Antipolo': (20, 22),
    'Pinto_Art_Museum': (24, 22), 'Teresa_Boundary': (30, 20), 'SM_Angono': (12, -15), 
    'Angono_Petroglyphs': (20, -10), 'Binangonan_Port': (18, -25), 'Greenwoods': (-12, 5),
    'Rosario': (-20, 15), 'Napindan': (-8, -5), 'Morong': (40, 15)
}

# ===========================
# 2. ALGORITHMS
# ===========================

# 2.1 The Dijkstra Algorithm Function
def dijkstra(graph, start, destination):
    # Initialization
    # Set all distances to infinity, except the start node which is 0
    distances = {node: float('infinity') for node in graph}
    distances[start] = 0
    
    # Keep track of the path so we can reconstruct it later
    previous_nodes = {node: None for node in graph}
    
    # Priority queue to process nodes based on lowest current cost
    # Format: (current_distance, node_name)
    priority_queue = [(0, start)]
    
    # The Core Loop
    while priority_queue:
        # Pop the node with the lowest distance from the queue
        current_distance, current_node = heapq.heappop(priority_queue)
        
        # If we reached the destination, we can stop searching
        if current_node == destination:
            break
            
        # Optimization: If we found a shorter path previously, skip this one
        if current_distance > distances[current_node]:
            continue
            
        # Check all neighboring nodes connected to the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the total distance to this neighbor
            distance = current_distance + weight
            
            # If we found a shorter path to the neighbor, update it
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                previous_nodes[neighbor] = current_node
                # Push the updated distance and neighbor into the queue
                heapq.heappush(priority_queue, (distance, neighbor))
                
    # Path Reconstruction
    path = []
    current = destination
    
    # Trace backward from the destination using the previous_nodes dictionary
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]
        
    # If the start node isn't in the path, it means no path exists
    if path[0] == start:
        return path, distances[destination]
    else:
        return None, float('infinity')

# 2.2 The Heuristic Helper Function
def calculate_heuristic(node_name, destination_name, coords):
    """
    Calculates the straight-line distance between two points using the Euclidean formula.
    This is the h(n) in the A* equation: f(n) = g(n) + h(n)
    """
    x1, y1 = coords[node_name]
    x2, y2 = coords[destination_name]
    
    # Euclidean distance formula: sqrt((x2 - x1)^2 + (y2 - y1)^2)
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 2.3 The A* Algorithm Function
def a_star(graph, coords, start, destination):
    # g_score: The exact travel time from the start node to the current node.
    # We initialize all to infinity, except the start node.
    g_scores = {node: float('infinity') for node in graph}
    g_scores[start] = 0
    
    # f_score: The total estimated cost (g_score + heuristic).
    # This is what the priority queue uses to decide where to go next.
    f_scores = {node: float('infinity') for node in graph}
    f_scores[start] = calculate_heuristic(start, destination, coords)
    
    # Dictionary to keep track of our path (the breadcrumbs)
    previous_nodes = {node: None for node in graph}
    
    # Priority queue stores tuples of: (f_score, node_name)
    priority_queue = [(f_scores[start], start)]
    
    # The Core Loop
    while priority_queue:
        # Pop the node with the lowest f_score (the most promising path)
        current_f_score, current_node = heapq.heappop(priority_queue)
        
        # If we reached the destination, stop searching!
        if current_node == destination:
            break
            
        # Check all neighboring nodes connected to the current node
        for neighbor, weight in graph[current_node].items():
            # Calculate the tentative g_score (actual travel time to get to this neighbor)
            tentative_g_score = g_scores[current_node] + weight
            
            # If this new path is faster than any previous path we found to this neighbor:
            if tentative_g_score < g_scores[neighbor]:
                # Update our breadcrumbs
                previous_nodes[neighbor] = current_node
                
                # Update the g_score (actual cost)
                g_scores[neighbor] = tentative_g_score
                
                # Calculate and update the f_score (actual cost + heuristic guess)
                h_score = calculate_heuristic(neighbor, destination, coords)
                f_scores[neighbor] = tentative_g_score + h_score
                
                # Add the neighbor to the queue to be explored
                heapq.heappush(priority_queue, (f_scores[neighbor], neighbor))
                
    # Path Reconstruction
    path = []
    current = destination
    
    # Trace backward from the destination using the previous_nodes dictionary
    while current is not None:
        path.insert(0, current)
        current = previous_nodes[current]
        
    # If the start node isn't in the path, it means no path exists
    if path[0] == start:
        # We return the path, and the actual total travel time (the g_score of the destination)
        return path, g_scores[destination]
    else:
        return None, float('infinity')

# ===========================
# 3. USER INTERFACE
# ===========================

def main():

    while True:

        print("""
==========================
        SELECT MODE
==========================
1: Dijkstra's Algorithm
2: A* Algorithm
==========================
            """)

        try:
            mode : int = int(input("Enter number (1 or 2): "))
            if mode in [1, 2]:
                break
            else:
                print("Error: Please select 1 or 2.")
        except ValueError:
            print("Error: Invalid input. Please enter a number.")

    print("""
==========================
      PLACES (LARGE)
==========================
SM_Taytay
Tiangge
Public_Market
Municipal_Hall
NCBA
Tres_Cruses
Siena_College
Club_Manila_East
Robinsons_Cainta
Junction_Cainta
Parola
Ortigas_Ext
Tikling
Ynares_Center
Antipolo_Cathedral
Angono_Border
Pasig_Border
Barkadahan_Bridge
Highway_2000
Muzon
Sta_Lucia_Mall
Marcos_Highway
Masinag
Sumulong_Highway
Valley_Golf
Beverly_Hills
Hinulugang_Taktak
Shopwise_Antipolo
Pinto_Art_Museum
Teresa_Boundary
SM_Angono
Angono_Petroglyphs
Binangonan_Port
Greenwoods
Rosario
Napindan
Morong
==========================
        """)
    
    start_location = input("input start location: ")
    end_location = input("input end location: ")
    print("")

    if mode == 1:
        shortest_path, total_time = dijkstra(taytay_graph, start_location, end_location)

        print(f"Shortest Path from {start_location} to {end_location}: {' -> '.join(shortest_path)}")
        print(f"Total Travel Time: {total_time} minutes")

    elif mode == 2:
        shortest_path, total_time = a_star(taytay_graph, taytay_coords, start_location, end_location)

        print(f"A* Path: {' -> '.join(shortest_path)} | Time: {total_time} mins")

# ===========================
# 4. RUN PROGRAM
# ===========================

if __name__ == "__main__":
    main()