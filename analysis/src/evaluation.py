#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
import igraph as ig

########################################################################################################################


# calculates similarity
def calc_similarity(network, path):

    # variable to hold membership
    membership = network.vs['membership']

    # variable to hold edges within communities
    edges_within = [(edge.source, edge.target) for edge in network.es()
                    if membership[edge.tuple[0]] == membership[edge.tuple[1]]]

    # variable to hold edges between communities
    edges_between = [(edge.source, edge.target) for edge in network.es()
                     if membership[edge.tuple[0]] != membership[edge.tuple[1]]]

    # variable to hold output file
    output_file = open('{}/network/txt/wnn/louvain/similarity.txt'.format(path), mode='a')

    # write header to file
    output_file.write('> Similarity\n\n')

    # write number of edges within communities to file
    output_file.write('- Number of edges within communities:  {}\n'.format(len(edges_within)))

    # write number of edges between communities to file
    output_file.write('- Number of edges between communities: {}\n\n'.format(len(edges_between)))

    ####################################################################################################################

    # variable to hold methods
    methods = network.similarity_dice, network.similarity_jaccard

    # for method in methods
    for method in methods:

        # variable to hold similarity within communities
        similarity_within = method(vertices=None, pairs=edges_within)

        # variable to hold similarity between communities
        similarity_between = method(vertices=None, pairs=edges_between)

        # variable to hold average within communities
        average_within = sum(similarity_within) / len(similarity_within)

        # variable to hold average between communities
        average_between = sum(similarity_between) / len(similarity_between)

        # variable to hold difference in similarity within and between communities
        difference_within_between = average_within - average_between

        ################################################################################################################

        # write sub-header to file
        output_file.write('> {} similarity\n\n'.format(method.__name__.replace('similarity_', '').capitalize()))

        # write average similarity within communities to file
        output_file.write('- Average similarity within communities:  {:.3f}\n'.format(average_within))

        # print average similarity between communities to file
        output_file.write('- Average similarity between communities: {:.3f}\n\n'.format(average_between))

        # print difference in similarity of edges within and between to file
        output_file.write('- Difference in similarity between and within communities: '
                          '{:.3f}\n\n'.format(difference_within_between))


########################################################################################################################


# main function
def main():

    # variable to hold path
    path = '../../data/networks/topics/current/network-a'

    # variable to hold network
    network = ig.Graph.Read_GraphML('{}/network/graphml/wnn/louvain/membership.graphml'.format(path))

    # calculate similarity
    calc_similarity(network, path)

    # print progress
    print('> Similarity calculated.')


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
