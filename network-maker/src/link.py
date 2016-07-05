#!/usr/bin/env python3

########################################################################################################################

# standard library modules
from locale import setlocale, LC_ALL, currency

# third-party library modules
import os
import locale
from copy import deepcopy
from pickle import dump, load
from collections import OrderedDict as dict

########################################################################################################################


# LinkAreas class
class LinkAreas:

    @staticmethod
    # runs other functions
    def run():
        # link areas
        LinkAreas.link_areas()

    ####################################################################################################################

    @staticmethod
    # links areas
    def link_areas():

        # if area links file does not exist
        if not os.path.isfile('../output/areas/links/area_links.csv'):

            # variable to hold input file
            input_file = open(r'../output/areas/info/grant_info.pkl', 'rb')
            # load data structure from file
            grants = load(input_file)
            # close input file
            input_file.close()

            # variable to hold area links list
            area_links = []

            # for area name and grant references in grants dictionary
            for area_name, grant_refs in grants.items():
                # link areas and return the output in area links list
                area_links += LinkAreas.compare_areas(area_name, grant_refs, grants)

            # for area name and grant references in grants dictionary
            for area_name, grant_refs in grants.items():
                # link areas and return the output in area links list
                area_links += LinkAreas.compare_areas(area_name, grant_refs, grants)

            # variable to hold output file
            output_file = open(r'../output/areas/links/area_links.pkl', 'wb')
            # write data structure to file
            dump(area_links, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Linking of areas completed ({} links identified - may include duplicate links)'
                  .format(len(area_links)))

    ####################################################################################################################

    @staticmethod
    # compares areas
    def compare_areas(default_area_name, default_grant_ref, grants):

        # variable to hold copy of grants dictionary
        grants_copy = deepcopy(grants)

        # delete key from grants dictionary
        del grants_copy[default_area_name]

        # variable to hold output file
        output_file = open('../output/areas/links/area_links.csv', 'a')

        # variable to hold area links list
        area_links = []

        # set locale to Great Britain
        locale.setlocale(locale.LC_ALL, 'en_GB.utf8')

        # for area name and grant references in grants dictionary
        for area_name, grant_refs in grants_copy.items():
            # retrieve common grants between two areas
            common_grants = [common_grant_ref for common_grant_ref in default_grant_ref if common_grant_ref in
                             grant_refs]
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

        # close output file
        output_file.close()

        # return area links list
        return area_links

########################################################################################################################


# LinkTopics class
class LinkTopics:

    @staticmethod
    # runs other functions
    def run():

        # extract grant topic information
        LinkTopics.extract_grant_topic_info()
        # link topics
        LinkTopics.link_topics()

    ####################################################################################################################

    @staticmethod
    # extracts grant topic information
    def extract_grant_topic_info():

        # if grant topic information file does not exist
        if not os.path.isfile('../output/topics/info/grants/grant_topic_info.csv'):

            # print progress
            print('> Extraction of grant topic information started')

            # variable to hold input file
            input_file = open(r'../output/topics/info/grants/grant_topics.pkl', 'rb')
            # load data structure from file
            grant_topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold topics
            topics = sorted(set([sub_topic for grant_topic in grant_topics.values() for sub_topic in grant_topic[0]]))

            # variable to hold new topics
            new_topics = dict()

            # for topic in topics
            for topic in topics:
                # variables to hold number and value set to 0
                number, value = 0, 0
                # for grant topic in grant topics
                for grant_topic in grant_topics.values():
                    # for sub topic in grant topic
                    for sub_topic in grant_topic[0]:
                        # if topic is equal to sub topic
                        if topic == sub_topic:
                            # increment number
                            number += 1
                            # add value to value
                            value += grant_topic[1]
                # add topic to new topics
                new_topics[topic] = [number, value]

            # set locale to Great Britain
            setlocale(LC_ALL, 'en_GB.utf8')

            # variable to hold output file
            output_file = open('../output/topics/info/grants/grant_topic_info.csv', mode='w')

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for name and attributes in new topics
            for name, attr in new_topics.items():
                # write name and attributes to file
                output_file.write('"{}","{}","{}"\n'.format(name, attr[0], currency(attr[1], grouping=True)))

                # print progress
                print('> Extraction of grant topic information in progress (information for {} topic(s)'
                      ' extracted)'.format(extraction_count))

                # increment extraction count
                extraction_count += 1

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/info/grants/grant_topic_info.pkl', 'wb')
            # write data structure to file
            dump(new_topics, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of grant topic information completed (information for {} topics'
                  ' extracted)'.format(len(topics)))

    ####################################################################################################################

    @staticmethod
    # links topics
    def link_topics():

        # if area links file does not exist
        if not os.path.isfile('../output/topics/links/topic_links.csv'):

            # print progress
            print('> Extraction of topic links started')

            # variable to hold input file
            input_file = open(r'../output/topics/info/grants/grant_topics.pkl', 'rb')
            # load data structure from file
            grant_topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold grant topics
            grant_topics = [grant_topic for grant_topic in grant_topics.values() if len(grant_topic[0]) > 1]

            # variable to hold topic links
            topic_links = [['|'.join([source, target]), grant_topic[1]] for grant_topic in grant_topics for source in
                           grant_topic[0] for target in grant_topic[0] if source != target]

            # remove reversed topic links
            [topic_links.remove([topic_link[0], topic_link[1]]) for topic_link in topic_links
             if [topic_link[0], topic_link[1]] in topic_links]

            # sort topic links
            topic_links = sorted(topic_links)

            # variable to hold new topic links
            new_topic_links = []

            # for topic link in topic links
            for topic_link in topic_links:
                # variable to hold topics
                topics = topic_link[0].split('|')
                # variable to hold duplicate topic links
                dupe_topic_links = [x for x in topic_links if x[0] == topic_link[0]]
                # variable to hold number and value
                number, value = len(dupe_topic_links), 0
                # for duplicate topic link in duplicate topic links
                for dupe_topic_link in dupe_topic_links:
                    # add value to value
                    value += dupe_topic_link[1]
                    # remove topic link
                    topic_links.remove(dupe_topic_link)
                # add topic link to new topic links
                new_topic_links += [[topics[0], topics[1], number, value]]

            # set locale to Great Britain
            setlocale(LC_ALL, 'en_GB.utf8')

            # variable to hold output file
            output_file = open('../output/topics/links/topic_links.csv', mode='w')

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for new topic link in new topic links
            for new_topic_link in new_topic_links:
                # write new topic link to file
                output_file.write('"{}","{}","{}","{}"\n'.format(new_topic_link[0], new_topic_link[1],
                                                                 new_topic_link[2], currency(new_topic_link[3],
                                                                                             grouping=True)))

                # print progress
                print('> Extraction of topic links in progress ({} topic link(s) extracted)'.format(extraction_count))

                # increment extraction count
                extraction_count += 1

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/links/topic_links.pkl', 'wb')
            # write data structure to file
            dump(new_topic_links, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of topic links completed ({} topic links extracted)'.format(len(new_topic_links)))

########################################################################################################################


# main function
def main():

    # link areas
    LinkAreas.run()

    # link topics
    LinkTopics.run()


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
