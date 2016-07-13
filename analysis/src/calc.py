#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
import os
import igraph as ig
import networkx as nx
from collections import OrderedDict

########################################################################################################################


# CalcStats class
class CalcStats:

    @staticmethod
    # runs other functions
    def run():

        # calculate basic stats
        CalcStats.calc_basic_stats('topics/current/network-a')
        # CalcStats.calc_basic_stats('topics/current/network-b')
        # CalcStats.calc_basic_stats('topics/past/2000-2010/network-a')
        # CalcStats.calc_basic_stats('topics/past/2000-2010/network-b')
        # CalcStats.calc_basic_stats('topics/past/1990-2000/network-a')
        # CalcStats.calc_basic_stats('topics/past/1990-2000/network-b')

        # CalcStats.calc_basic_stats('researchers/current/network-a')
        # CalcStats.calc_basic_stats('researchers/current/network-b')
        # CalcStats.calc_basic_stats('researchers/past/2000-2010/network-a')
        # CalcStats.calc_basic_stats('researchers/past/2000-2010/network-b')
        # CalcStats.calc_basic_stats('researchers/past/1990-2000/network-a')
        # CalcStats.calc_basic_stats('researchers/past/1990-2000/network-b')

    ####################################################################################################################

    @staticmethod
    # calculates basic stats
    def calc_basic_stats(path):

        # variable to hold network
        ig_network = ig.Graph.Read_GraphML('../../data/networks/{}/network.graphml'.format(path))

        # variable to hold network1
        nx_network = nx.read_graphml('../../data/networks/{}/network.graphml'.format(path))

        # variables to hold selectables
        network_summary = ig_network.summary()
        node_weights = ig_network.vs["Num"]
        node_attr = ig_network.vertex_attributes()
        node_degrees = ig_network.degree()
        degree_dist = ig_network.degree_distribution()
        edge_weights = ig_network.es["weight"]
        edge_attr = ig_network.edge_attributes()

        # variables to hold stats
        node_count = ig_network.vcount()
        edge_count = ig_network.ecount()
        directed_status = 'Directed' if ig_network.is_directed() else 'Undirected'
        weighted_status = 'Yes' if ig_network.is_weighted() else 'No'
        connected_status = 'Yes' if ig_network.is_connected() else 'No'
        avg_degree = ig.mean(ig_network.degree(loops=False))
        avg_weighted_degree = ig.mean(ig_network.strength(weights='weight'))
        diameter = ig_network.diameter(directed=False, weights='weight')
        radius = ig_network.radius(mode='ALL')
        density = ig_network.density()
        modularity = ig_network.modularity(ig_network.community_multilevel(weights='weight'))
        communities = len(ig_network.community_multilevel(weights='weight'))
        components = len(ig_network.components())
        closeness = ig.mean(ig_network.closeness(weights='weight'))
        node_betweenness = ig.mean(ig_network.betweenness(directed=False, weights='weight'))
        edge_betweenness = ig.mean(ig_network.edge_betweenness(directed=False, weights='weight'))
        avg_clustering_coeff = ig.mean(ig_network.transitivity_avglocal_undirected())
        eigenvector_centrality = ig.mean(ig_network.eigenvector_centrality(directed=False, weights='weight'))
        avg_path_length = ig.mean(ig_network.average_path_length(directed=False))

        # print stats to terminal
        print('> Network Overview\n')
        print('- Nodes: {}'.format(node_count))
        print('- Edges: {}'.format(edge_count))
        print('- Type: {}'.format(directed_status))
        print('- Weighted: {}'.format(weighted_status))
        print('- Connected: {}'.format(connected_status))
        print('- Average Degree: {0:.3f}'.format(avg_degree))
        print('- Average Weighted Degree: {0:.3f}'.format(avg_weighted_degree))
        print('- Diameter: {}'.format(diameter))
        print('- Radius: {}'.format(radius))
        print('- Density: {0:.3f}'.format(density))
        print('- Modularity: {0:.3f}'.format(modularity))
        print('- Communities: {}'.format(communities))
        print('- Weak Components: {}'.format(components))
        print('- Node Closeness: {0:.3f}'.format(closeness))
        print('- Node Betweenness: {0:.3f}'.format(node_betweenness))
        print('- Edge Betweenness: {0:.3f}\n'.format(edge_betweenness))

        print('> Node Overview\n')
        print('- Average Clustering Coefficient: {0:.3f}'.format(avg_clustering_coeff))
        print('- Eigenvector Centrality: {0:.3f}\n'.format(eigenvector_centrality))

        print('> Edge Overview\n')
        print('- Average Path Length: {0:.3f}'.format(avg_path_length))

        # if stats file does not exist
        if not os.path.isfile('../../data/networks/{}/stats.txt'.format(path)):

            # variable to hold output file
            output_file = open('../../data/networks/{}/stats.txt'.format(path), mode='w')

            # write stats to file
            output_file.write('> Network Overview\n\n')
            output_file.write('- Nodes: {}\n'.format(node_count))
            output_file.write('- Edges: {}\n'.format(edge_count))
            output_file.write('- Type: {}\n'.format(directed_status))
            output_file.write('- Weighted: {}\n'.format(weighted_status))
            output_file.write('- Average Degree: {0:.3f}\n'.format(avg_degree))
            output_file.write('- Average Weighted Degree: {0:.3f}\n'.format(avg_weighted_degree))
            output_file.write('- Diameter: {}\n'.format(diameter))
            output_file.write('- Radius: {}\n'.format(radius))
            output_file.write('- Density: {0:.3f}\n'.format(density))
            output_file.write('- Modularity: {0:.3f}\n'.format(modularity))
            output_file.write('- Communities: {}\n'.format(communities))
            output_file.write('- Weak Components: {}\n'.format(components))
            output_file.write('- Node Closeness: {0:.3f}\n'.format(closeness))
            output_file.write('- Node Betweenness: {0:.3f}\n'.format(node_betweenness))
            output_file.write('- Edge Betweenness: {0:.3f}\n\n'.format(edge_betweenness))

            output_file.write('> Node Overview\n\n')
            output_file.write('- Average Clustering Coefficient: {0:.3f}\n'.format(avg_clustering_coeff))
            output_file.write('- Eigenvector Centrality: {0:.3f}\n\n'.format(eigenvector_centrality))

            output_file.write('> Edge Overview\n\n')
            output_file.write('- Average Path Length: {0:.3f}'.format(avg_path_length))

            # close output file
            output_file.close()

        # if stats file does not exist
        if not os.path.isfile('../../data/networks/{}/network.pkl'.format(path)):

            # variable to hold output file
            output_file = open(r'../../data/networks/{}/network.pkl'.format(path), 'wb')
            # write network structure to file
            ig_network.write_pickle(output_file)
            # close output file
            output_file.close()


########################################################################################################################


# main function
def main():

    # calculate stats
    CalcStats.run()


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
