"""
Developed by James R Terris
"""
import logging
from clrs.generate_random_graph import generate_random_graph


def create_random_directional_graph(vertices):
    """Generate a directional graph of a user-defined number of vertex"""
    logging.debug("Generating directional graph")
    return generate_random_graph(vertices, 0.2, True, True, True,
                                 1, 20)

def create_random_graph(vertices):
    """Generate a graph with a user-defined number of vertex"""
    logging.debug("generating graph")
    return generate_random_graph(vertices, 0.2, True, False, True,
                                 1, 20)

def create_random_unweighted_graph(vertices):
    """Generate a graph with a user-defined number of vertex"""
    logging.debug("generating graph")
    return generate_random_graph(vertices, 0.2, True, False, False,
                                 1, 20)

if __name__ == "__main__":
    print(create_random_directional_graph(20))

