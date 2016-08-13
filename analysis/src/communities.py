
# local python files
import sub_communities as sca

# third-party library modules
import igraph as ig
from pickle import load
from random import randint
from collections import OrderedDict
from locale import setlocale, LC_ALL, currency

########################################################################################################################


# analyses communities
def analyse_communities(network, communities, network_type, edge_type, method, threshold, path):

    # check communities
    if check_communities(communities, edge_type, method, path):
        # return
        return

    ####################################################################################################################

    # add normalized node membership column to network
    network.vs['membership'] = norm_membership(communities.membership)

    ####################################################################################################################

    # save community membership
    save_community_membership(network, edge_type, method, path)

    ####################################################################################################################

    # plot community overview 1
    plot_community_overview(network, edge_type, method, communities, communities.membership, True, path)

    ####################################################################################################################

    # plot community overview 2
    plot_community_overview(network, edge_type, method, communities, communities.membership, False, path)

    ####################################################################################################################

    # variable to hold unique grants
    unique_grants = OrderedDict()

    # variable to hold total number and value
    total_number, total_value = 0, 0

    # variable to hold count1 set to 1
    count1 = 1

    ####################################################################################################################

    # for community in communities
    for community in communities:

        # if size of community is greater than threshold
        if len(community) > threshold:

            ############################################################################################################

            # variable to hold sub-graph
            sub_graph = network.subgraph(community, 'create_from_scratch')

            ############################################################################################################

            # save communities
            save_community(sub_graph, edge_type, method, count1, path)

            ############################################################################################################

            # save community entities and print progress
            save_community_entities(sub_graph, edge_type, method, count1, path)

            ############################################################################################################

            # plot community
            plot_community(sub_graph, edge_type, method, count1, path)

            ############################################################################################################

            # if network type equals to topic a or researcher b
            if network_type == 'topic-a' or network_type == 'researcher-b':

                # turn edges into grants
                grants, number, value = turn_edges_into_grants(sub_graph, edge_type, method, count1, path)

                # update unique grants
                unique_grants.update(grants)

                # add number to total number
                total_number += number
                # add value to total value
                total_value += value

            ############################################################################################################

            # check community
            if sca.check_sub_communities(sub_graph, edge_type, method, count1, path):
                # increment count1
                count1 += 1
                # return
                continue

            ############################################################################################################

            # variable to hold sub-communities
            sub_communities = calc_modularity(sub_graph, edge_type, method, count1, path)

            ############################################################################################################

            # analyse sub-communities
            sca.analyse_sub_communities(sub_graph, sub_communities, network_type, edge_type, method, count1, path)

            ############################################################################################################

            # increment count1
            count1 += 1

    ####################################################################################################################

    # if network type equals to topic a or researcher b
    if network_type == 'topic-a' or network_type == 'researcher-b':

        # set locale to Great Britain
        setlocale(LC_ALL, 'en_GB.utf8')

        # variable to hold output file
        output_file = open('../../data/networks/{}/communities/txt/{}/{}/'
                           'grants.txt'.format(path, edge_type, method), mode='a')
        # write grant number and value to file
        output_file.write('\n- Total:          {:>4d} {}\n'.format(total_number, currency(total_value, grouping=True)))

        # variable to hold total number
        total_number = len(unique_grants)
        # variable to hold total value
        total_value = sum([attr for attr in unique_grants.values()])

        # variable to hold output file
        output_file = open('../../data/networks/{}/communities/txt/{}/{}/'
                           'grants.txt'.format(path, edge_type, method), mode='a')
        # write grant number and value to file
        output_file.write('- Total (unique): {:>4d} {}'.format(total_number, currency(total_value, grouping=True)))


########################################################################################################################


# checks communities
def check_communities(communities, edge_type, method, path):

    # if communities do not exist
    if communities == ig.VertexClustering:

        # create placeholder files
        open('../../data/networks/{}/communities/graphml/'
             '{}/{}/community1_unconnected.graphml'.format(path, edge_type, method), mode='w')
        open('../../data/networks/{}/communities/txt/'
             '{}/{}/numbers_unconnected.txt'.format(path, edge_type, method), mode='w')
        open('../../data/networks/{}/communities/txt/'
             '{}/{}/grants_unconnected.txt'.format(path, edge_type, method), mode='w')
        open('../../data/networks/{}/network/graphml/'
             '{}/{}/membership_unconnected.graphml'.format(path, edge_type, method), mode='w')
        open('../../data/networks/{}/communities/txt/'
             '{}/{}/topics_unconnected.txt'.format(path, edge_type, method), mode='w')
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


# saves community membership
def save_community_membership(network, edge_type, method, path):

    # variable to hold output file
    output_file = open('../../data/networks/{}/network/graphml/'
                       '{}/{}/membership.graphml'.format(path, edge_type, method), mode='w')

    # write network structure to file
    network.write_graphml(output_file)


########################################################################################################################


# plots community overview
def plot_community_overview(network, edge_type, method, communities, membership, edges, path):

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

        # variable to hold visual style
        visual_style = {'vertex_label': None,
                        'vertex_size': network.vs['plot_size'],
                        'edge_width': network.es['plot_weight'],
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

        # variable to hold visual style
        visual_style = {'vertex_label': None,
                        'vertex_size': network.vs['plot_size'],
                        'edge_width': network.es['plot_weight'],
                        'layout': 'kk',
                        'bbox': (1000, 1000),
                        'margin': 40}

        # plot communities
        ig.plot(communities, '../../data/networks/{}/communities/png/'
                             '{}/{}/overview2.png'.format(path, edge_type, method), **visual_style)


########################################################################################################################


# saves community
def save_community(community, edge_type, method, count1, path):

    # variable to hold output file
    output_file = open('../../data/networks/{}/communities/graphml/{}/{}/'
                       'community{}.graphml'.format(path, edge_type, method, count1), mode='w')

    # write sub-graph structure to file
    community.write_graphml(output_file)

    # variable to hold output file
    output_file = open('../../data/networks/{}/communities/txt/'
                       '{}/{}/numbers.txt'.format(path, edge_type, method), mode='a')

    # if count1 is equal to 1
    if count1 == 1:

        # write header to file
        output_file.write('> Community size of each community\n\n')

        # write stat to file
        output_file.write('- Community {}: {}\n'.format(count1, community.vcount()))

    # if count1 is not equal to 1
    else:

        # write stat to file
        output_file.write('- Community {}: {}\n'.format(count1, community.vcount()))


########################################################################################################################


# saves community entities
def save_community_entities(community, edge_type, method, count1, path):

    # variable to hold entity
    entity = path.split('/', 1)[0]

    # variable to hold output file
    output_file = open('../../data/networks/{}/communities/txt/'
                       '{}/{}/{}.txt'.format(path, edge_type, method, entity), mode='a')

    # variable to hold community entities
    community_entities = [label for label in community.vs['label']]

    # if count1 is equal to 1
    if count1 == 1:

        # write header to file
        output_file.write('> {} in each community\n\n'.format(entity.capitalize()))

        # write headers to file
        output_file.write('> Community {} ({})\n\n'.format(count1, len(community_entities)))

    # if count1 is not equal to 1
    else:

        # write headers to file
        output_file.write('\n> Community {} ({})\n\n'.format(count1, len(community_entities)))

    # for community entity in community entities
    for community_entity in community_entities:

        # write community entity to file
        output_file.write('- {}\n'.format(community_entity))


########################################################################################################################


# plots community
def plot_community(community, edge_type, method, count1, path):

    # variable to hold visual style
    visual_style = {'vertex_label': None,
                    'vertex_color': 'blue',
                    'vertex_size': community.vs['plot_size'],
                    'edge_width': community.es['plot_weight'],
                    'layout': 'kk',
                    'bbox': (1000, 1000),
                    'margin': 40}

    # plot network
    ig.plot(community, '../../data/networks/{}/communities/png/'
                       '{}/{}/community{}.png'.format(path, edge_type, method, count1), **visual_style)


########################################################################################################################


# turns edges into grants
def turn_edges_into_grants(community, edge_type, method, count1, path):

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
        path_temp = '{}/{}'.format(path_split[1], path_temp[2])

    # variable to hold input file
    input_file = open(r'../../network-maker/output/grants/{}/info/grant_{}.pkl'.format(path_temp, path_split[0]), 'rb')
    # load data structure from file
    grant_entities = load(input_file)
    # close input file
    input_file.close()

    # variable to hold entity links
    entity_links = [[community.vs['label'][edge.source], community.vs['label'][edge.target]]
                    for edge in community.es()]

    # variable to hold grants
    grants = OrderedDict()

    # if split path equals to topics
    if path_split[0] == 'topics':

        # set grants
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
    output_file = open('../../data/networks/{}/communities/txt/{}/{}/'
                       'grants.txt'.format(path, edge_type, method), mode='a')

    # if count1 is equal to 1
    if count1 == 1:

        # write header to file
        output_file.write('> Number and value of grants in each community\n\n')

        # write grant number and value to file
        output_file.write('- Community {}:    {:>4d} {}\n'.format(count1, number, currency(value, grouping=True)))

    # if count1 is not equal to 1
    else:

        # write grant number and value to file
        output_file.write('- Community {}:    {:>4d} {}\n'.format(count1, number, currency(value, grouping=True)))

    # return number and value
    return grants, number, value


########################################################################################################################


# calculate modularity
def calc_modularity(community, edge_type, method, count1, path):

    # if community is weighted
    if community.is_weighted():

        # variable to hold infomap communities
        infomap_c = community.community_infomap(edge_weights='weight')
        # variable to hold infomap modularity
        infomap_m = infomap_c.modularity

        spinglass_c = ig.VertexClustering
        spinglass_m = float

        # if network is connected
        if community.is_connected():
            # variable to hold spinglass communities
            spinglass_c = community.community_spinglass(weights='weight')
            # variable to hold spinglass modularity
            spinglass_m = spinglass_c.modularity

        # variable to hold louvain communities
        louvain_c = community.community_multilevel(weights='weight')
        # variable to hold louvain modularity
        louvain_m = louvain_c.modularity

        # variable to hold label propagation communities
        label_prop_c = community.community_label_propagation(weights='weight')
        # variable to hold label propagation modularity
        label_prop_m = label_prop_c.modularity

        # variable to hold leading eigenvector communities
        leading_eigen_c = community.community_leading_eigenvector(weights='weight')
        # variable to hold leading eigenvector modularity
        leading_eigen_m = leading_eigen_c.modularity

        # variable to hold walktrap communities
        walktrap_c = community.community_walktrap(weights='weight', steps=4).as_clustering()
        # variable to hold walktrap modularity
        walktrap_m = walktrap_c.modularity

        # variable to hold fast greedy communities
        fastgreedy_c = community.community_fastgreedy(weights='weight').as_clustering()
        # variable to hold fast greedy modularity
        fastgreedy_m = fastgreedy_c.modularity

        edge_betweenness_c = ig.VertexClustering
        edge_betweenness_m = float

        # if network is connected and number of components is less than or equal to 2
        if community.is_connected() or len(community.components()) <= 2:
            # variable to hold edge betweenness communities
            edge_betweenness_c = community.community_edge_betweenness(directed=False,
                                                                      weights='weight').as_clustering()
            # variable to hold edge betweenness modularity
            edge_betweenness_m = edge_betweenness_c.modularity

    # if community is not weighted
    else:

        # variable to hold infomap communities
        infomap_c = community.community_infomap()
        # variable to hold infomap modularity
        infomap_m = infomap_c.modularity

        spinglass_c = ig.VertexClustering
        spinglass_m = float

        # if network is connected
        if community.is_connected():
            # variable to hold spinglass communities
            spinglass_c = community.community_spinglass()
            # variable to hold spinglass modularity
            spinglass_m = spinglass_c.modularity

        # variable to hold louvain communities
        louvain_c = community.community_multilevel()
        # variable to hold louvain modularity
        louvain_m = louvain_c.modularity

        # variable to hold label propagation communities
        label_prop_c = community.community_label_propagation()
        # variable to hold label propagation modularity
        label_prop_m = label_prop_c.modularity

        # variable to hold leading eigenvector communities
        leading_eigen_c = community.community_leading_eigenvector()
        # variable to hold leading eigenvector modularity
        leading_eigen_m = leading_eigen_c.modularity

        # variable to hold walktrap communities
        walktrap_c = community.community_walktrap(steps=4).as_clustering()
        # variable to hold walktrap modularity
        walktrap_m = walktrap_c.modularity

        # variable to hold fast greedy communities
        fastgreedy_c = community.community_fastgreedy().as_clustering()
        # variable to hold fast greedy modularity
        fastgreedy_m = fastgreedy_c.modularity

        edge_betweenness_c = ig.VertexClustering
        edge_betweenness_m = float

        # if network is connected and number of components is less than or equal to 2
        if community.is_connected() or len(community.components()) <= 2:
            # variable to hold edge betweenness communities
            edge_betweenness_c = community.community_edge_betweenness(directed=False).as_clustering()
            # variable to hold edge betweenness modularity
            edge_betweenness_m = edge_betweenness_c.modularity

    ####################################################################################################################

    # variable to hold output file
    output_file = open('../../data/networks/{}/communities/txt/'
                       '{}/{}/modularity.txt'.format(path, edge_type, method, count1), mode='a')

    # write modularity to file
    # if count1 equals to 1
    if count1 == 1:
        output_file.write('> Community sizes and Modularity scores\n\n')
    output_file.write('> Community {}\n\n'.format(count1))
    output_file.write('- Infomap:             {:3d} {:5.3f}\n'.format(len(infomap_c), infomap_m))

    # if network is connected
    if community.is_connected():
        output_file.write('- Spinglass:           {:3d} {:5.3f}\n'.format(len(spinglass_c), spinglass_m))

    output_file.write('- Louvain:             {:3d} {:5.3f}\n'.format(len(louvain_c), louvain_m))
    output_file.write('- Label Propagation:   {:3d} {:5.3f}\n'.format(len(label_prop_c), label_prop_m))
    output_file.write('- Leading Eigenvector: {:3d} {:5.3f}\n'.format(len(leading_eigen_c), leading_eigen_m))
    output_file.write('- Walktrap:            {:3d} {:5.3f}\n'.format(len(walktrap_c), walktrap_m))
    output_file.write('- Fast Greedy:         {:3d} {:5.3f}\n'.format(len(fastgreedy_c), fastgreedy_m))

    # if network is connected and number of components is less than or equal to 2
    if community.is_connected() or len(community.components()) <= 2:
        output_file.write('- Edge Betweenness:    {:3d} {:5.3f}\n\n'.format(len(edge_betweenness_c),
                                                                            edge_betweenness_m))

    ####################################################################################################################

    # if method equals to louvain
    if method == 'louvain':
        # return louvain communities
        return louvain_c
    # if method equals to spinglass
    elif method == 'spinglass':
        # return spinglass communities
        return spinglass_c
    # if method equals to fastgreedy
    elif method == 'fastgreedy':
        # return fastgreedy communities
        return fastgreedy_c


########################################################################################################################
