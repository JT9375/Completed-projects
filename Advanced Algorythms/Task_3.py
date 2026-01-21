"""
Developed by James R Terris
"""

from clrs.adjacency_list_graph import AdjacencyListGraph
from clrs.bfs import bfs
from Dataset import *
import random
from Graph_Generation import create_random_unweighted_graph


def create_graph(line):
    """
    Create a directional graph using the list of stations and their connections
    :param line:
    :return graph of stations, list of vertices, list of edges:
    """
    vertices = []
    edges = line.station_connections

    logging.debug("directed graph generating...")
    for x in range(len(line.list_of_stations)):
        vertices.append(line.list_of_stations[x][0]) #Sepperate the station status boolean from station names

    graph1 = AdjacencyListGraph(len(vertices), False, False) #Create graph

    for edge in edges:
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1])) #Add edges to the graph

    logging.debug("graph generated")
    return graph1, vertices, edges

def shortest_path_between_stations(line, source, destination, testing = False):
    start = time.time()
    path = []

    if not testing:
        graph, vertices, edges = create_graph(line)
        distance, pi = bfs(graph, vertices.index(source))
    else:
        distance, pi = bfs(line, int(source))
        vertices = []
        for x in range(int(line.get_card_V())):  # find number of vertices
            vertices.append(str(x))  # add vertex to list

    stations_visited = 0
    current = vertices.index(destination)  # Start at the destination
    while current is not None:
        stations_visited += 1
        path.insert(0, vertices[current])  # Add vertex to a list of visited stations
        current = pi[current]  # Assign current station to the station visited before the current station.
                                #  If no station before current None is returned

    print("Shortest path from", source, "to", destination + ":", " --> ".join(path))
    print("number of stations visited:", stations_visited)

    print()
    end = time.time()
    print("runtime:", end - start)

def test(number_of_tries):
    sizes = [100, 500, 1000, 1500, 2000, 2500]

    for n in sizes:
        total_time = 0
        for i in range(number_of_tries):
            graph = create_random_unweighted_graph(n)
            sv = random.randint(0, n-1)
            dv = random.randint(0, n-1)
            start = time.time()
            shortest_path_between_stations(graph, str(sv), str(dv), True)
            end = time.time()
            run_time = end - start
            total_time += run_time
            print(f" Run {i+1}: {run_time:.6f} seconds")
        average_time = total_time / number_of_tries
        print(f"Average runtime for n={n}: {average_time:.6f} seconds")
    print("Test complete")

if __name__ == "__main__":
    sample_data = Line("sample", [["A", True], ["B", True], ["C", True], ["D", True], ["E", True]],
                   [("A", "C", 0), ("A", "B", 0), ("B", "D", 0), ("C", "D", 0), ("C", "E", 0)])

    shortest_path_between_stations(sample_data, "B", "E")

    # s, c = create_complete_network()
    # Complete_Network = Line("Complete network", s, c)
    #
    # shortest_path_between_stations(Complete_Network, "Stratford", "Wimbledon")

    # shortest_path_between_stations(Piccadilly, "Covent Garden", "Green Park")

    # test(1)

"""
References:
testing, functions/parameters and examples from adjacency_list_graph and dijkstra were used as inspiration and sources of information for how to develop our own solutions
"""