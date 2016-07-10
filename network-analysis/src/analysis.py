#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
import graphistry
import pandas as pd
from igraph import *

########################################################################################################################


# GetStats class
class GetStats:

    @staticmethod
    # gets network stats
    def get_network_stats():

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

# analyses network uses graphistry
def graphistry_analysis():

    # variable to hold API key
    api_key = 'cd97e75121bb38884873b5e6dd0b51222d2986658c51371ab94ba7dd060d93f15684fb8dbf128cbb7a63349ca9d02558'
    # set API key
    graphistry.register(key=api_key)

    # variable to hold edges
    edges = pd.read_csv('../../data/networks/areas/edges_graphistry.tsv', delimiter='\t', encoding='utf-8')

    # variable to hold plotter
    plotter = graphistry.bind(source="source", destination="target")
    # plot edges
    plotter.plot(edges)


########################################################################################################################


# main function
def main():

    # get network stats
    GetStats.get_network_stats()


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
