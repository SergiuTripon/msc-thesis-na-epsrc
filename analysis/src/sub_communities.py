
# third-party library modules
import igraph as ig
from pickle import load
from random import randint
from collections import OrderedDict
from locale import setlocale, LC_ALL, currency

########################################################################################################################


# analyses sub-communities
def analyse_sub_communities(community, sub_communities, network_type, edge_type, method, count1, path):

    # check sub-communities
    if check_sub_communities(sub_communities, edge_type, method, count1, path):
        # return
        return

    ####################################################################################################################

    # normalize membership
    community.vs['membership'] = norm_membership(sub_communities.membership)

    ####################################################################################################################

    # save sub-community membership
    save_sub_community_membership(community, edge_type, method, count1, path)

    ####################################################################################################################

    # plot sub-community overview 1
    plot_sub_community_overview(community, sub_communities, sub_communities.membership, edge_type, method, True,
                                count1, path)

    ####################################################################################################################

    # plot sub-community overview 2
    plot_sub_community_overview(community, sub_communities, sub_communities.membership, edge_type, method, False,
                                count1, path)

    ####################################################################################################################

    # variable to hold unique grants
    unique_grants = OrderedDict()

    # variable to hold total number and value
    total_number, total_value = 0, 0

    # variable to hold count2 set to 1
    count2 = 1

    ####################################################################################################################

    # for sub-community in sub-communities
    for sub_community in sub_communities:

        ################################################################################################################

        # variable to hold sub-graph
        sub_graph = community.subgraph(sub_community, 'create_from_scratch')

        ################################################################################################################

        # save sub-community
        save_sub_community(sub_graph, edge_type, method, count1, count2, path)

        ################################################################################################################

        # save sub-community entities
        save_sub_community_entities(sub_graph, edge_type, method, count1, count2, path)

        ################################################################################################################

        # if network type equals to topic a or researcher b
        if network_type == 'topic-a' or network_type == 'researcher-b':

            # turn edges into grants
            grants, number, value = turn_edges_into_grants(sub_graph, edge_type, method, count1, count2, path)

            # update unique grants
            unique_grants.update(grants)

            # add number to total number
            total_number += number
            # add value to total value
            total_value += value

        ################################################################################################################

        # increment count2
        count2 += 1

    ####################################################################################################################

    # if network type equals to topic a or researcher b
    if network_type == 'topic-a' or network_type == 'researcher-b':

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


# checks sub-communities
def check_sub_communities(sub_community, edge_type, method, count1, path):

    # variable to hold entity
    entity = path.split('/', 1)[0]

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
                 '{}/{}/{}{}_zero_edges.txt'.format(path, edge_type, method, entity, count1), mode='w')
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
             '{}/{}/modularity_unconnected.txt'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/sub-communities/graphml/'
             '{}/{}/community{}_unconnected.graphml'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/sub-communities/txt/'
             '{}/{}/numbers{}_unconnected.txt'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/sub-communities/txt/'
             '{}/{}/grants{}_unconnected.txt'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/communities/graphml/'
             '{}/{}/membership{}_unconnected.graphml'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/sub-communities/txt/'
             '{}/{}/{}{}_unconnected.txt'.format(path, edge_type, method, entity, count1), mode='w')
        open('../../data/networks/{}/sub-communities/png/'
             '{}/{}/overview1_{}_unconnected.png'.format(path, edge_type, method, count1), mode='w')
        open('../../data/networks/{}/sub-communities/png/'
             '{}/{}/overview2_{}_unconnected.png'.format(path, edge_type, method, count1), mode='w')

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


# saves sub-community membership
def save_sub_community_membership(community, edge_type, method, count1, path):

    # variable to hold output file
    output_file = open('../../data/networks/{}/communities/graphml/'
                       '{}/{}/membership{}.graphml'.format(path, edge_type, method, count1), mode='w')

    # write network structure to file
    community.write_graphml(output_file)


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


# saves sub-community
def save_sub_community(sub_community, edge_type, method, count1, count2, path):

    # variable to hold output file
    output_file = open('../../data/networks/{}/sub-communities/graphml/'
                       '{}/{}/community{}_{}.graphml'.format(path, edge_type, method, count1, count2), mode='w')

    # write sub-community structure to file
    sub_community.write_graphml(output_file)

    # variable to hold output file
    output_file = open('../../data/networks/{}/sub-communities/txt/'
                       '{}/{}/numbers{}.txt'.format(path, edge_type, method, count1), mode='a')

    # if count2 is equal to 1
    if count2 == 1:

        # write header to file
        output_file.write('> Community size of each sub-community\n\n')

        # write stat to file
        output_file.write('- Community {}: {}\n'.format(count2, sub_community.vcount()))

    # if count2 is not equal to 1
    else:

        # write stat to file
        output_file.write('- Community {}: {}\n'.format(count2, sub_community.vcount()))


########################################################################################################################


# saves sub-community entities
def save_sub_community_entities(sub_community, edge_type, method, count1, count2, path):

    # variable to hold entity
    entity = path.split('/', 1)[0]

    # variable to hold output file
    output_file = open('../../data/networks/{}/sub-communities/txt/{}/{}/'
                       '{}{}.txt'.format(path, edge_type, method, entity, count1), mode='a')

    # variable to hold sub-community entities
    sub_community_entities = [label for label in sub_community.vs['label']]

    # if count2 is equal to 1
    if count2 == 1:

        # write header to file
        output_file.write('> {} in each sub-community\n\n'.format(entity.capitalize()))

        # write headers to file
        output_file.write('> Community {}.{} ({})\n\n'.format(count1, count2, len(sub_community_entities)))

    # if count2 is not equal to 1
    else:

        # write headers to file
        output_file.write('\n> Community {}.{} ({})\n\n'.format(count1, count2, len(sub_community_entities)))

    # for sub-community entity in sub-community entities
    for sub_community_entity in sub_community_entities:

        # write sub-community topic to file
        output_file.write('- {}\n'.format(sub_community_entity))


########################################################################################################################


# turns edges into grants
def turn_edges_into_grants(sub_community, edge_type, method, count1, count2, path):

    # variable to split path
    path_split = path.split('/', 3)

    # variable to hold temporary path
    path_temp = ''

    # if split path equals to current
    if path_split[1] == 'current':
        # set temporary path
        path_temp = '{}'.format(path_split[1])
    # if split path equals to past
    elif path_split[1] == 'past':
        # set temporary path
        path_temp = '{}/{}'.format(path_split[1], path_split[2])

    # variable to hold input file
    input_file = open(r'../../network-maker/output/grants/{}/info/grant_{}.pkl'.format(path_temp, path_split[0]), 'rb')
    # load data structure from file
    grant_entities = load(input_file)
    # close input file
    input_file.close()

    # variable to hold entity links
    entity_links = [[sub_community.vs['label'][edge.source], sub_community.vs['label'][edge.target]]
                    for edge in sub_community.es()]

    # variable to hold grants
    grants = OrderedDict()

    # if split path equals to topics
    if path_split[0] == 'topics':

        # variable to hold grants
        grants = OrderedDict((ref, attr[1]) for entity_link in entity_links for ref, attr in grant_entities.items()
                             if entity_link[0] and entity_link[1] in attr[0])

    # if split path equals to researchers
    elif path_split[0] == 'researchers':

        # set grants
        grants = OrderedDict((ref, attr[1]) for entity_link in entity_links for ref, attr in grant_entities.items()
                             if entity_link[0] and entity_link[1] in [researcher[0] for researcher in attr[0]])

    # variable to hold number
    number = len([ref for ref in grants.keys()])

    # set locale to Great Britain
    setlocale(LC_ALL, 'en_GB.utf8')

    # variable to hold value
    value = sum([attr for attr in grants.values()])

    # variable to hold output file
    output_file = open('../../data/networks/{}/sub-communities/txt/{}/{}/'
                       'grants{}.txt'.format(path, edge_type, method, count1), mode='a')

    # if count2 is equal to 1
    if count2 == 1:

        # write header to file
        output_file.write('> Number and value of grants in each sub-community\n\n')

        # write grant number and value to file
        output_file.write('- Community {}.{}:  {:>4d} {}\n'.format(count1, count2, number,
                                                                   currency(value, grouping=True)))

    # if count2 is not equal to 1
    else:

        # write grant number and value to file
        output_file.write('- Community {}.{}:  {:>4d} {}\n'.format(count1, count2, number,
                                                                   currency(value, grouping=True)))

    # return number and value
    return grants, number, value


########################################################################################################################
