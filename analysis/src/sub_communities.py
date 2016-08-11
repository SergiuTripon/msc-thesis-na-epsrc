
# local python files
import communities as ca

# third-party library modules
import igraph as ig
from pickle import load
from random import randint
from collections import OrderedDict
from locale import setlocale, LC_ALL, currency

########################################################################################################################


# analyses sub-communities
def analyse_sub_communities(community, sub_communities, edge_type, method, count1, path):

    # check sub-communities
    if check_sub_communities(sub_communities, edge_type, method, count1, path):
        # return
        return

    # normalize membership
    community.vs['membership'] = ca.norm_membership(sub_communities.membership)
    # print progress
    # print('> Community membership normalized.'.format(edge_type, method))

    # save sub-communities
    save_sub_communities(community, sub_communities, edge_type, method, count1, path)
    # print progress
    # print('> Sub-communities saved ({} - {}).'.format(edge_type, method))

    # save sub-community membership
    save_sub_community_membership(community, edge_type, method, count1, path)
    # print progress
    # print('> Sub-community membership saved ({} - {}).'.format(edge_type, method))

    # save sub-community topics
    save_sub_community_topics(community, sub_communities, edge_type, method, count1, path)
    # print progress
    # print('> Sub-community topics saved ({} - {}).'.format(edge_type, method))

    # plot sub-community overview
    plot_sub_community_overview(community, sub_communities, sub_communities.membership, edge_type, method,
                                True, count1, path)
    plot_sub_community_overview(community, sub_communities, sub_communities.membership, edge_type, method,
                                False, count1, path)
    # print progress
    # print('> Sub-community overview plotted ({} - {}).'.format(edge_type, method))


########################################################################################################################


# checks sub-communities
def check_sub_communities(sub_community, edge_type, method, count1, path):

    # if sub-community is an instance of graph
    if isinstance(sub_community, ig.Graph):

        # if edge count is greater than 0
        if sub_community.ecount() < 1:

            # create placeholder files
            open('../../data/networks/{}/sub-communities/graphml/'
                 '{}/{}/community{}_zero_edges.graphml'.format(path, edge_type, method, count1), mode='w')
            open('../../data/networks/{}/sub-communities/txt/'
                 '{}/{}/numbers{}_zero_edges.txt'.format(path, edge_type, method, count1), mode='w')
            open('../../data/networks/{}/sub-communities/txt/'
                 '{}/{}/grants{}_zero_edges.txt'.format(path, edge_type, method, count1), mode='w')
            open('../../data/networks/{}/communities/graphml/'
                 '{}/{}/membership{}_zero_edges.graphml'.format(path, edge_type, method, count1), mode='w')
            open('../../data/networks/{}/sub-communities/txt/'
                 '{}/{}/topics{}_zero_edges.txt'.format(path, edge_type, method, count1), mode='w')
            open('../../data/networks/{}/sub-communities/png/'
                 '{}/{}/overview1_{}_zero_edges.png'.format(path, edge_type, method, count1), mode='w')
            open('../../data/networks/{}/sub-communities/png/'
                 '{}/{}/overview2_{}_zero_edges.png'.format(path, edge_type, method, count1), mode='w')

            # return true
            return True

    # if sub-community equals to vertex clustering
    elif sub_community == ig.VertexClustering:

        # create placeholder files
        open('../../data/networks/{}/communities/txt/'
             '{}/{}/modularity_unconnected.graphml'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/sub-communities/graphml/'
             '{}/{}/community{}_unconnected.graphml'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/sub-communities/txt/'
             '{}/{}/numbers{}_unconnected.txt'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/sub-communities/txt/'
             '{}/{}/grants{}_unconnected.txt'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/communities/graphml/'
             '{}/{}/membership{}_unconnected.graphml'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/sub-communities/txt/'
             '{}/{}/topics{}_unconnected.txt'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/sub-communities/png/'
             '{}/{}/overview1_{}_unconnected.png'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/sub-communities/png/'
             '{}/{}/overview2_{}_unconnected.png'.format(path, edge_type, method, count1), mode='w')

        # return True
        return True


########################################################################################################################


# saves sub-communities
def save_sub_communities(community, sub_communities, edge_type, method, count1, path):

    # variable to hold output file
    output_file = open('../../data/networks/{}/sub-communities/txt/{}/{}/'
                       'grants{}.txt'.format(path, edge_type, method, count1), mode='a')
    # write header to file
    output_file.write('> Number and value of grants in each sub-community\n\n')

    # variable to hold output file
    output_file = open('../../data/networks/{}/sub-communities/txt/'
                       '{}/{}/numbers{}.txt'.format(path, edge_type, method, count1), mode='a')
    # write header to file
    output_file.write('> Community size of each sub-community\n\n')

    # variable to hold unique grants
    unique_grants = OrderedDict()

    # variable to hold total number and value
    total_number, total_value = 0, 0

    # variable to hold count2 set to 1
    count2 = 1

    # for sub-community in sub-communities
    for sub_community in sub_communities:

        # variable to hold sub-graph
        sub_graph = community.subgraph(sub_communities[count2 - 1], 'create_from_scratch')

        # variable to hold output file
        output_file = open('../../data/networks/{}/sub-communities/graphml/'
                           '{}/{}/community{}_{}.graphml'.format(path, edge_type, method, count1, count2), mode='w')

        # write sub-graph structure to file
        sub_graph.write_graphml(output_file)

        # variable to hold output file
        output_file = open('../../data/networks/{}/sub-communities/txt/'
                           '{}/{}/numbers{}.txt'.format(path, edge_type, method, count1), mode='a')

        # write stat to file
        output_file.write('- Community {}: {}\n'.format(count2, len(sub_community)))

        # turn edges into grants
        grants, number, value = turn_edges_into_grants(sub_graph, edge_type, method, count1, count2, path)

        # update unique grants
        unique_grants.update(grants)

        # add number to total number
        total_number += number
        # add value to total value
        total_value += value

        # increment count2
        count2 += 1

    # set locale to Great Britain
    setlocale(LC_ALL, 'en_GB.utf8')

    # variable to hold output file
    output_file = open('../../data/networks/{}/sub-communities/txt/{}/{}/'
                       'grants{}.txt'.format(path, edge_type, method, count1), mode='a')
    # write grant number and value to file
    output_file.write('\n- Total:          {:>4d} {}\n'.format(total_number, currency(total_value, grouping=True)))

    # variable to hold total number
    total_number = len(unique_grants)
    # variable to hold total value
    total_value = sum([attr for attr in unique_grants.values()])

    # variable to hold output file
    output_file = open('../../data/networks/{}/sub-communities/txt/{}/{}/'
                       'grants{}.txt'.format(path, edge_type, method, count1), mode='a')
    # write grant number and value to file
    output_file.write('- Total (unique): {:>4d} {}'.format(total_number, currency(total_value, grouping=True)))


########################################################################################################################


# turns edges into grants
def turn_edges_into_grants(sub_community, edge_type, method, count1, count2, path):

    # variable to hold temporary path
    path_temp = ''

    # if first and last letter of path equals to t and a
    if path[0] == 't' and path[-1] == 'a':
        # set temporary path
        path_temp = path.replace('topics/', '').replace('/network-a', '')
    # if first and last letter of path equals to t and b
    if path[0] == 't' and path[-1] == 'b':
        # set temporary path
        path_temp = path.replace('topics/', '').replace('/network-b', '')
    # if first and last letter of path equals to r and a
    if path[0] == 'r' and path[-1] == 'a':
        # set temporary path
        path_temp = path.replace('researchers/', '').replace('/network-a', '')
    # if first and last letter of path equals to r and b
    if path[0] == 'r' and path[-1] == 'b':
        # set temporary path
        path_temp = path.replace('researchers/', '').replace('/network-b', '')

    # variable to hold input file
    input_file = open(r'../../network-maker/output/grants/{}/info/grant_topics.pkl'.format(path_temp), 'rb')
    # load data structure from file
    grant_topics = load(input_file)
    # close input file
    input_file.close()

    # variable to hold topic links
    topic_links = [[sub_community.vs['label'][edge.source], sub_community.vs['label'][edge.target]]
                   for edge in sub_community.es()]

    # variable to hold grants
    grants = OrderedDict((ref, attr[1]) for topic_link in topic_links for ref, attr in grant_topics.items()
                         if topic_link[0] in attr[0])

    # variable to hold number
    number = len([ref for ref in grants.keys()])

    # set locale to Great Britain
    setlocale(LC_ALL, 'en_GB.utf8')

    # variable to hold value
    value = sum([attr for attr in grants.values()])

    # variable to hold output file
    output_file = open('../../data/networks/{}/sub-communities/txt/{}/{}/'
                       'grants{}.txt'.format(path, edge_type, method, count1), mode='a')
    # write grant number and value to file
    output_file.write('- Community {}.{}:  {:>4d} {}\n'.format(count1, count2, number, currency(value, grouping=True)))

    # return number and value
    return grants, number, value


########################################################################################################################


# saves sub-community membership
def save_sub_community_membership(community, edge_type, method, count1, path):

    # variable to hold output file
    output_file = open('../../data/networks/{}/communities/graphml/'
                       '{}/{}/membership{}.graphml'.format(path, edge_type, method, count1), mode='w')

    # write network structure to file
    community.write_graphml(output_file)


########################################################################################################################


# saves sub-community topics
def save_sub_community_topics(community, sub_communities, edge_type, method, count1, path):

    # variable to hold output file
    output_file = open('../../data/networks/{}/sub-communities/txt/{}/{}/'
                       'topics{}.txt'.format(path, edge_type, method, count1), mode='a')
    # write header to file
    output_file.write('> Topics of each sub-community\n\n')

    # for sub-community in range between 1 and length of sub-communities + 1
    for sub_community in range(1, len(sub_communities) + 1):

        # variable to hold sub-community topics
        sub_community_topics = [label for label, membership
                                in zip(community.vs['label'], community.vs['membership'])
                                if membership == sub_community]

        # if community is equal to 1
        if sub_community == 1:

            # write headers to file
            output_file.write('> Community {}.{} ({})\n\n'.format(count1, sub_community, len(sub_community_topics)))

        # if community is not equal to 0
        else:

            # write headers to file
            output_file.write('\n> Community {}.{} ({})\n\n'.format(count1, sub_community, len(sub_community_topics)))

        # for sub-community topic in sub-community topics
        for sub_community_topic in sub_community_topics:

            # write sub-community topic to file
            output_file.write('- {}\n'.format(sub_community_topic))


########################################################################################################################


# plots sub-community overview
def plot_sub_community_overview(community, sub_communities, membership, edge_type, method, edges, count1, path):

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

        # variable to hold visual style
        visual_style = {'vertex_size': community.vs['plot_size'],
                        'edge_width': community.es['plot_weight'],
                        'layout': community_copy.layout('kk'),
                        'bbox': (1000, 1000),
                        'margin': 40}

        # variable to hold colours
        colours = ['#%06X' % randint(0, 0xFFFFFF) for i in range(0, len(sub_communities) + 1)]

        # colour nodes
        [vertex.update_attributes({'color': colours[membership[vertex.index]]}) for vertex in community.vs()]

        # plot community
        ig.plot(community, '../../data/networks/{}/sub-communities/png/'
                           '{}/{}/overview1_{}.png'.format(path, edge_type, method, count1), **visual_style)

    ####################################################################################################################

    # if edges is False
    elif edges is False:

        # variable to hold edges
        edges = [edge for edge in community.es() if membership[edge.tuple[0]] != membership[edge.tuple[1]]]

        # delete edges
        community.delete_edges(edges)

        # variable to hold visual style
        visual_style = {'vertex_size': community.vs['plot_size'],
                        'edge_width': community.es['plot_weight'],
                        'layout': 'kk',
                        'bbox': (1000, 1000),
                        'margin': 40}

        # plot sub-communities
        ig.plot(sub_communities, '../../data/networks/{}/sub-communities/png/'
                                 '{}/{}/overview2_{}.png'.format(path, edge_type, method, count1), **visual_style)


########################################################################################################################
