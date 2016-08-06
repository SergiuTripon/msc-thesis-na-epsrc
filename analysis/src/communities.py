
# third-party library modules
import igraph as ig
from random import randint

########################################################################################################################


# checks communities
def check_communities(communities, edge_type, method, path):

    # if communities do not exist
    if communities == ig.VertexClustering:

        open('../../data/networks/{}/communities/graphml/'
             '{}/{}/community1_unconnected.graphml'.format(path, edge_type, method), mode='w')
        open('../../data/networks/{}/communities/txt/'
             '{}/{}/numbers_unconnected.txt'.format(path, edge_type, method), mode='w')
        open('../../data/networks/{}/network/graphml/'
             '{}/{}/membership_unconnected.graphml'.format(path, edge_type, method), mode='w')
        open('../../data/networks/{}/communities/txt/'
             '{}/{}/community_topics_unconnected.txt'.format(path, edge_type, method), mode='w')
        open('../../data/networks/{}/communities/png/'
             '{}/{}/overview1_unconnected.png'.format(path, edge_type, method), mode='w')
        open('../../data/networks/{}/communities/png/'
             '{}/{}/overview2_unconnected.png'.format(path, edge_type, method), mode='w')

        # return True
        return True


########################################################################################################################


# normalizes membership
def norm_membership(membership):

    # variable to hold new membership
    new_membership = [community + 1 for community in membership]

    # return new membership
    return new_membership


########################################################################################################################


# saves communities
def save_communities(network, communities, edge_type, method, path, threshold):

    # variable to hold number set to 1
    number = 1

    # for community in communities
    for community in communities:

        # if size of community is greater than threshold
        if len(community) > threshold:

            # variable to hold sub-graph
            sub_graph = network.subgraph(communities[number - 1], 'create_from_scratch')

            # variable to hold output file
            output_file = open('../../data/networks/{}/communities/graphml/{}/{}/'
                               'community{}.graphml'.format(path, edge_type, method, number), mode='w')

            # write sub-graph structure to file
            sub_graph.write_graphml(output_file)

            # variable to hold stats file
            stats_file = open('../../data/networks/{}/communities/txt/'
                              '{}/{}/numbers.txt'.format(path, edge_type, method), mode='a')

            # write stat to file
            stats_file.write('Community {}: {}\n'.format(number, len(community)))

            # increment number
            number += 1


########################################################################################################################


# saves community membership
def save_community_membership(network, edge_type, method, path):

    # if val in edge attributes
    if 'val' in network.es.attributes():
        # delete edge value attribute
        del network.es['val']
        # add edge value attribute
        network.es['val'] = network.es['norm_val']
        # delete edge normalized value attribute
        del network.es['norm_val']

    # if weight in edge attributes
    if 'weight' in network.es.attributes():
        # delete edge weight attribute
        del network.es['weight']
        # add edge weight attribute
        network.es['weight'] = network.es['norm_weight']
        # delete edge normalized weight attribute
        del network.es['norm_weight']

    # variable to hold output file
    output_file = open('../../data/networks/{}/network/graphml/'
                       '{}/{}/membership.graphml'.format(path, edge_type, method), mode='w')

    # write network structure to file
    network.write_graphml(output_file)


########################################################################################################################


# saves community topics
def save_community_topics(network, edge_type, method, communities, path):

    # variable to hold output file
    output_file = open('../../data/networks/{}/communities/txt/'
                       '{}/{}/community_topics.txt'.format(path, edge_type, method), mode='a')

    # for community in range between 1 and length of communities + 1
    for community in range(1, len(communities) + 1):

        # variable to hold community topics
        community_topics = [label for label, membership in zip(network.vs['label'], network.vs['membership'])
                            if membership == community]

        # if community is equal to 1
        if community == 1:

            # write headers to file
            output_file.write('> Community {} ({})\n\n'.format(community, len(community_topics)))

        # if community is not equal to 0
        else:

            # write headers to file
            output_file.write('\n> Community {} ({})\n\n'.format(community, len(community_topics)))

        # for community topic in community topics
        for community_topic in community_topics:
            # write community topic to file
            output_file.write('- {}\n'.format(community_topic))


########################################################################################################################


# plots community overview
def plot_community_overview(network, edge_type, method, communities, membership, path, edges):

    # if edges is True
    if edges is True:

        # variable to hold edges
        edges = [edge for edge in network.es() if membership[edge.tuple[0]] != membership[edge.tuple[1]]]

        # colour edges
        [edge.update_attributes({'color': 'grey'}) if membership[edge.tuple[0]] != membership[edge.tuple[1]]
         else edge.update_attributes({'color': 'black'}) for edge in network.es()]

        # variable to hold network copy
        network_copy = network.copy()

        # delete edges
        network_copy.delete_edges(edges)

        # add normalized edge weight column to network
        network.es['norm_weight'] = network.es['weight']

        # variable to hold visual style
        visual_style = {'vertex_label': None,
                        'vertex_size': network.vs['norm_num'],
                        'edge_width': network.es['norm_weight'],
                        'layout': network_copy.layout('kk'),
                        'bbox': (1000, 1000),
                        'margin': 40}

        # variable to hold colours
        colours = ['#%06X' % randint(0, 0xFFFFFF) for i in range(0, len(communities) + 1)]

        # colour nodes
        [vertex.update_attributes({'color': colours[membership[vertex.index]]}) for vertex in network.vs()]

        # plot network
        ig.plot(network, '../../data/networks/{}/communities/png/'
                         '{}/{}/overview1.png'.format(path, edge_type, method), **visual_style)

    ####################################################################################################################

    # if edges is False
    elif edges is False:

        # variable to hold edges
        edges = [edge for edge in network.es() if membership[edge.tuple[0]] != membership[edge.tuple[1]]]

        # delete edges
        network.delete_edges(edges)

        # add normalized edge weight column to network
        network.es['norm_weight'] = network.es['weight']

        # variable to hold visual style
        visual_style = {'vertex_label': None,
                        'vertex_size': network.vs['norm_num'],
                        'edge_width': network.es['norm_weight'],
                        'layout': 'kk',
                        'bbox': (1000, 1000),
                        'margin': 40}

        # plot communities
        ig.plot(communities, '../../data/networks/{}/communities/png/'
                             '{}/{}/overview2.png'.format(path, edge_type, method), **visual_style)


########################################################################################################################


# plots communities
def plot_communities(community, edge_type, method, path, i):

    # variable to hold visual style
    visual_style = {'vertex_label': None,
                    'vertex_color': 'blue',
                    'vertex_size': community.vs['norm_num'],
                    'edge_width': community.es['norm_weight'],
                    'layout': 'kk',
                    'bbox': (1000, 1000),
                    'margin': 40}

    # plot network
    ig.plot(community, '../../data/networks/{}/communities/png/'
                       '{}/{}/community{}.png'.format(path, edge_type, method, i), **visual_style)


########################################################################################################################
