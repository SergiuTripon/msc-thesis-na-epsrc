#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
from igraph import *
from collections import OrderedDict

########################################################################################################################


# CalcStats class
class CalcStats:

    @staticmethod
    # runs other functions
    def run():

        # calculate basic stats
        CalcStats.calc_basic_stats('topics/current/network-a')
        CalcStats.calc_basic_stats('topics/current/network-b')
        CalcStats.calc_basic_stats('topics/past/1990-2000/network-a')
        CalcStats.calc_basic_stats('topics/past/1990-2000/network-b')
        CalcStats.calc_basic_stats('topics/past/2000-2010/network-a')
        CalcStats.calc_basic_stats('topics/past/2000-2010/network-b')

    ####################################################################################################################

    @staticmethod
    # calculates basic stats
    def calc_basic_stats(path):

        # variable to hold network
        network = Graph.Read_GraphML('../../data/networks/{}/network.graphml'.format(path))

        node_weights = network.vs["Num"]
        node_attr = network.vertex_attributes()
        node_degrees = network.degree()
        degree_dist = network.degree_distribution()
        edge_weights = network.es["weight"]
        edge_attr = network.edge_attributes()

        node_count = network.vcount()
        edge_count = network.ecount()
        directed_status = 'Directed' if network.is_directed() else 'Undirected'
        weighted_status = 'Yes' if network.is_weighted() else 'No'
        avg_degree = mean(network.degree())
        diameter = network.diameter(directed=False)
        radius = network.radius(mode='OUT')
        density = network.density()
        components = len(network.components())
        closeness = mean(network.closeness())
        node_betweenness = mean(network.betweenness(directed=False))
        edge_betweenness = mean(network.edge_betweenness(directed=False))
        avg_clustering_coeff = mean(network.transitivity_avglocal_undirected())
        eigenvector_centrality = mean(network.eigenvector_centrality(directed=False))
        avg_path_length = mean(network.average_path_length(directed=False))

        # print stats to terminal
        print('> Network Overview\n')
        print('- Nodes: {}'.format(node_count))
        print('- Edges: {}'.format(edge_count))
        print('- Type: {}'.format(directed_status))
        print('- Weighted: {}'.format(weighted_status))
        print('- Average Degree: {0:.3f}'.format(avg_degree))
        print('- Diameter: {}'.format(diameter))
        print('- Radius: {}'.format(radius))
        print('- Density: {0:.3f}'.format(density))
        print('- Weak Components: {}'.format(components))
        print('- Node Closeness: {0:.3f}'.format(closeness))
        print('- Node Betweenness: {0:.3f}'.format(node_betweenness))
        print('- Edge Betweenness: {0:.3f}\n'.format(edge_betweenness))

        print('> Node Overview\n')
        print('- Average Clustering Coefficient: {0:.3f}'.format(avg_clustering_coeff))
        print('- Eigenvector Centrality: {0:.3f}\n'.format(eigenvector_centrality))

        print('> Edge Overview\n')
        print('- Average Path Length: {0:.3f}'.format(avg_path_length))

        # get summary
        # summary(network)

        # print node attributes
        # print(node_attr)

        # print edge attributes
        # print(edge_attr)

        # print node degrees
        # print(node_degrees)

        # print degree distribution
        # print(degree_dist)

        # if stats file does not exist
        if not os.path.isfile('../../data/networks/{}/stats.txt'.format(path)):

            # variable to hold output file
            output_file = open('../../data/networks/{}/stats.txt'.format(path), mode='w')

            # write stats to file
            output_file.write('> Network Overview\n')
            output_file.write('- Nodes: {}'.format(node_count))
            output_file.write('- Edges: {}'.format(edge_count))
            output_file.write('- Type: {}'.format(directed_status))
            output_file.write('- Weighted: {}'.format(weighted_status))
            output_file.write('- Average Degree: {0:.3f}'.format(avg_degree))
            output_file.write('- Diameter: {}'.format(diameter))
            output_file.write('- Radius: {}'.format(radius))
            output_file.write('- Density: {0:.3f}'.format(density))
            output_file.write('- Weak Components: {}'.format(components))
            output_file.write('- Node Closeness: {0:.3f}'.format(closeness))
            output_file.write('- Node Betweenness: {0:.3f}'.format(node_betweenness))
            output_file.write('- Edge Betweenness: {0:.3f}\n'.format(edge_betweenness))

            output_file.write('> Node Overview\n')
            output_file.write('- Average Clustering Coefficient: {0:.3f}'.format(avg_clustering_coeff))
            output_file.write('- Eigenvector Centrality: {0:.3f}\n'.format(eigenvector_centrality))

            output_file.write('> Edge Overview\n')
            output_file.write('- Average Path Length: {0:.3f}\n'.format(avg_path_length))

            # close output file
            output_file.close()

        # if stats file does not exist
        if not os.path.isfile('../../data/networks/{}/network.pkl'.format(path)):

            # variable to hold output file
            output_file = open(r'../../data/networks/{}/network.pkl'.format(path), 'wb')
            # write network structure to file
            network.write_pickle(output_file)
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
