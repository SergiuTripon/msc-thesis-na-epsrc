#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
from pickle import load
from collections import OrderedDict

########################################################################################################################


# creates network
def create_network(areas, area_links, tool):

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

    # if tool is gephi
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
                output_file.write('{}\t{}\t{}\t{}\t{}\n'.format(area_id, area_name, area_grant_num, area_prop_val,
                                                                area_grant_val))

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
                output_file.write('{}\t{}\t{}\t{}\t{}\n'.format(area_id_1st, area_id_2nd, 'Undirected', area_link[2],
                                                                area_link[3]))

    # if tool is graphistry
    elif tool == 'graphistry':

        # variable to hold output file
        with open('../../data/networks/areas/edges_graphistry.tsv', 'w') as output_file:
            # write headers to file
            output_file.write('source\ttarget\tvalue\n')
            # for area link in area links dictionary
            for area_link in area_links:
                # write area link to file
                output_file.write('{}\t{}\t{}\n'.format(area_link[0], area_link[1], area_link[2]))


########################################################################################################################


# main function
def main():

    # variable to hold areas input file
    areas_file = open(r'../output/areas/areas.pkl', 'rb')
    # load data structure from file
    areas = load(areas_file)
    # close areas input file
    areas_file.close()

    # variable to hold area links input file
    area_links_file = open(r'../output/areas/area_links.pkl', 'rb')
    # load data structure from file
    area_links = load(area_links_file)
    # close area links input file
    area_links_file.close()

    tool = 'gephi'
    # tool = 'graphistry'

    # create network
    create_network(areas, area_links, tool)

    # print progress
    print('> Creation of Gephi Network completed')


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
