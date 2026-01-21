"""
Developed by - James R Terris
"""

from clrs.mst import kruskal, print_undirected_edges
from Task_2 import shortest_path_by_time
from Dataset import *
from clrs.adjacency_list_graph import AdjacencyListGraph
import Graph_Generation


def create_undirected_graph(line):
    """
    Create a graph using the list of stations and their connections
    :param line:
    :return graph of stations, list of vertices, list of edges:
    """
    vertices = []
    edges = line.station_connections
    logging.debug("generating graph...")

    for x in range(len(line.list_of_stations)):
        vertices.append(line.list_of_stations[x][0]) #Sepperate the station status boolean from station names

    graph1 = AdjacencyListGraph(len(vertices), False, True) #Create graph

    for edge in edges:
        graph1.insert_edge(vertices.index(edge[0]), vertices.index(edge[1]), edge[2]) #Add edges to the graph

    logging.debug("graph generated")
    return graph1, vertices, edges


def find_backbone(graph):
    logging.debug("running kruskal...")
    backbone = kruskal(graph)
    logging.debug("kruskal complete")
    return backbone

def find_removed_edges(graph, backbone):
    """
    Remove the shared tuples within both lists
    Return the remaining tuples not in the backbone graph
    """
    removed_edges = list(set(graph.get_edge_list()) - set(backbone.get_edge_list()))
    return  removed_edges

def print_removed_edges(edges, vertices):
    removed_edges = []
    for x in range(len(edges)):
        vertex1 = int(edges[x][0])#Remove value from tuple
        vertex2 = int(edges[x][1])# Remove value from tuple
        removed_edges.append(vertices[vertex1] + " --> " + vertices[vertex2]) #print values as a string
    print(",".join(removed_edges))
    print("number of removed edges:", len(removed_edges))

def total_weight_of_graph(graph):
    connections = 0
    for x in range(0, graph.get_card_E() - 1):
        for y in range(0, graph.get_card_E() - 1):
            edge = graph.find_edge(x, y)
            if edge is not None:
                connections += edge.weight
    print("total weight of graph:", connections)


def execute_task_4(data, print_data = True, testing = False):
    start = time.time()
    if not testing:
        graph, vertices, edges = create_undirected_graph(data)
        backbone = find_backbone(graph)
    else:
        vertices = []
        graph = data
        backbone = find_backbone(graph)
        for x in range(int(graph.get_card_V()) + 1):
            vertices.append(str(x))

    removed_edges = find_removed_edges(graph, backbone)

    if print_data:
            # print("Graph:")
            # print(graph.strmap(lambda i: vertices[i]))
            # print()
            # print("Backbone connections:")
            # print_undirected_edges(backbone, vertices)
            # print()
            print("Removed edges:")
            print_removed_edges(removed_edges, vertices)
            print()

    end = time.time()
    print("time for execution of task 4:", end - start)
    print()

    return [backbone, vertices]


"""
Run code
"""
if __name__ == "__main__":
    start = time.time()

    # simple_dataset = Line("Sample dataset", [["A", True], ["B", True], ["C", True], ["D", True], ["E", True], ["F", True]],
    #                       [("A", "B", 0), ("A", "C", 0), ("B", "D", 0), ("C", "D", 0), ("C", "E", 0), ("D", "F", 0), ("E", "F", 0)])
    #
    # execute_task_4(simple_dataset)

    # execute_task_4(sample_line)
    #
    # backbone = execute_task_4(Complete_Network, False)
    # backbone_graph = backbone[0]
    # total_weight_of_graph(backbone_graph)

    # backbone = execute_task_4(Complete_Network)

    backbone = execute_task_4(Complete_Network, True)
    shortest_path_by_time("Stratford", "Wimbledon", backbone, True, True)

    # print("generating graph")
    # data = Graph_Generation.create_random_graph(100)
    # print("graph generated")
    # execute_task_4(data, True)


    end = time.time()
    print()
    print("total runtime:", end-start)


"""
References:
testing, functions/parameters and examples from adjacency_list_graph and mst were used as inspiration and sources of information for how to develop our own solutions
graph.strmap(lambda i: vertices[i]) has been copied from code within mst.py from the clrs library
"""