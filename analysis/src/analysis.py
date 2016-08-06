#!/usr/bin/env python3

########################################################################################################################

# local python files
import network as na
import communities as ca
import sub_communities as sca

# third-party library modules
import os
import glob
import igraph as ig
import pandas as pd
import networkx as nx
import graphistry as gp

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

        # variables to hold methods
        method1, method2, method3 = 'louvain', 'spinglass', 'fastgreedy'
        # variables to hold time periods
        time_period1, time_period2, time_period3 = 'current', 'past1', 'past2'

        # run network a
        AnalyseTopicNetwork.run_network_a(time_period1, method1)
        AnalyseTopicNetwork.run_network_a(time_period1, method2)
        AnalyseTopicNetwork.run_network_a(time_period1, method3)

        AnalyseTopicNetwork.run_network_a(time_period2, method1)
        AnalyseTopicNetwork.run_network_a(time_period2, method2)
        AnalyseTopicNetwork.run_network_a(time_period2, method3)

        AnalyseTopicNetwork.run_network_a(time_period3, method1)
        AnalyseTopicNetwork.run_network_a(time_period3, method2)
        AnalyseTopicNetwork.run_network_a(time_period3, method3)

        ################################################################################################################

        # run network b
        AnalyseTopicNetwork.run_network_b(time_period1, method1)
        AnalyseTopicNetwork.run_network_b(time_period1, method2)
        AnalyseTopicNetwork.run_network_b(time_period1, method3)

        AnalyseTopicNetwork.run_network_b(time_period2, method1)
        AnalyseTopicNetwork.run_network_b(time_period2, method2)
        AnalyseTopicNetwork.run_network_b(time_period2, method3)

        AnalyseTopicNetwork.run_network_b(time_period3, method1)
        AnalyseTopicNetwork.run_network_b(time_period3, method2)
        AnalyseTopicNetwork.run_network_b(time_period3, method3)

    ####################################################################################################################

    @staticmethod
    # runs network a
    def run_network_a(time_period, method):

        # variables to hold paths
        path1 = 'topics/current/network-a'
        path2 = 'topics/past/2000-2010/network-a'
        path3 = 'topics/past/1990-2000/network-a'
        # variables to hold edge types
        edge_type1, edge_type2, edge_type3, edge_type4, edge_type5 = 'uw', 'wn', 'wv', 'wnn', 'wnv'

        # if time period equals to current and method equals to louvain
        if time_period == 'current' and method == 'louvain':

            # analyse network a using louvain
            AnalyseTopicNetwork.analyse_network_a(edge_type1, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type2, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type3, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type4, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type5, method, path1)

        # if time period equals to current and method equals to spinglass
        if time_period == 'current' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseTopicNetwork.analyse_network_a(edge_type1, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type2, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type3, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type4, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type5, method, path1)

        # if time period equals to current and method equals to fastgreedy
        if time_period == 'current' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseTopicNetwork.analyse_network_a(edge_type1, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type2, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type3, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type4, method, path1)
            AnalyseTopicNetwork.analyse_network_a(edge_type5, method, path1)

        ################################################################################################################

        # if time period equals to past1 and method equals to louvain
        if time_period == 'past1' and method == 'louvain':

            # analyse network a using louvain
            AnalyseTopicNetwork.analyse_network_a(edge_type1, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type2, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type3, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type4, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type5, method, path2)

        # if time period equals to past1 and method equals to spinglass
        if time_period == 'past1' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseTopicNetwork.analyse_network_a(edge_type1, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type2, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type3, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type4, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type5, method, path2)

        # if time period equals to past1 and method equals to fastgreedy
        if time_period == 'past1' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseTopicNetwork.analyse_network_a(edge_type1, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type2, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type3, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type4, method, path2)
            AnalyseTopicNetwork.analyse_network_a(edge_type5, method, path2)

        ################################################################################################################

        # if time period equals to past2 and method equals to louvain
        if time_period == 'past2' and method == 'louvain':

            # analyse network a using louvain
            AnalyseTopicNetwork.analyse_network_a(edge_type1, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type2, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type3, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type4, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type5, method, path3)

        # if time period equals to past2 and method equals to spinglass
        if time_period == 'past2' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseTopicNetwork.analyse_network_a(edge_type1, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type2, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type3, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type4, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type5, method, path3)

        # if time period equals to past2 and method equals to fastgreedy
        if time_period == 'past2' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseTopicNetwork.analyse_network_a(edge_type1, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type2, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type3, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type4, method, path3)
            AnalyseTopicNetwork.analyse_network_a(edge_type5, method, path3)

    ####################################################################################################################

    @staticmethod
    # runs network b
    def run_network_b(time_period, method):

        # variables to hold paths
        path1 = 'topics/current/network-b'
        path2 = 'topics/past/2000-2010/network-b'
        path3 = 'topics/past/1990-2000/network-b'
        # variables to hold edge types
        edge_type1, edge_type2, edge_type3 = 'uw', 'wn', 'wnn'

        # if time period equals to current and method equals to louvain
        if time_period == 'current' and method == 'louvain':

            # analyse network b using louvain
            AnalyseTopicNetwork.analyse_network_b(edge_type1, method, path1)
            AnalyseTopicNetwork.analyse_network_b(edge_type2, method, path1)
            AnalyseTopicNetwork.analyse_network_b(edge_type3, method, path1)

        # if time period equals to current and method equals to spinglass
        if time_period == 'current' and method == 'spinglass':

            # analyse network b using spinglass
            AnalyseTopicNetwork.analyse_network_b(edge_type1, method, path1)
            AnalyseTopicNetwork.analyse_network_b(edge_type2, method, path1)
            AnalyseTopicNetwork.analyse_network_b(edge_type3, method, path1)

        # if time period equals to current and method equals to fastgreedy
        if time_period == 'current' and method == 'fastgreedy':

            # analyse network b using fastgreedy
            AnalyseTopicNetwork.analyse_network_b(edge_type1, method, path1)
            AnalyseTopicNetwork.analyse_network_b(edge_type2, method, path1)
            AnalyseTopicNetwork.analyse_network_b(edge_type3, method, path1)

        ################################################################################################################

        # if time period equals to past1 and method equals to louvain
        if time_period == 'past1' and method == 'louvain':

            # analyse network b using louvain
            AnalyseTopicNetwork.analyse_network_b(edge_type1, method, path2)
            AnalyseTopicNetwork.analyse_network_b(edge_type2, method, path2)
            AnalyseTopicNetwork.analyse_network_b(edge_type3, method, path2)

        # if time period equals to past1 and method equals to spinglass
        if time_period == 'past1' and method == 'spinglass':

            # analyse network b using spinglass
            AnalyseTopicNetwork.analyse_network_b(edge_type1, method, path2)
            AnalyseTopicNetwork.analyse_network_b(edge_type2, method, path2)
            AnalyseTopicNetwork.analyse_network_b(edge_type3, method, path2)

        # if time period equals to past1 and method equals to fastgreedy
        if time_period == 'past1' and method == 'fastgreedy':

            # analyse network b using fastgreedy
            AnalyseTopicNetwork.analyse_network_b(edge_type1, method, path2)
            AnalyseTopicNetwork.analyse_network_b(edge_type2, method, path2)
            AnalyseTopicNetwork.analyse_network_b(edge_type3, method, path2)

        ################################################################################################################

        # if time period equals to past2 and method equals to louvain
        if time_period == 'past2' and method == 'louvain':

            # analyse network b using louvain
            AnalyseTopicNetwork.analyse_network_b(edge_type1, method, path3)
            AnalyseTopicNetwork.analyse_network_b(edge_type2, method, path3)
            AnalyseTopicNetwork.analyse_network_b(edge_type3, method, path3)

        # if time period equals to past2 and method equals to spinglass
        if time_period == 'past2' and method == 'spinglass':

            # analyse network b using spinglass
            AnalyseTopicNetwork.analyse_network_b(edge_type1, method, path3)
            AnalyseTopicNetwork.analyse_network_b(edge_type2, method, path3)
            AnalyseTopicNetwork.analyse_network_b(edge_type3, method, path3)

        # if time period equals to past2 and method equals to fastgreedy
        if time_period == 'past2' and method == 'fastgreedy':

            # analyse network b using fastgreedy
            AnalyseTopicNetwork.analyse_network_b(edge_type1, method, path3)
            AnalyseTopicNetwork.analyse_network_b(edge_type2, method, path3)
            AnalyseTopicNetwork.analyse_network_b(edge_type3, method, path3)

    ####################################################################################################################

    @staticmethod
    # analyses network a
    def analyse_network_a(edge_type, method, path):

        # check folders
        if check_folders(edge_type, method, path) is False:
            # return
            return
        '''
        # variable to hold network
        network = ig.Graph.Read_GraphML('../../data/networks/{}/network/graphml/network.graphml'.format(path))

        # rename columns
        network = na.rename_columns(network)
        # print progress
        # print('> Network columns renamed ({}/{}/{}).'.format(path, edge_type, method))

        # add normalized node number column to network
        network.vs['norm_num'] = na.norm_vals(network.vs['num'], 20, 60)
        # add normalized node value column to network
        network.vs['norm_val'] = na.norm_vals(network.vs['val'], 20, 60)
        # add normalized edge weight column to network
        network.es['norm_weight'] = na.norm_vals(network.es['weight'], 1, 10)
        # add normalized edge value column to network
        network.es['norm_val'] = na.norm_vals(network.es['val'], 1, 10)
        # print progress
        # print('> Network values normalized ({}/{}/{}).'.format(path, edge_type, method))

        # get edge type and print progress
        na.get_edge_type(network, edge_type)
        # print progress
        # print('> Edge type retrieved. ({}/{}/{})'.format(path, edge_type, method))

        # calculate network stats
        na.calc_stats(network, edge_type, method, path)
        # print progress
        # print('> Stats calculated ({}/{}/{}).'.format(path, edge_type, method))

        # calculate modularity
        communities = na.calc_modularity(network, edge_type, method, path, False)
        # print progress
        # print('> Network modularity calculated ({}/{}/{}).'.format(path, edge_type, method))

        # plot network
        na.plot_network(network, edge_type, method, path)
        # print progress
        # print('> Network plotted ({}/{}/{}).'.format(path, edge_type, method))

        # check communities
        if ca.check_communities(communities, edge_type, method, path):
            # return
            return

        # add normalized node membership column to network
        network.vs['membership'] = ca.norm_membership(communities.membership)
        # print progress
        # print('> Network membership normalized ({}/{}/{}).'.format(path, edge_type, method))

        # save communities
        ca.save_communities(network, communities, edge_type, method, path, 0)
        # print progress
        # print('> Communities saved ({}/{}/{}).'.format(path, edge_type, method))

        # save community membership
        ca.save_community_membership(network, edge_type, method, path)
        # print progress
        # print('> Community membership saved ({}/{}/{}).'.format(path, edge_type, method))

        # save community topics and print progress
        ca.save_community_topics(network, edge_type, method, communities, path)
        # print progress
        # print('> Community topics saved ({}/{}/{}).'.format(path, edge_type, method))

        # plot community overview
        ca.plot_community_overview(network, edge_type, method, communities, communities.membership, path, True)
        ca.plot_community_overview(network, edge_type, method, communities, communities.membership, path, False)
        # print progress
        # print('> Community overview plotted ({}/{}/{}).'.format(path, edge_type, method))

        # analyse sub-communities
        analyse_sub_communities(edge_type, method, path, len(glob.glob('../../data/networks/{}/communities/graphml/'
                                                                       '{}/{}/community*'.format(path, edge_type,
                                                                                                 method))) + 1)

        # print progress
        print('> Network, communities and sub-communities analysed ({}/{}/{}).'.format(path, edge_type, method))
        '''
    ####################################################################################################################

    @staticmethod
    # analyses network b
    def analyse_network_b(edge_type, method, path):

        # check folders
        if check_folders(edge_type, method, path) is False:
            # return
            return
        '''
        # variable to hold network
        network = ig.Graph.Read_GraphML('../../data/networks/{}/network/graphml/network.graphml'.format(path))

        # rename columns
        network = na.rename_columns(network)
        # print progress
        # print('> Network columns renamed ({}/{}/{}).'.format(path, edge_type, method))

        # add normalized node number column to network
        network.vs['norm_num'] = na.norm_vals(network.vs['num'], 20, 60)
        # add normalized edge weight column to network
        network.es['norm_weight'] = na.norm_vals(network.es['weight'], 1, 10)
        # print progress
        # print('> Network values normalized ({}/{}/{}).'.format(path, edge_type, method))

        # get edge type and print progress
        na.get_edge_type(network, edge_type)
        # print progress
        # print('> Edge type retrieved. ({}/{}/{})'.format(path, edge_type, method))

        # calculate network stats
        na.calc_stats(network, edge_type, method, path)
        # print progress
        # print('> Stats calculated ({}/{}/{}).'.format(path, edge_type, method))

        # calculate modularity
        communities = na.calc_modularity(network, edge_type, method, path, False)
        # print progress
        # print('> Network modularity calculated ({}/{}/{}).'.format(path, edge_type, method))

        # plot network
        na.plot_network(network, edge_type, method, path)
        # print progress
        # print('> Network plotted ({}/{}/{}).'.format(path, edge_type, method))

        # check communities
        if ca.check_communities(communities, edge_type, method, path):
            # return
            return

        # add normalized node membership column to network
        network.vs['membership'] = ca.norm_membership(communities.membership)
        # print progress
        # print('> Network membership normalized ({}/{}/{}).'.format(path, edge_type, method))

        # save communities
        ca.save_communities(network, communities, edge_type, method, path, 0)
        # print progress
        # print('> Communities saved ({}/{}/{}).'.format(path, edge_type, method))

        # save community membership
        ca.save_community_membership(network, edge_type, method, path)
        # print progress
        # print('> Community membership saved ({}/{}/{}).'.format(path, edge_type, method))

        # save community topics and print progress
        ca.save_community_topics(network, edge_type, method, communities, path)
        # print progress
        # print('> Community topics saved ({}/{}/{}).'.format(path, edge_type, method))

        # plot community overview
        ca.plot_community_overview(network, edge_type, method, communities, communities.membership, path, True)
        ca.plot_community_overview(network, edge_type, method, communities, communities.membership, path, False)
        # print progress
        # print('> Community overview plotted ({}/{}/{}).'.format(path, edge_type, method))

        # analyse sub-communities
        analyse_sub_communities(edge_type, method, path, len(glob.glob('../../data/networks/{}/communities/graphml/'
                                                                       '{}/{}/community*'.format(path, edge_type,
                                                                                                 method))) + 1)

        # print progress
        print('> Network, communities and sub-communities analysed ({}/{}/{}).'.format(path, edge_type, method))
        '''

########################################################################################################################


# AnalyseResearcherNetwork class
class AnalyseResearcherNetwork:

    @staticmethod
    # runs other functions
    def run():

        # variables to hold methods
        method1, method2, method3 = 'louvain', 'spinglass', 'fastgreedy'
        # variables to hold time periods
        time_period1, time_period2, time_period3 = 'current', 'past1', 'past2'

        # run network a
        AnalyseResearcherNetwork.run_network_a(time_period1, method1)
        AnalyseResearcherNetwork.run_network_a(time_period1, method2)
        AnalyseResearcherNetwork.run_network_a(time_period1, method3)

        AnalyseResearcherNetwork.run_network_a(time_period2, method1)
        AnalyseResearcherNetwork.run_network_a(time_period2, method2)
        AnalyseResearcherNetwork.run_network_a(time_period2, method3)

        AnalyseResearcherNetwork.run_network_a(time_period3, method1)
        AnalyseResearcherNetwork.run_network_a(time_period3, method2)
        AnalyseResearcherNetwork.run_network_a(time_period3, method3)

        ################################################################################################################

        # run network b
        AnalyseResearcherNetwork.run_network_b(time_period1, method1)
        AnalyseResearcherNetwork.run_network_b(time_period1, method2)
        AnalyseResearcherNetwork.run_network_b(time_period1, method3)

        AnalyseResearcherNetwork.run_network_b(time_period2, method1)
        AnalyseResearcherNetwork.run_network_b(time_period2, method2)
        AnalyseResearcherNetwork.run_network_b(time_period2, method3)

        AnalyseResearcherNetwork.run_network_b(time_period3, method1)
        AnalyseResearcherNetwork.run_network_b(time_period3, method2)
        AnalyseResearcherNetwork.run_network_b(time_period3, method3)

    ####################################################################################################################

    @staticmethod
    # runs network a
    def run_network_a(time_period, method):

        # variables to hold paths
        path1 = 'researchers/current/network-a'
        path2 = 'researchers/past/2000-2010/network-a'
        path3 = 'researchers/past/1990-2000/network-a'
        # variables to hold edge types
        edge_type1, edge_type2, edge_type3 = 'uw', 'wn', 'wnn'

        # if time period equals to current and method equals to louvain
        if time_period == 'current' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, 20, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, 20, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, 20, path1)

        # if time period equals to current and method equals to spinglass
        if time_period == 'current' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, 20, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, 20, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, 20, path1)

        # if time period equals to current and method equals to fastgreedy
        if time_period == 'current' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, 20, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, 20, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, 20, path1)

        ################################################################################################################

        # if time period equals to past1 and method equals to louvain
        if time_period == 'past1' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, 20, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, 20, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, 20, path2)

        # if time period equals to past1 and method equals to spinglass
        if time_period == 'past1' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, 20, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, 20, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, 20, path2)

        # if time period equals to past1 and method equals to fastgreedy
        if time_period == 'past1' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, 20, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, 20, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, 20, path2)

        ################################################################################################################

        # if time period equals to past2 and method equals to louvain
        if time_period == 'past2' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, 20, path3)

        # if time period equals to past2 and method equals to spinglass
        if time_period == 'past2' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, 20, path3)

        # if time period equals to past2 and method equals to fastgreedy
        if time_period == 'past2' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, 20, path3)

    ####################################################################################################################

    @staticmethod
    # runs network b
    def run_network_b(time_period, method):

        # variables to hold paths
        path1 = 'researchers/current/network-b'
        path2 = 'researchers/past/2000-2010/network-b'
        path3 = 'researchers/past/1990-2000/network-b'
        # variables to hold edge types
        edge_type1, edge_type2, edge_type3, edge_type4, edge_type5 = 'uw', 'wn', 'wv', 'wnn', 'wnv'

        # if time period equals to current and method equals to louvain
        if time_period == 'current' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, 9, path1)

        # if time period equals to current and method equals to spinglass
        if time_period == 'current' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, 9, path1)

        # if time period equals to current and method equals to fastgreedy
        if time_period == 'current' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, 9, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, 9, path1)

        ################################################################################################################

        # if time period equals to past1 and method equals to louvain
        if time_period == 'past1' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, 30, path2)

        # if time period equals to past1 and method equals to spinglass
        if time_period == 'past1' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, 30, path2)

        # if time period equals to past1 and method equals to fastgreedy
        if time_period == 'past1' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, 30, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, 30, path2)

        ################################################################################################################

        # if time period equals to past2 and method equals to louvain
        if time_period == 'past2' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, 20, path3)

        # if time period equals to past2 and method equals to spinglass
        if time_period == 'past2' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, 20, path3)

        # if time period equals to past2 and method equals to fastgreedy
        if time_period == 'past2' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, 20, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, 20, path3)

    ####################################################################################################################

    @staticmethod
    # analyses network a
    def analyse_network_a(edge_type, method, threshold, path):

        # check folders
        if check_folders(edge_type, method, path) is False:
            # return
            return
        '''
        # variable to hold network
        network = ig.Graph.Read_GraphML('../../data/networks/{}/network/graphml/network.graphml'.format(path))

        # rename columns
        network = na.rename_columns(network)
        # print progress
        # print('> Network columns renamed ({}/{}/{}).'.format(path, edge_type, method))

        # add normalized node number column to network
        network.vs['norm_num'] = na.norm_vals(network.vs['num'], 20, 60)
        # add normalized edge weight column to network
        network.es['norm_weight'] = na.norm_vals(network.es['weight'], 1, 10)
        # print progress
        # print('> Network values normalized ({}/{}/{}).'.format(path, edge_type, method))

        # get edge type and print progress
        na.get_edge_type(network, edge_type)
        # print progress
        # print('> Edge type retrieved. ({}/{}/{})'.format(path, edge_type, method))

        # calculate network stats
        na.calc_stats(network, edge_type, method, path)
        # print progress
        # print('> Stats calculated ({}/{}/{}).'.format(path, edge_type, method))

        # calculate modularity
        communities = na.calc_modularity(network, edge_type, method, path, False)
        # print progress
        # print('> Network modularity calculated ({}/{}/{}).'.format(path, edge_type, method))

        # plot network
        na.plot_network(network, edge_type, method, path)
        # print progress
        # print('> Network plotted ({}/{}/{}).'.format(path, edge_type, method))

        # check communities
        if ca.check_communities(communities, edge_type, method, path):
            # return
            return

        # add normalized node membership column to network
        network.vs['membership'] = ca.norm_membership(communities.membership)
        # print progress
        # print('> Network membership normalized ({}/{}/{}).'.format(path, edge_type, method))

        # save communities
        ca.save_communities(network, communities, edge_type, method, path, threshold)
        # print progress
        # print('> Communities saved ({}/{}/{}).'.format(path, edge_type, method))

        # save community membership
        ca.save_community_membership(network, edge_type, method, path)
        # print progress
        # print('> Community membership saved ({}/{}/{}).'.format(path, edge_type, method))

        # save community topics and print progress
        ca.save_community_topics(network, edge_type, method, communities, path)
        # print progress
        # print('> Community topics saved ({}/{}/{}).'.format(path, edge_type, method))

        # plot community overview
        ca.plot_community_overview(network, edge_type, method, communities, communities.membership, path, True)
        ca.plot_community_overview(network, edge_type, method, communities, communities.membership, path, False)
        # print progress
        # print('> Community overview plotted ({}/{}/{}).'.format(path, edge_type, method))

        # analyse sub-communities
        analyse_sub_communities(edge_type, method, path, len(glob.glob('../../data/networks/{}/communities/graphml/'
                                                                       '{}/{}/community*'.format(path, edge_type,
                                                                                                 method))) + 1)

        # print progress
        print('> Network, communities and sub-communities analysed ({}/{}/{}).'.format(path, edge_type, method))
        '''
    ####################################################################################################################

    @staticmethod
    # analyses network b
    def analyse_network_b(edge_type, method, threshold, path):

        # check folders
        if check_folders(edge_type, method, path) is False:
            # return
            return
        '''
        # variable to hold network
        network = ig.Graph.Read_GraphML('../../data/networks/{}/network/graphml/network.graphml'.format(path))

        # rename columns
        network = na.rename_columns(network)
        # print progress
        # print('> Network columns renamed ({}/{}/{}).'.format(path, edge_type, method))

        # add normalized node number column to network
        network.vs['norm_num'] = na.norm_vals(network.vs['num'], 20, 60)
        # add normalized node value column to network
        network.vs['norm_val'] = na.norm_vals(network.vs['val'], 20, 60)
        # add normalized edge weight column to network
        network.es['norm_weight'] = na.norm_vals(network.es['weight'], 1, 10)
        # add normalized edge value column to network
        network.es['norm_val'] = na.norm_vals(network.es['val'], 1, 10)
        # print progress
        # print('> Network values normalized ({}/{}/{}).'.format(path, edge_type, method))

        # get edge type and print progress
        na.get_edge_type(network, edge_type)
        # print progress
        # print('> Edge type retrieved. ({}/{}/{})'.format(path, edge_type, method))

        # calculate network stats
        na.calc_stats(network, edge_type, method, path)
        # print progress
        # print('> Stats calculated ({}/{}/{}).'.format(path, edge_type, method))

        # calculate modularity
        communities = na.calc_modularity(network, edge_type, method, path, False)
        # print progress
        # print('> Network modularity calculated ({}/{}/{}).'.format(path, edge_type, method))

        # plot network
        na.plot_network(network, edge_type, method, path)
        # print progress
        # print('> Network plotted ({}/{}/{}).'.format(path, edge_type, method))

        # check communities
        if ca.check_communities(communities, edge_type, method, path):
            # return
            return

        # add normalized node membership column to network
        network.vs['membership'] = ca.norm_membership(communities.membership)
        # print progress
        # print('> Network membership normalized ({}/{}/{}).'.format(path, edge_type, method))

        # save communities
        ca.save_communities(network, communities, edge_type, method, path, threshold)
        # print progress
        # print('> Communities saved ({}/{}/{}).'.format(path, edge_type, method))

        # save community membership
        ca.save_community_membership(network, edge_type, method, path)
        # print progress
        # print('> Community membership saved ({}/{}/{}).'.format(path, edge_type, method))

        # save community topics and print progress
        ca.save_community_topics(network, edge_type, method, communities, path)
        # print progress
        # print('> Community topics saved ({}/{}/{}).'.format(path, edge_type, method))

        # plot community overview
        ca.plot_community_overview(network, edge_type, method, communities, communities.membership, path, True)
        ca.plot_community_overview(network, edge_type, method, communities, communities.membership, path, False)
        # print progress
        # print('> Community overview plotted ({}/{}/{}).'.format(path, edge_type, method))

        # analyse sub-communities
        analyse_sub_communities(edge_type, method, path, len(glob.glob('../../data/networks/{}/communities/graphml/'
                                                                       '{}/{}/community*'.format(path, edge_type,
                                                                                                 method))) + 1)

        # print progress
        print('> Network, communities and sub-communities analysed ({}/{}/{}).'.format(path, edge_type, method))
        '''


########################################################################################################################


# checks folders
def check_folders(edge_type, method, path):

    # variable to hold clean flag
    clean_flag = True

    # check network stats file
    if glob.glob('../../data/networks/{}/network/txt/'
                 '{}/{}/stats.txt'.format(path, edge_type, method)):
        # print error
        print('\n> File(s) at path: {}/network/txt/'
              '{}/{}/stats.txt, exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check network modularity file
    if glob.glob('../../data/networks/{}/network/txt/'
                 '{}/{}/modularity.txt'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/network/txt/'
              '{}/{}/modularity.txt, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check network plot file
    if glob.glob('../../data/networks/{}/network/png/'
                 '{}/{}/network.png'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/network/png/'
              '{}/{}/network.png, already exist(s).\n'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    ####################################################################################################################

    # check community modularity file
    if glob.glob('../../data/networks/{}/communities/txt/'
                 '{}/{}/modularity.txt'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/communities/txt/'
              '{}/{}/modularity.txt, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check community network files
    if glob.glob('../../data/networks/{}/communities/graphml/'
                 '{}/{}/community*.graphml'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/communities/graphml/'
              '{}/{}/community*.graphml, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check community stats file
    if glob.glob('../../data/networks/{}/communities/txt/'
                 '{}/{}/numbers*.txt'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/communities/txt/'
              '{}/{}/numbers*.txt, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check community membership network file
    if glob.glob('../../data/networks/{}/network/graphml/'
                 '{}/{}/membership*.graphml'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/network/graphml/'
              '{}/{}/membership*.graphml, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check community topics file
    if glob.glob('../../data/networks/{}/communities/txt/'
                 '{}/{}/community_topics*.txt'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/communities/txt/'
              '{}/{}/community_topics*.txt, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check community overview plot file
    if glob.glob('../../data/networks/{}/communities/png/'
                 '{}/{}/overview1*.png'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/communities/png/'
              '{}/{}/overview1.png, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check community overview plot file
    if glob.glob('../../data/networks/{}/communities/png/'
                 '{}/{}/overview2*.png'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/communities/png/'
              '{}/{}/overview2.png, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check communities plot files
    if glob.glob('../../data/networks/{}/communities/png/'
                 '{}/{}/community*.png'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/communities/png/'
              '{}/{}/community*.png, already exist(s).\n'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    ####################################################################################################################

    # check sub-community network files
    if glob.glob('../../data/networks/{}/sub-communities/graphml/'
                 '{}/{}/community*.graphml'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/sub-communities/graphml/'
              '{}/{}/community*.graphml, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check sub-community stats files
    if glob.glob('../../data/networks/{}/sub-communities/txt/'
                 '{}/{}/numbers*.txt'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/sub-communities/txt/'
              '{}/{}/numbers*.txt, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check sub-community membership network files
    if glob.glob('../../data/networks/{}/communities/graphml/'
                 '{}/{}/membership*.graphml'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/communities/graphml/'
              '{}/{}/membership*.graphml, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check sub-community topics files
    if glob.glob('../../data/networks/{}/sub-communities/txt/'
                 '{}/{}/sub_community_topics*.txt'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/sub-communities/txt/'
              '{}/{}/sub_community_topics*.txt, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check sub-community overview plot files
    if glob.glob('../../data/networks/{}/sub-communities/png/'
                 '{}/{}/overview1*.png'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/sub-communities/png/'
              '{}/{}/overview1*.png, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check sub-community overview plot files
    if glob.glob('../../data/networks/{}/sub-communities/png/'
                 '{}/{}/overview2*.png'.format(path, edge_type, method)):
        # print error
        print('> File(s) at path: {}/sub-communities/png/'
              '{}/{}/overview2*.png, already exist(s).'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    ####################################################################################################################

    # if clean flag is false
    if clean_flag is False:
        print('\n######################################################################################################'
              '########################')
        # return clean flag
        return clean_flag
    # if clean flag is true and check equals to 1
    elif clean_flag is True:
        # print progress
        print('\n> Folders checked and found clean ({}/{}/{}).'.format(path, edge_type, method))


########################################################################################################################


# analyses sub-communities
def analyse_sub_communities(edge_type, method, path, length):

    # for i in range between 0 and length of communities
    for i in range(1, length):

        # variable to hold community
        community = ig.Graph.Read_GraphML('../../data/networks/{}/communities/graphml/{}/{}/'
                                          'community{}.graphml'.format(path, edge_type, method, i))

        # rename columns
        community = na.rename_columns(community)
        # print progress
        # print('> Community columns renamed. ({} - {})'.format(edge_type, method))

        # plot communities
        ca.plot_communities(community, edge_type, method, path, i)
        # print progress
        # print('> Communities plotted ({} - {}).'.format(edge_type, method))

        # check community
        if sca.check_sub_communities(community, edge_type, method, path, i):
            # skip iteration
            continue

        # variable to hold sub-communities
        sub_communities = na.calc_modularity(community, edge_type, method, path, i)
        # print progress
        # print('> Community modularity calculated ({} - {}).'.format(edge_type, method))

        # check sub-communities
        if sca.check_sub_communities(sub_communities, edge_type, method, path, i):
            # skip iteration
            continue

        # normalize membership
        community.vs['membership'] = ca.norm_membership(sub_communities.membership)
        # print progress
        # print('> Community membership normalized.'.format(edge_type, method))

        # save sub-communities
        sca.save_sub_communities(community, sub_communities, edge_type, method, path, i)
        # print progress
        # print('> Sub-communities saved ({} - {}).'.format(edge_type, method))

        # save sub-community membership
        sca.save_sub_community_membership(community, edge_type, method, path, i)
        # print progress
        # print('> Sub-community membership saved ({} - {}).'.format(edge_type, method))

        # save sub-community topics
        sca.save_sub_community_topics(community, sub_communities, edge_type, method, path, i)
        # print progress
        # print('> Sub-community topics saved ({} - {}).'.format(edge_type, method))

        # plot sub-community overview
        sca.plot_sub_community_overview(community, sub_communities, sub_communities.membership, edge_type, method,
                                        path, i, True)
        sca.plot_sub_community_overview(community, sub_communities, sub_communities.membership, edge_type, method,
                                        path, i, False)

        # print progress
        # print('> Sub-community overview plotted ({} - {}).'.format(edge_type, method))


########################################################################################################################


# visualises networks in graphistry
def visualise_in_graphistry(network):

    # variable to hold nodes data frame
    nodes_df = pd.DataFrame()

    # add id to nodes data frame
    nodes_df['id'] = [node.index for node in network.vs()]
    # add label to nodes data frame
    nodes_df['label'] = [node for node in network.vs['label']]
    # add num to nodes data frame
    nodes_df['num'] = [int(node_num) for node_num in network.vs['NormNum']]
    # add val to nodes data frame
    nodes_df['val'] = [int(node_val) for node_val in network.vs['NormVal']]
    # add colour to nodes data frame
    nodes_df['colour'] = 7

    # print nodes data frame
    # print(nodes_df)

    # variable to hold edges data frame
    edges_df = pd.DataFrame()

    # add source to edges data frame
    edges_df['source'] = [edge.source for edge in network.es()]
    # add target to edges data frame
    edges_df['target'] = [edge.target for edge in network.es()]
    # add weight to edges data frame
    edges_df['weight'] = [int(edge_weight) for edge_weight in network.es['NormWeight']]
    # add val to edges data frame
    edges_df['val'] = [int(edge_val) for edge_val in network.es['NormVal']]
    # add colour to edges data frame
    edges_df['colour'] = 3

    # print edges data frame
    # print(edges_df)

    # variable to hold network
    network = gp.bind(source='source', destination='target', edge_color='colour', edge_weight='weight')
    # variable to hold network
    network = network.graph(edges_df)
    # variable to hold network nodes
    network_nodes = network.bind(node='id', point_title='label', point_color='colour',
                                 point_size='num').nodes(nodes_df)
    # plot network nodes
    network_nodes.plot()


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
