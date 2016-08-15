
# local python files
import communities as ca

# third-party library modules
import igraph as ig
from pickle import load
from collections import OrderedDict
from locale import setlocale, LC_ALL, currency

########################################################################################################################


# analyses network
def analyse_network(edge_type, method, attr, threshold, path):

    # variable to hold network
    network = ig.Graph.Read_GraphML('../../data/networks/{}/network/graphml/network.graphml'.format(path))

    ####################################################################################################################

    # rename columns
    network = rename_columns(network)

    ####################################################################################################################

    # if attributes equals to all
    if attr == 'all':
        # add normalized node number column to network
        network.vs['norm_num'] = norm_vals(network.vs['num'], 20, 60)
        # add normalized node value column to network
        network.vs['norm_val'] = norm_vals(network.vs['val'], 20, 60)
        # add normalized edge weight column to network
        network.es['norm_weight'] = norm_vals(network.es['weight'], 1, 10)
        # add normalized edge value column to network
        network.es['norm_val'] = norm_vals(network.es['val'], 1, 10)
    # if attributes equals to half
    elif attr == 'half':
        # add normalized node number column to network
        network.vs['norm_num'] = norm_vals(network.vs['num'], 20, 60)
        # add normalized edge weight column to network
        network.es['norm_weight'] = norm_vals(network.es['weight'], 1, 10)

    ####################################################################################################################

    # get network type and print progress
    network_type = get_network_type(path)

    ####################################################################################################################

    # set edge type and print progress
    set_edge_type(network, edge_type)

    ####################################################################################################################

    # calculate network stats
    calc_stats(network, edge_type, method, path)

    ####################################################################################################################

    # plot network
    plot_network(network, edge_type, method, path)

    ####################################################################################################################

    # if edge type does not equal to uw
    if edge_type != 'uw':
        # check robustness
        check_robustness(network, edge_type, method, path)

    ####################################################################################################################

    # if network type equals to topic a or researcher b
    if network_type == 'topic-a' or network_type == 'researcher-b':

        # turn edges into grants
        turn_edges_into_grants(network, edge_type, method, path)

    ####################################################################################################################

    # calculate modularity
    communities = calc_modularity(network, edge_type, method, path)

    ####################################################################################################################

    # analyse communities
    ca.analyse_communities(network, communities, network_type, edge_type, method, threshold, path)


########################################################################################################################


# renames columns
def rename_columns(network):

    # if number is in node attributes
    if 'Num' in network.vs.attributes():
        # add node number attribute
        network.vs['num'] = network.vs['Num']
        # delete node number attribute
        del network.vs['Num']
    # if value is in node attributes
    if 'Val' in network.vs.attributes():
        # add node value attribute
        network.vs['val'] = network.vs['Val']
        # delete node value attribute
        del network.vs['Val']

    # if number is in edge attributes
    if 'Num' in network.es.attributes():
        # add edge number attribute
        network.es['num'] = network.es['Num']
        # delete edge number attribute
        del network.es['Num']
    # if value is in edge attributes
    if 'Val' in network.es.attributes():
        # add edge value attribute
        network.es['val'] = network.es['Val']
        # delete edge value attribute
        del network.es['Val']

    # if normalized number is in node attributes
    if 'NormNum' in network.vs.attributes():
        # add node normalized number attribute
        network.vs['norm_num'] = network.vs['NormNum']
        # delete node normalized number attribute
        del network.vs['NormNum']
    # if normalized value is in node attributes
    if 'NormVal' in network.vs.attributes():
        # add node normalized value attribute
        network.vs['norm_val'] = network.vs['NormVal']
        # delete node normalized value attribute
        del network.vs['NormVal']

    # if normalized weight is in node attributes
    if 'NormWeight' in network.es.attributes():
        # add node normalized weight attribute
        network.es['norm_weight'] = network.es['NormWeight']
        # delete node normalized weight attribute
        del network.es['NormWeight']
    # if normalized value is in node attributes
    if 'NormVal' in network.es.attributes():
        # add node normalized value attribute
        network.es['norm_val'] = network.es['NormVal']
        # delete node normalized value attribute
        del network.es['NormVal']

    # if edge id is in edge attributes
    if 'Edge Id' in network.es.attributes():
        # delete edge id attribute
        del network.es['Edge Id']
    # if edge label is in edge attributes
    if 'Edge Label' in network.es.attributes():
        # delete edge label attribute
        del network.es['Edge Label']

    # return network
    return network


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


# gets network type
def get_network_type(path):

    # variable to hold split path
    path_split = path.split('/', 1)

    # variable to hold entity
    entity = path_split[0][:-1]

    # variable to hold plan
    plan = path_split[1].replace('current/network-', '')
    # set plan
    plan = plan.replace('past/2000-2010/network-', '')
    # set plan
    plan = plan.replace('past/1990-2000/network-', '')

    # variable to hold network type
    network_type = '{}-{}'.format(entity, plan)

    # return network type
    return network_type


########################################################################################################################


# sets edge type
def set_edge_type(network, edge_type):

    # if edge type equals to uw
    if edge_type == 'uw':
        # delete edge weight attribute
        del network.es['weight']
        # add node plot size attribute
        network.vs['plot_size'] = 30.0
        # add edge plot weight attribute
        network.es['plot_weight'] = 1.0
    # if edge type equals to wn
    elif edge_type == 'wn':
        # add node plot size attribute
        network.vs['plot_size'] = network.vs['norm_num']
        # add edge plot weight attribute
        network.es['plot_weight'] = network.es['norm_weight']
    # if edge type equals to wv
    elif edge_type == 'wv':
        # delete edge weight attribute
        del network.es['weight']
        # add edge weight attribute
        network.es['weight'] = network.es['val']
        # add node plot size attribute
        network.vs['plot_size'] = network.vs['norm_val']
        # add edge plot weight attribute
        network.es['plot_weight'] = network.es['norm_val']
    # if edge type equals to wnn
    elif edge_type == 'wnn':
        # delete edge weight attribute
        del network.es['weight']
        # add edge weight attribute
        network.es['weight'] = network.es['norm_weight']
        # add node plot size attribute
        network.vs['plot_size'] = network.vs['norm_num']
        # add edge plot weight attribute
        network.es['plot_weight'] = network.es['norm_weight']
    # if edge type equals to wnv
    elif edge_type == 'wnv':
        # delete edge weight attribute
        del network.es['weight']
        # add edge weight attribute
        network.es['weight'] = network.es['norm_val']
        # add node plot size attribute
        network.vs['plot_size'] = network.vs['norm_val']
        # add edge plot weight attribute
        network.es['plot_weight'] = network.es['norm_val']

    # return network
    return network


########################################################################################################################


# calculates stats
def calc_stats(network, edge_type, method, path):

    # if network is weighted
    if network.is_weighted():

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

    # if network is not weighted
    else:

        # variables to hold stats
        node_count = network.vcount()
        edge_count = network.ecount()
        directed_status = 'Directed' if network.is_directed() else 'Undirected'
        weighted_status = 'Yes' if network.is_weighted() else 'No'
        connected_status = 'Yes' if network.is_connected() else 'No'
        avg_degree = ig.mean(network.degree(loops=False))
        avg_weighted_degree = ig.mean(network.strength())
        diameter = network.diameter(directed=False)
        radius = network.radius(mode='ALL')
        density = network.density()
        modularity = network.community_multilevel().modularity
        communities = len(network.community_multilevel())
        components = len(network.components())
        closeness = ig.mean(network.closeness())
        node_betweenness = ig.mean(network.betweenness(directed=False))
        edge_betweenness = ig.mean(network.edge_betweenness(directed=False))
        avg_clustering_coeff = ig.mean(network.transitivity_avglocal_undirected())
        eigenvector_centrality = ig.mean(network.eigenvector_centrality(directed=False))
        avg_path_length = ig.mean(network.average_path_length(directed=False))

    # variable to hold output file
    output_file = open('../../data/networks/{}/network/txt/'
                       '{}/{}/stats.txt'.format(path, edge_type, method), mode='w')

    # write stats to file
    output_file.write('> Network Overview\n\n')
    output_file.write('- Nodes: {}\n'.format(node_count))
    output_file.write('- Edges: {}\n'.format(edge_count))
    output_file.write('- Type: {}\n'.format(directed_status))
    output_file.write('- Weighted: {}\n'.format(weighted_status))
    output_file.write('- Connected: {}\n'.format(connected_status))
    output_file.write('- Average Degree: {0:.3f}\n'.format(avg_degree))
    # if network is weighted
    if network.is_weighted():
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


# plots network
def plot_network(network, edge_type, method, path):

    # variable to hold visual style
    visual_style = {'vertex_label': None,
                    'vertex_color': 'blue',
                    'vertex_size': network.vs['plot_size'],
                    'edge_width': network.es['plot_weight'],
                    'layout': 'kk',
                    'bbox': (1000, 1000),
                    'margin': 40}

    # plot network
    ig.plot(network, '../../data/networks/{}/network/png/'
                     '{}/{}/network.png'.format(path, edge_type, method), **visual_style)


########################################################################################################################


# check robustness
def check_robustness(network, edge_type, method, path):

    # variable to hold threshold
    threshold = 0
    # if edge type equals to wn
    if edge_type == 'wn':
        threshold = 4
    # if edge type equals to wv
    if edge_type == 'wv':
        threshold = 7099177.11
    # if edge type equals to wnn or wnv
    elif edge_type == 'wnn' or edge_type == 'wnv':
        threshold = 2

    # variable to hold network copy
    network_copy = network.copy()

    # variable to hold edges
    edges = [edge for edge, edge_weight in zip(network_copy.es(), network_copy.es['weight'])
             if int(edge_weight) < threshold]

    # delete edges
    network_copy.delete_edges(edges)

    # variable to hold nodes
    nodes = [node for node, node_degree in zip(network_copy.vs(), network_copy.degree()) if int(node_degree) == 0]

    # delete nodes
    network_copy.delete_vertices(nodes)

    ####################################################################################################################

    # variable to hold infomap communities
    infomap_c = network_copy.community_infomap(edge_weights='weight')
    # variable to hold infomap modularity
    infomap_m = infomap_c.modularity

    spinglass_c = ig.VertexClustering
    spinglass_m = float

    # if network is connected
    if network_copy.is_connected():
        # variable to hold spinglass communities
        spinglass_c = network_copy.community_spinglass(weights='weight')
        # variable to hold spinglass modularity
        spinglass_m = spinglass_c.modularity

    # variable to hold louvain communities
    louvain_c = network_copy.community_multilevel(weights='weight')
    # variable to hold louvain modularity
    louvain_m = louvain_c.modularity

    # variable to hold label propagation communities
    label_prop_c = network_copy.community_label_propagation(weights='weight')
    # variable to hold label propagation modularity
    label_prop_m = label_prop_c.modularity

    # variable to hold leading eigenvector communities
    leading_eigen_c = network_copy.community_leading_eigenvector(weights='weight')
    # variable to hold leading eigenvector modularity
    leading_eigen_m = leading_eigen_c.modularity

    # variable to hold walktrap communities
    walktrap_c = network_copy.community_walktrap(weights='weight', steps=4).as_clustering()
    # variable to hold walktrap modularity
    walktrap_m = walktrap_c.modularity

    # variable to hold fast greedy communities
    fastgreedy_c = network_copy.community_fastgreedy(weights='weight').as_clustering()
    # variable to hold fast greedy modularity
    fastgreedy_m = fastgreedy_c.modularity

    edge_betweenness_c = ig.VertexClustering
    edge_betweenness_m = float

    # if network is connected and number of components is less than or equal to 2
    if network_copy.is_connected() or len(network_copy.components()) <= 2:
        # variable to hold edge betweenness communities
        edge_betweenness_c = network_copy.community_edge_betweenness(directed=False,
                                                                     weights='weight').as_clustering()
        # variable to hold edge betweenness modularity
        edge_betweenness_m = edge_betweenness_c.modularity

    ####################################################################################################################

    # variable to hold output file
    output_file = open('../../data/networks/{}/network/txt/'
                       '{}/{}/robustness.txt'.format(path, edge_type, method), mode='w')

    # write modularity to file
    output_file.write('> Network robustness check\n\n')
    output_file.write('> Nodes: {}\n'.format(network_copy.vcount()))
    output_file.write('> Edges: {}\n\n'.format(network_copy.ecount()))
    output_file.write('> Community sizes and Modularity scores\n\n')
    output_file.write('- Infomap:             {:3d} {:5.3f}\n'.format(len(infomap_c), infomap_m))

    # if network is connected
    if network_copy.is_connected():
        output_file.write('- Spinglass:           {:3d} {:5.3f}\n'.format(len(spinglass_c), spinglass_m))

    output_file.write('- Louvain:             {:3d} {:5.3f}\n'.format(len(louvain_c), louvain_m))
    output_file.write('- Label Propagation:   {:3d} {:5.3f}\n'.format(len(label_prop_c), label_prop_m))
    output_file.write('- Leading Eigenvector: {:3d} {:5.3f}\n'.format(len(leading_eigen_c), leading_eigen_m))
    output_file.write('- Walktrap:            {:3d} {:5.3f}\n'.format(len(walktrap_c), walktrap_m))
    output_file.write('- Fast Greedy:         {:3d} {:5.3f}\n'.format(len(fastgreedy_c), fastgreedy_m))

    # if network is connected and number of components is less than or equal to 2
    if network_copy.is_connected() or len(network_copy.components()) <= 2:
        output_file.write('- Edge Betweenness:    {:3d} {:5.3f}\n\n'.format(len(edge_betweenness_c),
                                                                            edge_betweenness_m))


########################################################################################################################


# turns edges into grants
def turn_edges_into_grants(network, edge_type, method, path):

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
    entity_links = [[network.vs['label'][edge.source], network.vs['label'][edge.target]] for edge in
                    network.es()]

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
    output_file = open('../../data/networks/{}/network/txt/{}/{}/'
                       'grants.txt'.format(path, edge_type, method), mode='w')

    # write header to file
    output_file.write('> Number and value of grants in the network\n\n')

    # write grant number and value to file
    output_file.write('- Total (unique): {:>4d} {}\n'.format(number, currency(value, grouping=True)))


########################################################################################################################


# calculate modularity
def calc_modularity(network, edge_type, method, path):

    # if network is weighted
    if network.is_weighted():

        # variable to hold infomap communities
        infomap_c = network.community_infomap(edge_weights='weight')
        # variable to hold infomap modularity
        infomap_m = infomap_c.modularity

        spinglass_c = ig.VertexClustering
        spinglass_m = float

        # if network is connected
        if network.is_connected():
            # variable to hold spinglass communities
            spinglass_c = network.community_spinglass(weights='weight')
            # variable to hold spinglass modularity
            spinglass_m = spinglass_c.modularity

        # variable to hold louvain communities
        louvain_c = network.community_multilevel(weights='weight')
        # variable to hold louvain modularity
        louvain_m = louvain_c.modularity

        # variable to hold label propagation communities
        label_prop_c = network.community_label_propagation(weights='weight')
        # variable to hold label propagation modularity
        label_prop_m = label_prop_c.modularity

        # variable to hold leading eigenvector communities
        leading_eigen_c = network.community_leading_eigenvector(weights='weight')
        # variable to hold leading eigenvector modularity
        leading_eigen_m = leading_eigen_c.modularity

        # variable to hold walktrap communities
        walktrap_c = network.community_walktrap(weights='weight', steps=4).as_clustering()
        # variable to hold walktrap modularity
        walktrap_m = walktrap_c.modularity

        # variable to hold fast greedy communities
        fastgreedy_c = network.community_fastgreedy(weights='weight').as_clustering()
        # variable to hold fast greedy modularity
        fastgreedy_m = fastgreedy_c.modularity

        edge_betweenness_c = ig.VertexClustering
        edge_betweenness_m = float

        # if network is connected and number of components is less than or equal to 2
        if network.is_connected() or len(network.components()) <= 2:
            # variable to hold edge betweenness communities
            edge_betweenness_c = network.community_edge_betweenness(directed=False, weights='weight').as_clustering()
            # variable to hold edge betweenness modularity
            edge_betweenness_m = edge_betweenness_c.modularity

    # if network is not weighted
    else:

        # variable to hold infomap communities
        infomap_c = network.community_infomap()
        # variable to hold infomap modularity
        infomap_m = infomap_c.modularity

        spinglass_c = ig.VertexClustering
        spinglass_m = float

        # if network is connected
        if network.is_connected():
            # variable to hold spinglass communities
            spinglass_c = network.community_spinglass()
            # variable to hold spinglass modularity
            spinglass_m = spinglass_c.modularity

        # variable to hold louvain communities
        louvain_c = network.community_multilevel()
        # variable to hold louvain modularity
        louvain_m = louvain_c.modularity

        # variable to hold label propagation communities
        label_prop_c = network.community_label_propagation()
        # variable to hold label propagation modularity
        label_prop_m = label_prop_c.modularity

        # variable to hold leading eigenvector communities
        leading_eigen_c = network.community_leading_eigenvector()
        # variable to hold leading eigenvector modularity
        leading_eigen_m = leading_eigen_c.modularity

        # variable to hold walktrap communities
        walktrap_c = network.community_walktrap(steps=4).as_clustering()
        # variable to hold walktrap modularity
        walktrap_m = walktrap_c.modularity

        # variable to hold fast greedy communities
        fastgreedy_c = network.community_fastgreedy().as_clustering()
        # variable to hold fast greedy modularity
        fastgreedy_m = fastgreedy_c.modularity

        edge_betweenness_c = ig.VertexClustering
        edge_betweenness_m = float

        # if network is connected and number of components is less than or equal to 2
        if network.is_connected() or len(network.components()) <= 2:
            # variable to hold edge betweenness communities
            edge_betweenness_c = network.community_edge_betweenness(directed=False).as_clustering()
            # variable to hold edge betweenness modularity
            edge_betweenness_m = edge_betweenness_c.modularity

    ####################################################################################################################

    # variable to hold output file
    output_file = open('../../data/networks/{}/network/txt/'
                       '{}/{}/modularity.txt'.format(path, edge_type, method), mode='w')

    # write modularity to file
    output_file.write('> Community sizes and Modularity scores\n\n')
    output_file.write('- Infomap:             {:3d} {:5.3f}\n'.format(len(infomap_c), infomap_m))

    # if network is connected
    if network.is_connected():
        output_file.write('- Spinglass:           {:3d} {:5.3f}\n'.format(len(spinglass_c), spinglass_m))

    output_file.write('- Louvain:             {:3d} {:5.3f}\n'.format(len(louvain_c), louvain_m))
    output_file.write('- Label Propagation:   {:3d} {:5.3f}\n'.format(len(label_prop_c), label_prop_m))
    output_file.write('- Leading Eigenvector: {:3d} {:5.3f}\n'.format(len(leading_eigen_c), leading_eigen_m))
    output_file.write('- Walktrap:            {:3d} {:5.3f}\n'.format(len(walktrap_c), walktrap_m))
    output_file.write('- Fast Greedy:         {:3d} {:5.3f}\n'.format(len(fastgreedy_c), fastgreedy_m))

    # if network is connected and number of components is less than or equal to 2
    if network.is_connected() or len(network.components()) <= 2:
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
