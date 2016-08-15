#!/usr/bin/env python3

########################################################################################################################

# local python files
import network as na

# third-party library modules
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
    def run(network, time_period):

        # variables to hold time periods
        time_period1, time_period2, time_period3 = 'current', 'past1', 'past2'
        # variables to hold methods
        method1, method2, method3 = 'louvain', 'spinglass', 'fastgreedy'

        # if network equals to a and time period equals to time period 1
        if network == 'a' and time_period == time_period1:

            # run network a
            AnalyseTopicNetwork.run_network_a(time_period1, method1)
            AnalyseTopicNetwork.run_network_a(time_period1, method2)
            AnalyseTopicNetwork.run_network_a(time_period1, method3)

        # if network equals to a and time period equals to time period 2
        if network == 'a' and time_period == time_period2:

            AnalyseTopicNetwork.run_network_a(time_period2, method1)
            AnalyseTopicNetwork.run_network_a(time_period2, method2)
            AnalyseTopicNetwork.run_network_a(time_period2, method3)

        # if network equals to a and time period equals to time period 3
        if network == 'a' and time_period == time_period3:
            AnalyseTopicNetwork.run_network_a(time_period3, method1)
            AnalyseTopicNetwork.run_network_a(time_period3, method2)
            AnalyseTopicNetwork.run_network_a(time_period3, method3)

        ################################################################################################################

        # if network equals to b and time period equals to time period 1
        if network == 'b' and time_period == time_period1:

            # run network b
            AnalyseTopicNetwork.run_network_b(time_period1, method1)
            AnalyseTopicNetwork.run_network_b(time_period1, method2)
            AnalyseTopicNetwork.run_network_b(time_period1, method3)

        # if network equals to b and time period equals to time period 2
        if network == 'b' and time_period == time_period2:

            AnalyseTopicNetwork.run_network_b(time_period2, method1)
            AnalyseTopicNetwork.run_network_b(time_period2, method2)
            AnalyseTopicNetwork.run_network_b(time_period2, method3)

        # if network equals to b and time period equals to time period 3
        if network == 'b' and time_period == time_period3:

            AnalyseTopicNetwork.run_network_b(time_period3, method1)
            AnalyseTopicNetwork.run_network_b(time_period3, method2)
            AnalyseTopicNetwork.run_network_b(time_period3, method3)

    ####################################################################################################################

    @staticmethod
    # runs network a
    def run_network_a(time_period, method):

        # variables to hold edge types
        edge_type1, edge_type2, edge_type3, edge_type4, edge_type5 = 'uw', 'wn', 'wv', 'wnn', 'wnv'
        # variables to hold paths
        path1 = 'topics/current/network-a'
        path2 = 'topics/past/2000-2010/network-a'
        path3 = 'topics/past/1990-2000/network-a'

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

        # variables to hold edge types
        edge_type1, edge_type2, edge_type3 = 'uw', 'wn', 'wnn'
        # variables to hold paths
        path1 = 'topics/current/network-b'
        path2 = 'topics/past/2000-2010/network-b'
        path3 = 'topics/past/1990-2000/network-b'

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

        # analyse network
        na.analyse_network(edge_type, method, 'all', 0, path)

        # print progress
        print('> Network, communities and sub-communities analysed ({}/{}/{}).'.format(path, edge_type, method))

    ####################################################################################################################

    @staticmethod
    # analyses network b
    def analyse_network_b(edge_type, method, path):

        # check folders
        if check_folders(edge_type, method, path) is False:
            # return
            return

        # variable to hold network and communities
        na.analyse_network(edge_type, method, 'half', 0, path)

        # print progress
        print('> Network, communities and sub-communities analysed ({}/{}/{}).'.format(path, edge_type, method))


########################################################################################################################


# AnalyseResearcherNetwork class
class AnalyseResearcherNetwork:

    @staticmethod
    # runs other functions
    def run(network, time_period):

        # variables to hold time periods
        time_period1, time_period2, time_period3 = 'current', 'past1', 'past2'
        # variables to hold methods
        method1, method2, method3 = 'louvain', 'spinglass', 'fastgreedy'

        # if network equals to a and time period equals to time period 1
        if network == 'a' and time_period == time_period1:

            # run network a
            AnalyseResearcherNetwork.run_network_a(time_period1, method1)
            AnalyseResearcherNetwork.run_network_a(time_period1, method2)
            AnalyseResearcherNetwork.run_network_a(time_period1, method3)

        # if network equals to a and time period equals to time period 2
        if network == 'a' and time_period == time_period2:

            AnalyseResearcherNetwork.run_network_a(time_period2, method1)
            AnalyseResearcherNetwork.run_network_a(time_period2, method2)
            AnalyseResearcherNetwork.run_network_a(time_period2, method3)

        # if network equals to a and time period equals to time period 3
        if network == 'a' and time_period == time_period3:

            AnalyseResearcherNetwork.run_network_a(time_period3, method1)
            AnalyseResearcherNetwork.run_network_a(time_period3, method2)
            AnalyseResearcherNetwork.run_network_a(time_period3, method3)

        ################################################################################################################

        # if network equals to b and time period equals to time period 1
        if network == 'b' and time_period == time_period1:

            # run network b
            AnalyseResearcherNetwork.run_network_b(time_period1, method1)
            AnalyseResearcherNetwork.run_network_b(time_period1, method2)
            AnalyseResearcherNetwork.run_network_b(time_period1, method3)

        # if network equals to b and time period equals to time period 2
        if network == 'b' and time_period == time_period2:

            AnalyseResearcherNetwork.run_network_b(time_period2, method1)
            AnalyseResearcherNetwork.run_network_b(time_period2, method2)
            AnalyseResearcherNetwork.run_network_b(time_period2, method3)

        # if network equals to b and time period equals to time period 3
        if network == 'b' and time_period == time_period3:

            AnalyseResearcherNetwork.run_network_b(time_period3, method1)
            AnalyseResearcherNetwork.run_network_b(time_period3, method2)
            AnalyseResearcherNetwork.run_network_b(time_period3, method3)

    ####################################################################################################################

    @staticmethod
    # runs network a
    def run_network_a(time_period, method):

        # variables to hold edge types
        edge_type1, edge_type2, edge_type3 = 'uw', 'wn', 'wnn'
        # variable to hold threshold
        threshold1 = 20
        # variables to hold paths
        path1 = 'researchers/current/network-a'
        path2 = 'researchers/past/2000-2010/network-a'
        path3 = 'researchers/past/1990-2000/network-a'

        # if time period equals to current and method equals to louvain
        if time_period == 'current' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, threshold1, path1)

        # if time period equals to current and method equals to spinglass
        if time_period == 'current' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, threshold1, path1)

        # if time period equals to current and method equals to fastgreedy
        if time_period == 'current' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, threshold1, path1)

        ################################################################################################################

        # if time period equals to past1 and method equals to louvain
        if time_period == 'past1' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, threshold1, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, threshold1, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, threshold1, path2)

        # if time period equals to past1 and method equals to spinglass
        if time_period == 'past1' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, threshold1, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, threshold1, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, threshold1, path2)

        # if time period equals to past1 and method equals to fastgreedy
        if time_period == 'past1' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, threshold1, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, threshold1, path2)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, threshold1, path2)

        ################################################################################################################

        # if time period equals to past2 and method equals to louvain
        if time_period == 'past2' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, threshold1, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, threshold1, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, threshold1, path3)

        # if time period equals to past2 and method equals to spinglass
        if time_period == 'past2' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, threshold1, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, threshold1, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, threshold1, path3)

        # if time period equals to past2 and method equals to fastgreedy
        if time_period == 'past2' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_a(edge_type1, method, threshold1, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type2, method, threshold1, path3)
            AnalyseResearcherNetwork.analyse_network_a(edge_type3, method, threshold1, path3)

    ####################################################################################################################

    @staticmethod
    # runs network b
    def run_network_b(time_period, method):

        # variables to hold edge types
        edge_type1, edge_type2, edge_type3, edge_type4, edge_type5 = 'uw', 'wn', 'wv', 'wnn', 'wnv'
        # variables to hold thresholds
        threshold1, threshold2, threshold3 = 9, 30, 20
        # variables to hold paths
        path1 = 'researchers/current/network-b'
        path2 = 'researchers/past/2000-2010/network-b'
        path3 = 'researchers/past/1990-2000/network-b'

        # if time period equals to current and method equals to louvain
        if time_period == 'current' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, threshold1, path1)

        # if time period equals to current and method equals to spinglass
        if time_period == 'current' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, threshold1, path1)

        # if time period equals to current and method equals to fastgreedy
        if time_period == 'current' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, threshold1, path1)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, threshold1, path1)

        ################################################################################################################

        # if time period equals to past1 and method equals to louvain
        if time_period == 'past1' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, threshold2, path2)

        # if time period equals to past1 and method equals to spinglass
        if time_period == 'past1' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, threshold2, path2)

        # if time period equals to past1 and method equals to fastgreedy
        if time_period == 'past1' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, threshold2, path2)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, threshold2, path2)

        ################################################################################################################

        # if time period equals to past2 and method equals to louvain
        if time_period == 'past2' and method == 'louvain':

            # analyse network a using louvain
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, threshold3, path3)

        # if time period equals to past2 and method equals to spinglass
        if time_period == 'past2' and method == 'spinglass':

            # analyse network a using spinglass
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, threshold3, path3)

        # if time period equals to past2 and method equals to fastgreedy
        if time_period == 'past2' and method == 'fastgreedy':

            # analyse network a using fastgreedy
            AnalyseResearcherNetwork.analyse_network_b(edge_type1, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type2, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type3, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type4, method, threshold3, path3)
            AnalyseResearcherNetwork.analyse_network_b(edge_type5, method, threshold3, path3)

    ####################################################################################################################

    @staticmethod
    # analyses network a
    def analyse_network_a(edge_type, method, threshold, path):

        # check folders
        if check_folders(edge_type, method, path) is False:
            # return
            return

        # variable to hold network and communities
        na.analyse_network(edge_type, method, 'half', threshold, path)

        # print progress
        print('> Network, communities and sub-communities analysed ({}/{}/{}).'.format(path, edge_type, method))

    ####################################################################################################################

    @staticmethod
    # analyses network b
    def analyse_network_b(edge_type, method, threshold, path):

        # check folders
        if check_folders(edge_type, method, path) is False:
            # return
            return

        # variable to hold network and communities
        na.analyse_network(edge_type, method, 'all', threshold, path)

        # print progress
        print('> Network, communities and sub-communities analysed ({}/{}/{}).'.format(path, edge_type, method))


########################################################################################################################


# checks folders
def check_folders(edge_type, method, path):

    # variable to hold clean flag
    clean_flag = True

    # check network graphml folder
    if glob.glob('../../data/networks/{}/network/graphml/'
                 '{}/{}/*'.format(path, edge_type, method)):
        # print error
        print('\n> Folder at path: {}/network/graphml/'
              '{}/{}/, is not empty.'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check network png folder
    if glob.glob('../../data/networks/{}/network/png/'
                 '{}/{}/*'.format(path, edge_type, method)):
        # print error
        print('> Folder at path: {}/network/png/'
              '{}/{}/, is not empty.'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check network txt folder
    if glob.glob('../../data/networks/{}/network/txt/'
                 '{}/{}/*'.format(path, edge_type, method)):
        # print error
        print('> Folder at path: {}/network/txt/'
              '{}/{}/, is not empty.\n'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    ####################################################################################################################

    # check communities graphml folder
    if glob.glob('../../data/networks/{}/communities/graphml/'
                 '{}/{}/*'.format(path, edge_type, method)):
        # print error
        print('> Folder at path: {}/communities/graphml/'
              '{}/{}/, is not empty.'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check communities png folder
    if glob.glob('../../data/networks/{}/communities/png/'
                 '{}/{}/*'.format(path, edge_type, method)):
        # print error
        print('> Folder at path: {}/communities/png/'
              '{}/{}/, is not empty.'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check communities txt folder
    if glob.glob('../../data/networks/{}/communities/txt/'
                 '{}/{}/*'.format(path, edge_type, method)):
        # print error
        print('> Folder at path: {}/communities/txt/'
              '{}/{}/, is not empty.\n'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    ####################################################################################################################

    # check sub-communities graphml folder
    if glob.glob('../../data/networks/{}/sub-communities/graphml/'
                 '{}/{}/*'.format(path, edge_type, method)):
        # print error
        print('> Folder at path: {}/sub-communities/graphml/'
              '{}/{}/, is not empty.'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check sub-communities png folder
    if glob.glob('../../data/networks/{}/sub-communities/png/'
                 '{}/{}/*'.format(path, edge_type, method)):
        # print error
        print('> Folder at path: {}/sub-communities/png/'
              '{}/{}/, is not empty.'.format(path, edge_type, method))
        # set clean flag to false
        clean_flag = False

    # check sub-communities txt folder
    if glob.glob('../../data/networks/{}/sub-communities/txt/'
                 '{}/{}/*'.format(path, edge_type, method)):
        # print error
        print('> Folder at path: {}/sub-communities/txt/'
              '{}/{}/, is not empty.'.format(path, edge_type, method))
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

    # analyse topic network a
    # AnalyseTopicNetwork.run('a', 'current')
    # AnalyseTopicNetwork.run('a', 'past1')
    # AnalyseTopicNetwork.run('a', 'past2')

    # analyse topic network b
    # AnalyseTopicNetwork.run('b', 'current')
    # AnalyseTopicNetwork.run('b', 'past1')
    # AnalyseTopicNetwork.run('b', 'past2')

    # analyse researcher network a
    AnalyseResearcherNetwork.run('a', 'current')
    # AnalyseResearcherNetwork.run('a', 'past1')
    # AnalyseResearcherNetwork.run('a', 'past2')

    # analyse researcher network b
    # AnalyseResearcherNetwork.run('b', 'current')
    # AnalyseResearcherNetwork.run('b', 'past1')
    # AnalyseResearcherNetwork.run('b', 'past2')


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
