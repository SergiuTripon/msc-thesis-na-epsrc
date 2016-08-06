
# third-party library modules
import igraph as ig

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

# gets edge type
def get_edge_type(network, edge_type):

    # if edge type equals to uw
    if edge_type == 'uw':
        # add normalized edge weight attribute
        network.es['norm_weight'] = 1.0
    # if edge type equals to wn
    elif edge_type == 'wn':
        # add normalized edge weight attribute
        network.es['norm_weight'] = network.es['weight']
    # if edge type equals to wv
    elif edge_type == 'wv':
        # add normalized edge weight attribute
        network.es['norm_weight'] = network.es['val']
    # if edge type equals to wnn
    elif edge_type == 'wnn':
        # add normalized edge weight attribute
        network.es['norm_weight'] = network.es['norm_weight']
    # if edge type equals to wnv
    elif edge_type == 'wnv':
        # add normalized edge weight attribute
        network.es['norm_weight'] = network.es['norm_val']

    # return network
    return network


########################################################################################################################


# calculates stats
def calc_stats(network, edge_type, method, path):

    # if edge type equals to unweighted
    if edge_type == 'uw':
        # delete edge type attribute
        del network.es['weight']

    # variables to hold selectables
    network_summary = network.summary()
    node_weights = network.vs["num"]
    node_attr = network.vertex_attributes()
    node_degrees = network.degree()
    degree_dist = network.degree_distribution()
    edge_weights = network.es["norm_weight"]
    edge_attr = network.edge_attributes()

    # variables to hold stats
    node_count = network.vcount()
    edge_count = network.ecount()
    directed_status = 'Directed' if network.is_directed() else 'Undirected'
    weighted_status = 'Yes' if network.is_weighted() else 'No'
    connected_status = 'Yes' if network.is_connected() else 'No'
    avg_degree = ig.mean(network.degree(loops=False))
    avg_weighted_degree = float
    # if network is weighted
    if network.is_weighted():
        avg_weighted_degree = ig.mean(network.strength(weights='norm_weight'))
    diameter = network.diameter(directed=False, weights='norm_weight')
    radius = network.radius(mode='ALL')
    density = network.density()
    modularity = network.community_multilevel(weights='norm_weight').modularity
    communities = len(network.community_multilevel(weights='norm_weight'))
    components = len(network.components())
    closeness = ig.mean(network.closeness(weights='norm_weight'))
    node_betweenness = ig.mean(network.betweenness(directed=False, weights='norm_weight'))
    edge_betweenness = ig.mean(network.edge_betweenness(directed=False, weights='norm_weight'))
    avg_clustering_coeff = ig.mean(network.transitivity_avglocal_undirected())
    eigenvector_centrality = ig.mean(network.eigenvector_centrality(directed=False, weights='norm_weight'))
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

    # add edge weight column to the network
    network.es['weight'] = network.es['norm_weight']


########################################################################################################################


# calculate modularity
def calc_modularity(network, edge_type, method, path, i):

    # variable to hold infomap communities
    infomap_c = network.community_infomap(edge_weights='norm_weight')
    # variable to hold infomap modularity
    infomap_m = infomap_c.modularity

    spinglass_c = ig.VertexClustering
    spinglass_m = float

    # if network is connected
    if network.is_connected():
        # variable to hold spinglass communities
        spinglass_c = network.community_spinglass(weights='norm_weight')
        # variable to hold spinglass modularity
        spinglass_m = spinglass_c.modularity

    # variable to hold louvain communities
    louvain_c = network.community_multilevel(weights='norm_weight')
    # variable to hold louvain modularity
    louvain_m = louvain_c.modularity

    # variable to hold label propagation communities
    label_prop_c = network.community_label_propagation(weights='norm_weight')
    # variable to hold label propagation modularity
    label_prop_m = label_prop_c.modularity

    # variable to hold leading eigenvector communities
    leading_eigen_c = network.community_leading_eigenvector(weights='norm_weight')
    # variable to hold leading eigenvector modularity
    leading_eigen_m = leading_eigen_c.modularity

    # variable to hold walktrap communities
    walktrap_c = network.community_walktrap(weights='norm_weight', steps=4).as_clustering()
    # variable to hold walktrap modularity
    walktrap_m = walktrap_c.modularity

    # variable to hold fast greedy communities
    fastgreedy_c = network.community_fastgreedy(weights='norm_weight').as_clustering()
    # variable to hold fast greedy modularity
    fastgreedy_m = fastgreedy_c.modularity

    edge_betweenness_c = ig.VertexClustering
    edge_betweenness_m = float

    # if network is connected and number of components is less than or equal to 2
    if network.is_connected() or len(network.components()) <= 2:
        # variable to hold edge betweenness communities
        edge_betweenness_c = network.community_edge_betweenness(directed=False, weights='norm_weight').as_clustering()
        # variable to hold edge betweenness modularity
        edge_betweenness_m = edge_betweenness_c.modularity

    ####################################################################################################################

    # if i does not exist
    if not i:

        # variable to hold output file
        output_file = open('../../data/networks/{}/network/txt/'
                           '{}/{}/modularity.txt'.format(path, edge_type, method), mode='w')

        # write modularity to file
        output_file.write('> Modularity scores and community sizes\n\n')
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

    # if i exists
    elif i:

        # variable to hold output file
        output_file = open('../../data/networks/{}/communities/txt/'
                           '{}/{}/modularity.txt'.format(path, edge_type, method, i), mode='a')

        # write modularity to file
        # if i equals to 1
        if i == 1:
            output_file.write('> Modularity scores and community sizes\n\n')
        output_file.write('> Community {}\n\n'.format(i))
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


# plots network
def plot_network(network, edge_type, method, path):

    # variable to hold visual style
    visual_style = {'vertex_label': None,
                    'vertex_color': 'blue',
                    'vertex_size': network.vs['norm_num'],
                    'edge_width': network.es['norm_weight'],
                    'layout': 'kk',
                    'bbox': (1000, 1000),
                    'margin': 40}

    # plot network
    ig.plot(network, '../../data/networks/{}/network/png/'
                     '{}/{}/network.png'.format(path, edge_type, method), **visual_style)


########################################################################################################################
