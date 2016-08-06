
# third-party library modules
import igraph as ig
from random import randint

########################################################################################################################


# checks sub-communities
def check_sub_communities(community, edge_type, method, path, i):

    # if community is an instance of graph
    if isinstance(community, ig.Graph):

        # if edge count is greater than 0
        if community.ecount() < 1:

            # variable to hold output file
            open('../../data/networks/{}/sub-communities/graphml/'
                 '{}/{}/community{}_zero_edges.graphml'.format(path, edge_type, method, i), mode='w')
            open('../../data/networks/{}/sub-communities/txt/'
                 '{}/{}/numbers{}_zero_edges.txt'.format(path, edge_type, method, i), mode='w')
            open('../../data/networks/{}/communities/graphml/'
                 '{}/{}/membership{}_zero_edges.graphml'.format(path, edge_type, method, i), mode='w')
            open('../../data/networks/{}/sub-communities/txt/{}/{}/'
                 'sub_community_topics{}_zero_edges.txt'.format(path, edge_type, method, i), mode='w')
            open('../../data/networks/{}/sub-communities/png/'
                 '{}/{}/overview1_{}_zero_edges.png'.format(path, edge_type, method, i), mode='w')
            open('../../data/networks/{}/sub-communities/png/'
                 '{}/{}/overview2_{}_zero_edges.png'.format(path, edge_type, method, i), mode='w')

            # return True
            return True

    # if community equals to vertex clustering
    elif community == ig.VertexClustering:

        # variable to hold output file
        open('../../data/networks/{}/sub-communities/graphml/'
             '{}/{}/community{}_unconnected.graphml'.format(path, edge_type, method, i), mode='w')
        open('../../data/networks/{}/sub-communities/txt/'
             '{}/{}/numbers{}_unconnected.txt'.format(path, edge_type, method, i), mode='w')
        open('../../data/networks/{}/communities/graphml/'
             '{}/{}/membership{}_unconnected.graphml'.format(path, edge_type, method, i), mode='w')
        open('../../data/networks/{}/sub-communities/txt/{}/{}/'
             'sub_community_topics{}_unconnected.txt'.format(path, edge_type, method, i), mode='w')
        open('../../data/networks/{}/sub-communities/png/'
             '{}/{}/overview1_{}_unconnected.png'.format(path, edge_type, method, i), mode='w')
        open('../../data/networks/{}/sub-communities/png/'
             '{}/{}/overview2_{}_unconnected.png'.format(path, edge_type, method, i), mode='w')

        # return True
        return True


########################################################################################################################


# saves sub-communities
def save_sub_communities(community, sub_communities, edge_type, method, path, i):

    # variable to hold number set to 1
    number = 1

    # for sub-community in sub-communities
    for sub_community in sub_communities:

        # variable to hold sub-graph
        sub_graph = community.subgraph(sub_communities[number - 1], 'create_from_scratch')

        # variable to hold output file
        output_file = open('../../data/networks/{}/sub-communities/graphml/'
                           '{}/{}/community{}_{}.graphml'.format(path, edge_type, method, i, number), mode='w')

        # write sub-graph structure to file
        sub_graph.write_graphml(output_file)

        # variable to hold stats file
        stats_file = open('../../data/networks/{}/sub-communities/txt/'
                          '{}/{}/numbers{}.txt'.format(path, edge_type, method, i), mode='a')

        # write stat to file
        stats_file.write('Community {}: {}\n'.format(number, len(sub_community)))

        # increment number
        number += 1


########################################################################################################################


# saves sub-community membership
def save_sub_community_membership(community, edge_type, method, path, i):

    # if val in edge attributes
    if 'val' in community.es.attributes():
        # delete edge value attribute
        del community.es['val']
        # add edge value attribute
        community.es['val'] = community.es['norm_val']
        # delete edge normalized value attribute
        del community.es['norm_val']

    # if weight in edge attributes
    if 'weight' in community.es.attributes():
        # delete edge weight attribute
        del community.es['weight']
        # add edge weight attribute
        community.es['weight'] = community.es['norm_weight']
        # delete edge normalized weight attribute
        del community.es['norm_weight']

    # variable to hold output file
    output_file = open('../../data/networks/{}/communities/graphml/'
                       '{}/{}/membership{}.graphml'.format(path, edge_type, method, i), mode='w')

    # write network structure to file
    community.write_graphml(output_file)


########################################################################################################################


# saves sub-community topics
def save_sub_community_topics(community, sub_communities, edge_type, method, path, i):

    # variable to hold output file
    output_file = open('../../data/networks/{}/sub-communities/txt/{}/{}/'
                       'sub_community_topics{}.txt'.format(path, edge_type, method, i), mode='a')

    # for sub-community in range between 1 and length of sub-communities + 1
    for sub_community in range(1, len(sub_communities) + 1):

        # variable to hold sub-community topics
        sub_community_topics = [label for label, membership
                                in zip(community.vs['label'], community.vs['membership'])
                                if membership == sub_community]

        # if community is equal to 1
        if sub_community == 1:

            # write headers to file
            output_file.write('> Community {}.{} ({})\n\n'.format(i, sub_community, len(sub_community_topics)))

        # if community is not equal to 0
        else:

            # write headers to file
            output_file.write('\n> Community {}.{} ({})\n\n'.format(i, sub_community,
                                                                    len(sub_community_topics)))

        # for sub-community topic in sub-community topics
        for sub_community_topic in sub_community_topics:

            # write sub-community topic to file
            output_file.write('- {}\n'.format(sub_community_topic))


########################################################################################################################


# plots sub-community overview
def plot_sub_community_overview(community, sub_communities, membership, edge_type, method, path, i, edges):

    # if edges is True
    if edges is True:

        # variable to hold edges
        edges = [edge for edge in community.es() if membership[edge.tuple[0]] != membership[edge.tuple[1]]]

        # colour edges
        [edge.update_attributes({'color': 'grey'}) if membership[edge.tuple[0]] != membership[edge.tuple[1]]
         else edge.update_attributes({'color': 'black'}) for edge in community.es()]

        # variable to hold community copy
        community_copy = community.copy()

        # delete edges
        community_copy.delete_edges(edges)

        # add normalized edge weight column to community
        community.es['norm_weight'] = community.es['weight']

        # variable to hold visual style
        visual_style = {'vertex_size': community.vs['norm_num'],
                        'edge_width': community.es['norm_weight'],
                        'layout': community_copy.layout('kk'),
                        'bbox': (1000, 1000),
                        'margin': 40}

        # variable to hold colours
        colours = ['#%06X' % randint(0, 0xFFFFFF) for i in range(0, len(sub_communities) + 1)]

        # colour nodes
        [vertex.update_attributes({'color': colours[membership[vertex.index]]}) for vertex in community.vs()]

        # plot community
        ig.plot(community, '../../data/networks/{}/sub-communities/png/'
                           '{}/{}/overview1_{}.png'.format(path, edge_type, method, i), **visual_style)

    ####################################################################################################################

    # if edges is False
    elif edges is False:

        # variable to hold edges
        edges = [edge for edge in community.es() if membership[edge.tuple[0]] != membership[edge.tuple[1]]]

        # delete edges
        community.delete_edges(edges)

        # add normalized edge weight column to community
        community.es['norm_weight'] = community.es['weight']

        # variable to hold visual style
        visual_style = {'vertex_size': community.vs['norm_num'],
                        'edge_width': community.es['norm_weight'],
                        'layout': 'kk',
                        'bbox': (1000, 1000),
                        'margin': 40}

        # plot sub-communities
        ig.plot(sub_communities, '../../data/networks/{}/sub-communities/png/'
                                 '{}/{}/overview2_{}.png'.format(path, edge_type, method, i), **visual_style)


########################################################################################################################
