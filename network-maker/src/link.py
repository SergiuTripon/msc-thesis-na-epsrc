#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
import locale
from copy import deepcopy
from pickle import dump, load

########################################################################################################################


# links areas
def link_areas():

    # variable to hold input file
    input_file = open(r'../output/areas/grants.pkl', 'rb')
    # load data structure from file
    grants = load(input_file)
    # close input file
    input_file.close()

    # variable to hold area links list
    area_links = []

    # for area name and grant references in grants dictionary
    for area_name, grant_refs in grants.items():
        # link areas and return the output in area links list
        area_links += compare_areas(area_name, grant_refs, grants)

    # for area name and grant references in grants dictionary
    for area_name, grant_refs in grants.items():
        # link areas and return the output in area links list
        area_links += compare_areas(area_name, grant_refs, grants)

    # variable to hold output file
    output_file = open(r'../output/areas/area_links.pkl', 'wb')
    # write data structure to file
    dump(area_links, output_file)
    # close output file
    output_file.close()

    # print progress
    print('> Linking of areas completed ({} links identified - may include duplicate links)'.format(len(area_links)))


########################################################################################################################


# compares areas
def compare_areas(default_area_name, default_grant_ref, grants):

    # variable to hold copy of grants dictionary
    grants_copy = deepcopy(grants)

    # delete key from grants dictionary
    del grants_copy[default_area_name]

    # variable to hold output file
    output_file = open('../output/areas/area_links.csv', 'a')

    # variable to hold area links list
    area_links = []

    # set locale to Great Britain
    locale.setlocale(locale.LC_ALL, 'en_GB.utf8')

    # for area name and grant references in grants dictionary
    for area_name, grant_refs in grants_copy.items():
        # retrieve common grants between two areas
        common_grants = [common_grant_ref for common_grant_ref in default_grant_ref if common_grant_ref in grant_refs]
        # if common grants exist
        if common_grants:
            # variable to hold value of common grants
            common_grants_val = 0
            # for common grant in common grants
            for common_grant in common_grants:
                # add common grants values to value of common grants
                common_grants_val += common_grant[1]
            # write area links, number of links and value of common grants to file
            output_file.write('"{}","{}","{}","{}"\n'.format(default_area_name, area_name, len(common_grants),
                                                             locale.currency(common_grants_val, grouping=True)))
            # add area links, number of links, and value of common grants to area links list
            area_links += [(default_area_name, area_name, len(common_grants), common_grants_val)]

    # return area links list
    return area_links


########################################################################################################################


# main function
def main():

    # link areas
    link_areas()


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
