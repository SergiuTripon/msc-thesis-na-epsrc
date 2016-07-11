#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
from igraph import Graph

########################################################################################################################


# calculates stats
def calc_stats():

    # variable to hold network
    network = Graph.Read_GraphML('../../data/networks/topics/current/network-a/nodes_edges.graphml')

    # get summary
    # summary(network)

    # print number of nodes
    print('Number of nodes: {}'.format(network.vcount()))

    # print number of edges
    print('Number of edges: {}'.format(network.ecount()))

    # print directed status
    print('Type: {}'.format('Undirected' if network.is_directed() == 'True' else 'Undirected'))

    # print weighted status
    print('Weighted: {}'.format('Yes' if network.is_weighted() == 'True' else 'No'))

    # print average node degree
    print('Average Node Degree: {}'.format(mean(network.degree())))

    # print diameter
    print('Network Diameter: {}'.format(network.diameter()))

    # print number of weakly connected components
    print('Number of weakly connected components: {}'.format(len(network.components())))

    # print node degrees
    # print(network.degree())

    # print degree distribution
    # print(network.degree_distribution())

    # set layout for network
    # network_layout = network.layout("fr")

    # plot network
    # plot(network, layout=network_layout, bbox=(3000, 2000), margin=20, keep_aspect_ratio=True, edge_curved=True)

########################################################################################################################


# main function
def main():

    # calculate stats
    calc_stats()


########################################################################################################################
