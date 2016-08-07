
# local python files
import network as na
import sub_communities as sca

# third-party library modules
import igraph as ig
from pickle import load
from random import randint
from collections import OrderedDict
from locale import setlocale, LC_ALL, currency

########################################################################################################################


# analyses communities
def analyse_communities(network, communities, edge_type, method, threshold, path):

    # check communities
    if check_communities(communities, edge_type, method, path):
        # return
        return

    # add normalized node membership column to network
    network.vs['membership'] = norm_membership(communities.membership)
    # print progress
    # print('> Network membership normalized ({}/{}/{}).'.format(path, edge_type, method))

    # save communities
    save_communities(network, communities, edge_type, method, threshold, path)
    # print progress
    # print('> Communities saved ({}/{}/{}).'.format(path, edge_type, method))

    # save community membership
    save_community_membership(network, edge_type, method, path)
    # print progress
    # print('> Community membership saved ({}/{}/{}).'.format(path, edge_type, method))

    # save community topics and print progress
    save_community_topics(network, edge_type, method, communities, path)
    # print progress
    # print('> Community topics saved ({}/{}/{}).'.format(path, edge_type, method))

    # plot community overview
    plot_community_overview(network, edge_type, method, communities, communities.membership, True, path)
    plot_community_overview(network, edge_type, method, communities, communities.membership, False, path)
    # print progress
    # print('> Community overview plotted ({}/{}/{}).'.format(path, edge_type, method))


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


# saves communities
def save_communities(network, communities, edge_type, method, threshold, path):

    # variable to hold unique grants
    unique_grants = OrderedDict()

    # variable to hold total number and value
    total_number, total_value = 0, 0

    # variable to hold count1 set to 1
    count1 = 1

    # for community in communities
    for community in communities:

        # if size of community is greater than threshold
        if len(community) > threshold:

            # variable to hold sub-graph
            sub_graph = network.subgraph(communities[count1 - 1], 'create_from_scratch')

            # variable to hold output file
            output_file = open('../../data/networks/{}/communities/graphml/{}/{}/'
                               'community{}.graphml'.format(path, edge_type, method, count1), mode='w')

            # write sub-graph structure to file
            sub_graph.write_graphml(output_file)

            # variable to hold stats file
            stats_file = open('../../data/networks/{}/communities/txt/'
                              '{}/{}/numbers.txt'.format(path, edge_type, method), mode='a')

            # write stat to file
            stats_file.write('Community {}: {}\n'.format(count1, len(community)))

            ############################################################################################################

            # rename columns
            sub_graph = na.rename_columns(sub_graph)
            # print progress
            # print('> Community columns renamed. ({} - {})'.format(edge_type, method))

            ############################################################################################################

            # plot communities
            plot_communities(sub_graph, edge_type, method, count1, path)
            # print progress
            # print('> Communities plotted ({} - {}).'.format(edge_type, method))

            ############################################################################################################

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
                # return
                continue

            ############################################################################################################

            # variable to hold sub-communities
            sub_communities = calc_modularity(sub_graph, edge_type, method, count1, path)
            # print progress
            # print('> Community modularity calculated ({} - {}).'.format(edge_type, method))

            ############################################################################################################

            # analyse sub-communities
            sca.analyse_sub_communities(sub_graph, sub_communities, edge_type, method, count1, path)

            ############################################################################################################

            # increment count1
            count1 += 1

    # set locale to Great Britain
    setlocale(LC_ALL, 'en_GB.utf8')

    # variable to hold output file
    output_file = open('../../data/networks/{}/communities/txt/{}/{}/'
                       'grants.txt'.format(path, edge_type, method), mode='a')
    # write grant number and value to file
    output_file.write('\n> Total:          {:>4d} {}\n'.format(total_number, currency(total_value, grouping=True)))

    # variable to hold total number
    total_number = len(unique_grants)
    # variable to hold total value
    total_value = sum([attr for attr in unique_grants.values()])

    # variable to hold output file
    output_file = open('../../data/networks/{}/communities/txt/{}/{}/'
                       'grants.txt'.format(path, edge_type, method), mode='a')
    # write grant number and value to file
    output_file.write('> Total (unique): {:>4d} {}'.format(total_number, currency(total_value, grouping=True)))


########################################################################################################################


# turns edges into grants
def turn_edges_into_grants(community, edge_type, method, count1, path):

    # variable to hold temporary path
    path_temp = path.replace('topics/', '').replace('/network-a', '')

    # variable to hold input file
    input_file = open(r'../../network-maker/output/grants/{}/info/grant_topics.pkl'.format(path_temp), 'rb')
    # load data structure from file
    grant_topics = load(input_file)
    # close input file
    input_file.close()

    # variable to hold topic links
    topic_links = [[community.vs['label'][edge.source], community.vs['label'][edge.target]] for edge in community.es()]

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
    output_file = open('../../data/networks/{}/communities/txt/{}/{}/'
                       'grants.txt'.format(path, edge_type, method), mode='a')
    # write grant number and value to file
    output_file.write('> Community {}:    {:>4d} {}\n'.format(count1, number, currency(value, grouping=True)))

    # return number and value
    return grants, number, value


########################################################################################################################


# calculate modularity
def calc_modularity(community, edge_type, method, count1, path):

    # variable to hold infomap communities
    infomap_c = community.community_infomap(edge_weights='norm_weight')
    # variable to hold infomap modularity
    infomap_m = infomap_c.modularity

    spinglass_c = ig.VertexClustering
    spinglass_m = float

    # if network is connected
    if community.is_connected():
        # variable to hold spinglass communities
        spinglass_c = community.community_spinglass(weights='norm_weight')
        # variable to hold spinglass modularity
        spinglass_m = spinglass_c.modularity

    # variable to hold louvain communities
    louvain_c = community.community_multilevel(weights='norm_weight')
    # variable to hold louvain modularity
    louvain_m = louvain_c.modularity

    # variable to hold label propagation communities
    label_prop_c = community.community_label_propagation(weights='norm_weight')
    # variable to hold label propagation modularity
    label_prop_m = label_prop_c.modularity

    # variable to hold leading eigenvector communities
    leading_eigen_c = community.community_leading_eigenvector(weights='norm_weight')
    # variable to hold leading eigenvector modularity
    leading_eigen_m = leading_eigen_c.modularity

    # variable to hold walktrap communities
    walktrap_c = community.community_walktrap(weights='norm_weight', steps=4).as_clustering()
    # variable to hold walktrap modularity
    walktrap_m = walktrap_c.modularity

    # variable to hold fast greedy communities
    fastgreedy_c = community.community_fastgreedy(weights='norm_weight').as_clustering()
    # variable to hold fast greedy modularity
    fastgreedy_m = fastgreedy_c.modularity

    edge_betweenness_c = ig.VertexClustering
    edge_betweenness_m = float

    # if network is connected and number of components is less than or equal to 2
    if community.is_connected() or len(community.components()) <= 2:
        # variable to hold edge betweenness communities
        edge_betweenness_c = community.community_edge_betweenness(directed=False,
                                                                  weights='norm_weight').as_clustering()
        # variable to hold edge betweenness modularity
        edge_betweenness_m = edge_betweenness_c.modularity

    ####################################################################################################################

    # variable to hold output file
    output_file = open('../../data/networks/{}/communities/txt/'
                       '{}/{}/modularity.txt'.format(path, edge_type, method, count1), mode='a')

    # write modularity to file
    # if count1 equals to 1
    if count1 == 1:
        output_file.write('> Modularity scores and community sizes\n\n')
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
                       '{}/{}/topics.txt'.format(path, edge_type, method), mode='a')

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
def plot_communities(community, edge_type, method, count1, path):

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
                       '{}/{}/community{}.png'.format(path, edge_type, method, count1), **visual_style)


########################################################################################################################
