#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
import os
from pickle import load
from collections import OrderedDict

########################################################################################################################


# CreateNetwork class
class CreateNetwork:

    @staticmethod
    # runs other functions
    def run():

        # create area network in gephi format
        CreateNetwork.create_area_network('gephi')
        # create area network in graphistry format
        CreateNetwork.create_area_network('graphistry')

        # create topic network a
        CreateNetwork.create_topic_network_a()
        # create topic network b
        CreateNetwork.create_topic_network_b()

        # create researcher network a
        CreateNetwork.create_researcher_network_a()
        # create researcher network b
        CreateNetwork.create_researcher_network_b()

    ####################################################################################################################

    # creates area network
    @staticmethod
    def create_area_network(tool):

        # if area nodes in gephi format or edges in graphistry format file does not exist
        if not (os.path.isfile('../../data/networks/areas/nodes_gephi.tsv') and
                os.path.isfile('../../data/networks/areas/edges_graphistry.tsv')):

            # variable to hold input file
            input_file = open(r'../output/areas/info/area_info.pkl', 'rb')
            # load data structure from file
            areas = load(input_file)
            # close input file
            input_file.close()

            # variable to hold input file
            input_file = open(r'../output/areas/links/area_links.pkl', 'rb')
            # load data structure from file
            area_links = load(input_file)
            # close input file
            input_file.close()

            # for area link in area links list
            for area_link in area_links:
                # variable to hold area link swap
                area_link_swap = (area_link[1], area_link[0], area_link[2], area_link[3])
                # remove area link swap from area links list
                area_links.remove(area_link_swap)

            # variable to hold area ids dictionary
            area_ids = OrderedDict()
            # variable to hold identifier set to 1
            identifier = 1
            # for area name in areas dictionary
            for area_name in areas.keys():
                # add identifier to areas ids dictionary
                area_ids[area_name] = identifier
                # increment identifier
                identifier += 1

            # if tool equals to gephi
            if tool == 'gephi':

                # open file
                with open('../../data/networks/areas/nodes_gephi.tsv', 'w') as output_file:
                    # write headers to file
                    output_file.write('Id\tLabel\tGrantNum\tPropVal\tGrantVal\n')
                    # for area name and id in areas ids dictionary
                    for area_name, area_id in area_ids.items():
                        # variable to hold area grant number
                        area_grant_num = areas.get(area_name)[1]
                        # variable to hold area proportional value
                        area_prop_val = areas.get(area_name)[2]
                        # variable to hold area grant value
                        area_grant_val = areas.get(area_name)[3]
                        # write area to file
                        output_file.write('{}\t{}\t{}\t{}\t{}\n'.format(area_id, area_name, area_grant_num,
                                                                        area_prop_val, area_grant_val))

                # variable to hold output file
                with open('../../data/networks/areas/edges_gephi.tsv', 'w') as output_file:
                    # write headers to file
                    output_file.write('Source\tTarget\tType\tWeight\tTotalVal\n')
                    # for area link in area links dictionary
                    for area_link in area_links:
                        # variable to hold first area name
                        area_name_1st = area_link[0]
                        # variable to hold first area id
                        area_id_1st = area_ids.get(area_name_1st)
                        # variable to hold second area name
                        area_name_2nd = area_link[1]
                        # variable to hold second area id
                        area_id_2nd = area_ids.get(area_name_2nd)
                        # write area link to file
                        output_file.write('{}\t{}\t{}\t{:.1f}\t{}\n'.format(area_id_1st, area_id_2nd, 'Undirected',
                                                                            area_link[2], area_link[3]))

                # print progress
                print('> Creation of Area Network in Gephi format completed')

            # if tool equals to graphistry
            elif tool == 'graphistry':
                # variable to hold output file
                with open('../../data/networks/areas/edges_graphistry.tsv', 'w') as output_file:
                    # write headers to file
                    output_file.write('source\ttarget\tvalue\n')
                    # for area link in area links dictionary
                    for area_link in area_links:
                        # write area link to file
                        output_file.write('{}\t{}\t{}\n'.format(area_link[0], area_link[1], area_link[2]))

                # print progress
                print('> Creation of Area Network in Graphistry format completed')

    ####################################################################################################################

    @staticmethod
    # creates topic network a
    def create_topic_network_a():

        # if  file does not exist
        if not os.path.isfile('../../data/networks/topics/nodes_gephi.tsv'):

            # variable to hold input file
            input_file = open(r'../output/topics/info/grants/grant_topic_info.pkl', 'rb')
            # load data structure from file
            topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold input file
            input_file = open(r'../output/topics/links/topic_links.pkl', 'rb')
            # load data structure from file
            topic_links = load(input_file)
            # close input file
            input_file.close()

            # variable to hold topic ids
            topic_ids = OrderedDict()
            # variable to hold identifier set to 1
            identifier = 1
            # for topic name in topics
            for topic_name in topics.keys():
                # add identifier to topic ids
                topic_ids[topic_name] = identifier
                # increment identifier
                identifier += 1

            # variable to hold output file
            output_file = open('../../data/networks/topics/nodes_gephi.tsv', 'w')
            # write headers to file
            output_file.write('Id\tLabel\tNum\t\tVal\n')
            # for topic name and id in topic ids
            for topic_name, topic_id in topic_ids.items():
                # variable to hold topic number
                topic_num = topics.get(topic_name)[0]
                # variable to hold topic value
                topic_val = topics.get(topic_name)[1]
                # write topic to file
                output_file.write('{}\t{}\t{}\t{}\t\n'.format(topic_id, topic_name, topic_num, topic_val))

            # variable to hold output file
            output_file = open('../../data/networks/topics/edges_gephi.tsv', 'w')
            # write headers to file
            output_file.write('Source\tTarget\tType\tWeight\tVal\n')
            # for topic link in topic links
            for topic_link in topic_links:
                # variable to hold source
                source = topic_link[0]
                # variable to hold source id
                source_id = topic_ids.get(source)
                # variable to hold target
                target = topic_link[1]
                # variable to hold target id
                target_id = topic_ids.get(target)
                # write topic link to file
                output_file.write('{}\t{}\t{}\t{:.1f}\t{}\n'.format(source_id, target_id, 'Undirected',
                                                                    topic_link[2], topic_link[3]))

            # print progress
            print('> Creation of Topic Network A in Gephi format completed')

    ####################################################################################################################

    @staticmethod
    # creates topic network b
    def create_topic_network_b():
        pass

    ####################################################################################################################

    @staticmethod
    # creates researcher network a
    def create_researcher_network_a():
        pass

    ####################################################################################################################

    @staticmethod
    # creates researcher network b
    def create_researcher_network_b():
        pass


########################################################################################################################


# main function
def main():

    # create network
    CreateNetwork.run()


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
