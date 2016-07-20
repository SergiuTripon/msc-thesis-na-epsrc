#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
import os
import pandas as pd
import igraph as ig
import networkx as nx
import graphistry as gp
from copy import deepcopy
from random import randint

# increase arpack iterations
ig.arpack_options.maxiter = 300000

# variable to hold graphistry api key
api_key = 'cd97e75121bb38884873b5e6dd0b51222d2986658c51371ab94ba7dd060d93f15684fb8dbf128cbb7a63349ca9d02558'

# set api key
gp.register(key=api_key)

########################################################################################################################


# AnalyseTopicNetwork class
class AnalyseTopicNetwork:

    @staticmethod
    # runs other functions
    def run():

        # analyse network a
        # AnalyseTopicNetwork.analyse_network_a('topics/current/network-a')
        # AnalyseTopicNetwork.analyse_network_a('topics/past/2000-2010/network-a')
        # AnalyseTopicNetwork.analyse_network_a('topics/past/1990-2000/network-a')

        # analyse network b
        # AnalyseTopicNetwork.analyse_network_b('topics/current/network-b')
        # AnalyseTopicNetwork.analyse_network_b('topics/past/2000-2010/network-b')
        AnalyseTopicNetwork.analyse_network_b('topics/past/1990-2000/network-b')

    ####################################################################################################################

    @staticmethod
    # analyses network a
    def analyse_network_a(path):

        # variable to hold network
        network = ig.Graph.Read_GraphML('../../data/networks/{}/network.graphml'.format(path))

        # calculate network stats
        calc_stats(network, path)

        # calculate modularity
        calc_modularity(network, path)

        # add normalized node number column to network
        network.vs['NormNum'] = norm_vals(network.vs['Num'], 20, 60)
        # add normalized node value column to network
        network.vs['NormVal'] = norm_vals(network.vs['Val'], 20, 60)

        # add normalized edge weight column to network
        network.es['NormWeight'] = norm_vals(network.es['weight'], 1, 10)
        # add normalized edge value column to network
        network.es['NormVal'] = norm_vals(network.es['Val'], 1, 10)

        # plot network
        plot_network(network, path)

        # variable to hold louvain
        louvain = network.community_multilevel(weights='weight')

        # variable to hold communities
        communities = louvain

        # save communities
        save_communities(network, communities, path, 0)

        # plot communities
        plot_communities(network, communities, communities.membership, path, True)

        # analyse sub-communities
        analyse_sub_communities(path, len(communities) + 1)

    ####################################################################################################################

    @staticmethod
    # analyses network b
    def analyse_network_b(path):

        # variable to hold network
        network = ig.Graph.Read_GraphML('../../data/networks/{}/network.graphml'.format(path))

        # calculate network stats
        calc_stats(network, path)

        # calculate modularity
        calc_modularity(network, path)

        # add normalized node number column to network
        network.vs['NormNum'] = norm_vals(network.vs['Num'], 20, 60)

        # add normalized edge weight column to network
        network.es['NormWeight'] = norm_vals(network.es['weight'], 1, 10)

        # plot network
        plot_network(network, path)

        # variable to hold louvain
        louvain = network.community_multilevel(weights='weight')

        # variable to hold communities
        communities = louvain

        # save communities
        save_communities(network, communities, path, 0)

        # plot communities
        plot_communities(network, communities, communities.membership, path, True)

        # analyse sub-communities
        analyse_sub_communities(path, len(communities) + 1)

########################################################################################################################


# AnalyseResearcherNetwork class
class AnalyseResearcherNetwork:

    @staticmethod
    # runs other functions
    def run():

        # analyse network a
        AnalyseResearcherNetwork.analyse_network_a('researchers/current/network-a', 20)
        AnalyseResearcherNetwork.analyse_network_a('researchers/past/2000-2010/network-a', 20)
        AnalyseResearcherNetwork.analyse_network_a('researchers/past/1990-2000/network-a', 20)

        # analyse network b
        # AnalyseResearcherNetwork.analyse_network_b('researchers/current/network-b', 9)
        # AnalyseResearcherNetwork.analyse_network_b('researchers/past/2000-2010/network-b', 30)
        AnalyseResearcherNetwork.analyse_network_b('researchers/past/1990-2000/network-b', 20)

    ####################################################################################################################

    @staticmethod
    # analyses network a
    def analyse_network_a(path, threshold):

        # variable to hold network
        network = ig.Graph.Read_GraphML('../../data/networks/{}/network.graphml'.format(path))

        # calculate network stats
        calc_stats(network, path)

        # calculate modularity
        calc_modularity(network, path)

        # add normalized node number column to network
        network.vs['NormNum'] = norm_vals(network.vs['Num'], 20, 60)

        # add normalized edge weight column to network
        network.es['NormWeight'] = norm_vals(network.es['weight'], 1, 10)

        # plot network
        plot_network(network, path)

        # variable to hold louvain
        louvain = network.community_multilevel(weights='weight')

        # variable to hold communities
        communities = louvain

        # save communities
        save_communities(network, communities, path, threshold)

        # plot communities
        plot_communities(network, communities, communities.membership, path, True)

    ####################################################################################################################

    @staticmethod
    # analyses network b
    def analyse_network_b(path, threshold):

        # variable to hold network
        network = ig.Graph.Read_GraphML('../../data/networks/{}/network.graphml'.format(path))

        # calculate network stats
        calc_stats(network, path)

        # calculate modularity
        calc_modularity(network, path)

        # add normalized node number column to network
        network.vs['NormNum'] = norm_vals(network.vs['Num'], 20, 60)
        # add normalized node value column to network
        network.vs['NormVal'] = norm_vals(network.vs['Val'], 20, 60)

        # add normalized edge weight column to network
        network.es['NormWeight'] = norm_vals(network.es['weight'], 1, 10)
        # add normalized edge value column to network
        network.es['NormVal'] = norm_vals(network.es['Val'], 1, 10)

        # plot network
        plot_network(network, path)

        # variable to hold louvain
        louvain = network.community_multilevel(weights='weight')

        # variable to hold communities
        communities = louvain

        # save communities
        save_communities(network, communities, path, threshold)

        # plot communities
        plot_communities(network, communities, communities.membership, path, True)


########################################################################################################################


# calculates stats
def calc_stats(network, path):

    # if stats file does not exist
    if not os.path.isfile('../../data/networks/{}/stats.txt'.format(path)):

        # variables to hold selectables
        network_summary = network.summary()
        node_weights = network.vs["Num"]
        node_attr = network.vertex_attributes()
        node_degrees = network.degree()
        degree_dist = network.degree_distribution()
        edge_weights = network.es["weight"]
        edge_attr = network.edge_attributes()

        # variables to hold stats
        node_count = network.vcount()
        edge_count = network.ecount()
        directed_status = 'Directed' if network.is_directed() else 'Undirected'
        weighted_status = 'Yes' if network.is_weighted() else 'No'
        connected_status = 'Yes' if network.is_connected() else 'No'
        avg_degree = ig.mean(network.degree(loops=False))
        avg_weighted_degree = ig.mean(network.strength(weights='weight'))
        diameter = network.diameter(directed=False, weights='weight')
        radius = network.radius(mode='ALL')
        density = network.density()
        modularity = network.community_multilevel(weights='weight').modularity
        communities = len(network.community_multilevel(weights='weight'))
        components = len(network.components())
        closeness = ig.mean(network.closeness(weights='weight'))
        node_betweenness = ig.mean(network.betweenness(directed=False, weights='weight'))
        edge_betweenness = ig.mean(network.edge_betweenness(directed=False, weights='weight'))
        avg_clustering_coeff = ig.mean(network.transitivity_avglocal_undirected())
        eigenvector_centrality = ig.mean(network.eigenvector_centrality(directed=False, weights='weight'))
        avg_path_length = ig.mean(network.average_path_length(directed=False))

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

        # variable to hold output file
        output_file = open('../../data/networks/{}/stats.txt'.format(path), mode='w')

        # write stats to file
        output_file.write('> Network Overview\n\n')
        output_file.write('- Nodes: {}\n'.format(node_count))
        output_file.write('- Edges: {}\n'.format(edge_count))
        output_file.write('- Type: {}\n'.format(directed_status))
        output_file.write('- Weighted: {}\n'.format(weighted_status))
        output_file.write('- Connected: {}\n'.format(connected_status))
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
        output_file.write('- Average Path Length: {0:.3f}\n'.format(avg_path_length))

        # close output file
        output_file.close()


########################################################################################################################


# calculate modularity
def calc_modularity(network, path):

    # if modularity file does not exist
    if not os.path.isfile('../../data/networks/{}/modularity.txt'.format(path)):

        # variable to hold infomap communities
        infomap_communities = network.community_infomap(edge_weights='weight')
        # variable to hold infomap modularity
        infomap_modularity = infomap_communities.modularity

        spinglass_communities = ig.VertexClustering
        spinglass_modularity = float

        # if network is connected
        if network.is_connected():
            # variable to hold spinglass communities
            spinglass_communities = network.community_spinglass(weights='weight')
            # variable to hold spinglass modularity
            spinglass_modularity = spinglass_communities.modularity

        # variable to hold louvain communities
        louvain_communities = network.community_multilevel(weights='weight')
        # variable to hold louvain modularity
        louvain_modularity = louvain_communities.modularity

        # variable to hold label propagation communities
        label_propagation_communities = network.community_label_propagation(weights='weight')
        # variable to hold label propagation modularity
        label_propagation_modularity = label_propagation_communities.modularity

        # variable to hold leading eigenvector communities
        leading_eigenvector_communities = network.community_leading_eigenvector(weights='weight')
        # variable to hold leading eigenvector modularity
        leading_eigenvector_modularity = leading_eigenvector_communities.modularity

        # variable to hold walktrap communities
        walktrap_communities = network.community_walktrap(weights='weight', steps=4).as_clustering()
        # variable to hold walktrap modularity
        walktrap_modularity = walktrap_communities.modularity

        # variable to hold fast greedy communities
        fastgreedy_communities = network.community_fastgreedy(weights='weight').as_clustering()
        # variable to hold fast greedy modularity
        fastgreedy_modularity = fastgreedy_communities.modularity

        edge_betweenness_communities = ig.VertexClustering
        edge_betweenness_modularity = float

        # if network is connected and number of components is less than or equal to 2
        if network.is_connected() or len(network.components()) <= 2:
            # variable to hold edge betweenness communities
            edge_betweenness_communities = network.community_edge_betweenness(directed=False,
                                                                              weights='weight').as_clustering()
            # variable to hold edge betweenness modularity
            edge_betweenness_modularity = edge_betweenness_communities.modularity

        # print stats to terminal
        print('Infomap Communities:             {}'.format(len(infomap_communities)))

        # if network is connected
        if network.is_connected():
            print('Spinglass Communities:           {}'.format(len(spinglass_communities)))

        print('Louvain Communities:             {}'.format(len(louvain_communities)))
        print('Label Propagation Communities:   {}'.format(len(label_propagation_communities)))
        print('Leading Eigenvector Communities: {}'.format(len(leading_eigenvector_communities)))
        print('Walktrap Modularity:             {}'.format(len(walktrap_communities)))
        print('Fast Greedy Communities:         {}'.format(len(fastgreedy_communities)))

        # if network is connected and number of components is less than or equal to 2
        if network.is_connected() or len(network.components()) <= 2:
            print('Edge Betweenness Communities:    {}\n'.format(len(edge_betweenness_communities)))

        print('Infomap Modularity:              {0:.3f}'.format(infomap_modularity))

        # if network is connected
        if network.is_connected():
            print('Spinglass Modularity:            {0:.3f}'.format(spinglass_modularity))

        print('Louvain Modularity:              {0:.3f}'.format(louvain_modularity))
        print('Label Propagation Modularity:    {0:.3f}'.format(label_propagation_modularity))
        print('Leading Eigenvector Modularity:  {0:.3f}'.format(leading_eigenvector_modularity))
        print('Walktrap Modularity:             {0:.3f}'.format(walktrap_modularity))
        print('Fast Greedy Modularity:          {0:.3f}'.format(fastgreedy_modularity))

        # if network is connected and number of components is less than or equal to 2
        if network.is_connected() or len(network.components()) <= 2:
            print('Edge Betweenness Communities:    {0:.3f}'.format(edge_betweenness_modularity))

        # variable to hold output file
        output_file = open('../../data/networks/{}/modularity.txt'.format(path), mode='w')

        # write stats to file
        output_file.write('Infomap Communities:             {}\n'.format(len(infomap_communities)))

        # if network is connected
        if network.is_connected():
            output_file.write('Spinglass Communities:           {}\n'.format(len(spinglass_communities)))

        output_file.write('Louvain Communities:             {}\n'.format(len(louvain_communities)))
        output_file.write('Label Propagation Communities:   {}\n'.format(len(label_propagation_communities)))
        output_file.write('Leading Eigenvector Communities: {}\n'.format(len(leading_eigenvector_communities)))
        output_file.write('Walktrap Modularity:             {}\n'.format(len(walktrap_communities)))
        output_file.write('Fast Greedy Communities:         {}\n'.format(len(fastgreedy_communities)))

        # if network is connected and number of components is less than or equal to 2
        if network.is_connected() or len(network.components()) <= 2:
            output_file.write('Edge Betweenness Communities:    {}\n\n'.format(len(edge_betweenness_communities)))

        output_file.write('Infomap Modularity:              {0:.3f}\n'.format(infomap_modularity))

        # if network is connected
        if network.is_connected():
            output_file.write('Spinglass Modularity:            {0:.3f}\n'.format(spinglass_modularity))

        output_file.write('Louvain Modularity:              {0:.3f}\n'.format(louvain_modularity))
        output_file.write('Label Propagation Modularity:    {0:.3f}\n'.format(label_propagation_modularity))
        output_file.write('Leading Eigenvector Modularity:  {0:.3f}\n'.format(leading_eigenvector_modularity))
        output_file.write('Walktrap Modularity:             {0:.3f}\n'.format(walktrap_modularity))
        output_file.write('Fast Greedy Modularity:          {0:.3f}\n'.format(fastgreedy_modularity))

        # if network is connected and number of components is less than or equal to 2
        if network.is_connected() or len(network.components()) <= 2:
            output_file.write('Edge Betweenness Communities:    {0:.3f}'.format(edge_betweenness_modularity))


########################################################################################################################


# normalizes values
def norm_vals(vals, new_min, new_max):

    # variable to hold old minimum and maximum
    old_min, old_max = min(vals), max(vals)
    # variable to hold old and new range
    old_range, new_range = old_max - old_min, new_max - new_min

    int_vals = [int(val) for val in vals]

    # variable to hold new values
    new_vals = [round((((val - old_min) * new_range / old_range) + new_min), 0) for val in int_vals]

    # return new values
    return new_vals


########################################################################################################################


# plots network
def plot_network(network, path):

    # if network plot file does not exist
    if not os.path.isfile('../../data/networks/{}/network.png'.format(path)):

        # variable to hold visual style
        visual_style = {'vertex_label': None,
                        'vertex_color': 'blue',
                        'vertex_size': network.vs['NormNum'],
                        'edge_width': network.es['NormWeight'],
                        'layout': 'kk',
                        'bbox': (1000, 1000),
                        'margin': 40}

        # plot network
        ig.plot(network, '../../data/networks/{}/network.png'.format(path), **visual_style)


########################################################################################################################


# saves communities
def save_communities(network, communities, path, threshold):

    # variable to hold number set to 1
    number = 1
    # for community in communities
    for community in communities:
        # if community graph file does not exist
        if not os.path.isfile('../../data/networks/{}/communities/community{}.graphml'.format(path, number)):
            # if size of community is greater than threshold
            if len(community) > threshold:
                # variable to hold sub-graph
                sub_graph = network.subgraph(communities[number - 1], 'create_from_scratch')
                # variable to hold output file
                output_file = open('../../data/networks/{}/communities/community{}.graphml'.format(path, number),
                                   mode='w')
                # write sub-graph structure to file
                sub_graph.write_graphml(output_file)
                # print stat to terminal
                print('Community {}: {}'.format(number, len(community)))

                # variable to hold stats file
                stats_file = open('../../data/networks/{}/communities/stats.txt'.format(path), mode='a')
                # write stat to file
                stats_file.write('Community {}: {}\n'.format(number, len(community)))

                # increment number
                number += 1


########################################################################################################################


# plots communities
def plot_communities(network, communities, membership, path, edges):

    # if edges is True
    if edges is True:

        # if communities plot file does not exist
        if not os.path.isfile('../../data/networks/{}/communities/communities1.png'.format(path)):

            # variable to hold edges
            edges = [edge for edge in network.es() if membership[edge.tuple[0]] != membership[edge.tuple[1]]]

            # colour edges
            [edge.update_attributes({'color': 'grey'}) if membership[edge.tuple[0]] != membership[edge.tuple[1]]
             else edge.update_attributes({'color': 'black'}) for edge in network.es()]

            # variable to hold network copy
            network_copy = network.copy()

            # delete edges
            network_copy.delete_edges(edges)

            # variable to hold visual style
            visual_style = {'vertex_label': None,
                            'vertex_size': network.vs['NormNum'],
                            'edge_width': network.es['NormWeight'],
                            'layout': network_copy.layout('kk'),
                            'bbox': (1000, 1000),
                            'margin': 40}

            # variable to hold colours
            colours = ['#%06X' % randint(0, 0xFFFFFF) for i in range(0, len(membership) + 1)]

            # colour nodes
            [vertex.update_attributes({'color': colours[membership[vertex.index]]}) for vertex in network.vs()]

            # plot network
            ig.plot(network, '../../data/networks/{}/communities/communities1.png'.format(path), **visual_style)

    # if edges is False
    elif edges is False:

        # if communities plot file does not exist
        if not os.path.isfile('../../data/networks/{}/communities/communities2.png'.format(path)):

            # variable to hold edges
            edges = [edge for edge in network.es() if membership[edge.tuple[0]] != membership[edge.tuple[1]]]

            # delete edges
            network.delete_edges(edges)

            # variable to hold visual style
            visual_style = {'vertex_label': None,
                            'vertex_size': network.vs['NormNum'],
                            'edge_width': network.es['NormWeight'],
                            'layout': 'kk',
                            'bbox': (1000, 1000),
                            'margin': 40}

            # plot network
            ig.plot(communities, '../../data/networks/{}/communities/communities2.png'.format(path), **visual_style)


########################################################################################################################

# analyses sub-communities
def analyse_sub_communities(path, length):

    # for i in range between 0 and length of communities
    for i in range(1, length):

        # variable to hold community
        community = ig.Graph.Read_GraphML('../../data/networks/{}/communities/community{}.graphml'.format(path, i))

        # variable to hold louvain
        louvain = community.community_multilevel(weights='weight')

        # variable to hold sub-communities
        sub_communities = louvain

        # save sub-communities
        save_sub_communities(community, sub_communities, path, i)

        # plot sub-communities
        # plot_sub_communities(community, sub_communities, sub_communities.membership, path, i, True)

########################################################################################################################


# saves sub-communities
def save_sub_communities(network, sub_communities, path, i):

    # variable to hold number set to 1
    number = 1
    # for sub-community in sub-communities
    for sub_community in sub_communities:
        # if sub-community graph file does not exist
        if not os.path.isfile('../../data/networks/{}/sub-communities/community{}_{}.graphml'.format(path, i, number)):
            # variable to hold sub-graph
            sub_graph = network.subgraph(sub_communities[number - 1], 'create_from_scratch')
            # variable to hold output file
            output_file = open('../../data/networks/{}/sub-communities/community{}_{}.graphml'.format(path, i, number),
                               mode='w')
            # write sub-graph structure to file
            sub_graph.write_graphml(output_file)
            # print stat to terminal
            print('Community {}.{}: {}'.format(i, number, len(sub_community)))

            # variable to hold stats file
            stats_file = open('../../data/networks/{}/sub-communities/stats_{}.txt'.format(path, i), mode='a')
            # write stat to file
            stats_file.write('Community {}.{}: {}\n'.format(i, number, len(sub_community)))

            # increment number
            number += 1


########################################################################################################################


# plots sub-communities
def plot_sub_communities(network, sub_communities, membership, path, i, edges):

    # if edges is True
    if edges is True:

        # if communities plot file does not exist
        if not os.path.isfile('../../data/networks/{}/sub-communities/communities1_{}.png'.format(path, i)):

            # variable to hold edges
            for edge in network.es():
                if membership[edge.tuple[0]] != membership[edge.tuple[1]]:
                    print(edge)

            # colour edges
            [edge.update_attributes({'color': 'grey'}) if membership[edge.tuple[0]] != membership[edge.tuple[1]]
             else edge.update_attributes({'color': 'black'}) for edge in network.es()]

            # variable to hold network copy
            network_copy = network.copy()

            # delete edges
            network_copy.delete_edges(edges)

            # variable to hold visual style
            visual_style = {'vertex_label': None,
                            'vertex_size': network.vs['NormNum'],
                            'edge_width': network.es['NormWeight'],
                            'layout': network_copy.layout('kk'),
                            'bbox': (1000, 1000),
                            'margin': 40}

            # variable to hold colours
            colours = ['#%06X' % randint(0, 0xFFFFFF) for i in range(0, len(membership) + 1)]

            # colour nodes
            [vertex.update_attributes({'color': colours[membership[vertex.index]]}) for vertex in network.vs()]

            # plot network
            ig.plot(network, '../../data/networks/{}/sub-communities/communities1_{}.png'.format(path, i), **visual_style)

    # if edges is False
    elif edges is False:

        # if communities plot file does not exist
        if not os.path.isfile('../../data/networks/{}/sub-communities/communities2_{}.png'.format(path, i)):

            # variable to hold edges
            edges = [edge for edge in network.es() if membership[edge.tuple[0]] != membership[edge.tuple[1]]]

            # delete edges
            network.delete_edges(edges)

            # variable to hold visual style
            visual_style = {'vertex_label': None,
                            'vertex_size': network.vs['NormNum'],
                            'edge_width': network.es['NormWeight'],
                            'layout': 'kk',
                            'bbox': (1000, 1000),
                            'margin': 40}

            # plot network
            ig.plot(sub_communities, '../../data/networks/{}/sub-communities/communities2_{}.png'.format(path, i),
                    **visual_style)


########################################################################################################################


# main function
def main():

    # analyse topic network
    AnalyseTopicNetwork.run()

    # analyse researcher network
    AnalyseResearcherNetwork.run()


########################################################################################################################

# runs main function
if __name__ == '__main__':
    main()

########################################################################################################################
