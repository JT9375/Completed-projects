"""
Developed by James R Terris
"""

from clrs.adjacency_list_graph import AdjacencyListGraph
from clrs.dijkstra import dijkstra
from Dataset import *


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

    graph1 = AdjacencyListGraph(len(vertices), False, True) #Create graph

    for edge in edges:
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2]) #Add edges to the graph

    logging.debug("graph generated")
    return graph1, vertices, edges


def shortest_path_by_time(source_vertex, destination_vertex, line, pre_generated_graph = False, backbone = False):
    """
    Find the shortest path between two stations
    :param source_vertex: searching from
    :param destination_vertex: searching to
    :param line: source data for your graph
    :param pre_generated_graph: True if inserting a pre-generated graph into the function. False if entering lists
    :param backbone: True if graph is the backbone generation
    :return All visited stations between the source and destination, the weight (time taken) to get between them:
    """
    start = time.time()
    logging.debug("running dijkstra's...")
    path = []
    if not pre_generated_graph:
        graph, vertices, edges = create_graph(line)
        d, pi = dijkstra(graph, vertices.index(source_vertex))
    elif pre_generated_graph and backbone:
            vertices = line[1]
            line = line[0]
            d, pi = dijkstra(line, vertices.index(source_vertex))
    else:
        d, pi = dijkstra(line, int(source_vertex))
        vertices = []
        for x in range(int(line.get_card_V())): #find number of vertices
            vertices.append(str(x)) #add vertex to list

    current = vertices.index(destination_vertex)  # Start at the destination
    while current is not None:
        path.insert(0, vertices[current]) #Add vertex to a list of visited stations
        current = pi[current] #Asign current station to the station visited before the current station.
                                # If no station before current None is returned
        logging.debug("Dijkstra's complete")

    end = time.time()

    print("Path from", source_vertex, "to", destination_vertex + ":", " --> ".join(path))
    print("Time between stations:", str(d[vertices.index(destination_vertex)]), "minuets")
    print("dijkstra's runtime:", end - start)



"""
Run code
"""
if __name__ == "__main__":
    start = time.time()



    # shortest_path_by_time("A", "E", sample_line)
    #
    # shortest_path_by_time("Covent Garden", "Green Park", Piccadilly)
    shortest_path_by_time("Stratford", "Wimbledon", Complete_Network)

    # n=1000
    # sv = random.randint(0, n)
    # dv = random.randint(0, n)
    # shortest_path_by_time(str(sv), str(dv), Graph_Generation.create_random_directional_graph(n), True)

    print()
    end = time.time()
    print("runtime:", end - start)


"""
References:
testing, functions/parameters and examples from adjacency_list_graph and dijkstra were used as inspiration and sources of information for how to develop our own solutions
"""