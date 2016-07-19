#!/usr/bin/env python3

########################################################################################################################

# standard library modules
from locale import setlocale, LC_ALL, currency

# third-party library modules
import os
import locale
from copy import deepcopy
from pickle import dump, load
from collections import OrderedDict

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
        if not os.path.isfile('../output/areas/current/links/area_links.csv'):

            # variable to hold input file
            input_file = open(r'../output/areas/current/info/area_grants.pkl', 'rb')
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

            # variable to hold output file
            output_file = open(r'../output/areas/current/links/area_links.pkl', 'wb')
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
        output_file = open('../output/areas/current/links/area_links.csv', 'a')

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
        LinkTopics.extract_grant_topic_info('current')
        LinkTopics.extract_grant_topic_info('past/2000-2010')
        LinkTopics.extract_grant_topic_info('past/1990-2000')

        # extract researcher topic information
        LinkTopics.extract_researcher_topic_info('current')
        LinkTopics.extract_researcher_topic_info('past/2000-2010')
        LinkTopics.extract_researcher_topic_info('past/1990-2000')

        # link grant topics
        LinkTopics.link_grant_topics('current')
        LinkTopics.link_grant_topics('past/2000-2010')
        LinkTopics.link_grant_topics('past/1990-2000')

        # link researcher topics
        LinkTopics.link_researcher_topics('current')
        LinkTopics.link_researcher_topics('past/2000-2010')
        LinkTopics.link_researcher_topics('past/1990-2000')

    ####################################################################################################################

    @staticmethod
    # extracts grant topic information
    def extract_grant_topic_info(path):

        # if grant topic information file does not exist
        if not os.path.isfile('../output/topics/{}/info/grant_topic_info.csv'.format(path)):

            # print progress
            print('> Extraction of grant topic information ({}) started'.format(path))

            # variable to hold input file
            input_file = open(r'../output/grants/{}/info/grant_topics.pkl'.format(path), 'rb')
            # load data structure from file
            grant_topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold topics
            topics = sorted(set([sub_topic for grant_topic in grant_topics.values() for sub_topic in grant_topic[0]
                                 if len(grant_topic[0]) > 1]))

            # variable to hold new topics
            new_topics = OrderedDict()

            # for topic in topics
            for topic in topics:
                # variables to hold number and value set to 0
                number, value = 0, 0
                # for grant topic in grant topics
                for grant_topic in grant_topics.values():
                    # if topic in grant topic
                    if topic in grant_topic[0]:
                        # increment number
                        number += 1
                        # add value to value
                        value += grant_topic[1]
                # add topic to new topics
                new_topics[topic] = [number, value]

            # set locale to Great Britain
            setlocale(LC_ALL, 'en_GB.utf8')

            # variable to hold output file
            output_file = open('../output/topics/{}/info/grant_topic_info.csv'.format(path), mode='w')

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for name and attributes in new topics
            for name, attr in new_topics.items():
                # write name and attributes to file
                output_file.write('"{}","{}","{}"\n'.format(name, attr[0], currency(attr[1], grouping=True)))

                # print progress
                print('> Extraction of grant topic information ({}) in progress (information for {} topic(s)'
                      ' extracted)'.format(path, extraction_count))

                # increment extraction count
                extraction_count += 1

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/{}/info/grant_topic_info.pkl'.format(path), 'wb')
            # write data structure to file
            dump(new_topics, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of grant topic information ({}) completed (information for {} topics'
                  ' extracted)'.format(path, len(new_topics)))

    ####################################################################################################################

    @staticmethod
    # extracts researcher topic information
    def extract_researcher_topic_info(path):

        # if researcher topic information file does not exist
        if not os.path.isfile('../output/topics/{}/info/researcher_topic_info.csv'.format(path)):

            # print progress
            print('> Extraction of researcher topic information ({}) started'.format(path))

            # variable to hold input file
            input_file = open(r'../output/researchers/{}/info/researcher_topics.pkl'.format(path), 'rb')
            # load data structure from file
            researcher_topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold topics
            topics = sorted(set([sub_topic for researcher_topic in researcher_topics.values() for sub_topic in
                                 researcher_topic[1] if len(researcher_topic[1]) > 1]))

            # variable to hold new topics
            new_topics = OrderedDict()

            # for topic in topics
            for topic in topics:
                # variables to hold number set to 0
                number = 0
                # for researcher topic in researcher topics
                for researcher_topic in researcher_topics.values():
                    # if topic in researcher topic
                    if topic in researcher_topic[1]:
                        # increment number
                        number += 1
                # add new topic to new topics
                new_topics[topic] = number

            # variable to hold output file
            output_file = open('../output/topics/{}/info/researcher_topic_info.csv'.format(path), mode='w')

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for name and number in new topics
            for name, number in new_topics.items():
                # write name and number to file
                output_file.write('"{}","{}"\n'.format(name, number))

                # print progress
                print('> Extraction of researcher topic information ({}) in progress (information for {} topic(s)'
                      ' extracted)'.format(path, extraction_count))

                # increment extraction count
                extraction_count += 1

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/{}/info/researcher_topic_info.pkl'.format(path), 'wb')
            # write data structure to file
            dump(new_topics, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of researcher topic information ({}) completed (information for {} topics'
                  ' extracted)'.format(path, len(new_topics)))

    ####################################################################################################################

    @staticmethod
    # links topics
    def link_grant_topics(path):

        # if grant topic links file does not exist
        if not os.path.isfile('../output/topics/{}/links/grant_topic_links.csv'.format(path)):

            # print progress
            print('> Extraction of grant topic links ({}) started'.format(path))

            # variable to hold input file
            input_file = open(r'../output/grants/{}/info/grant_topics.pkl'.format(path), 'rb')
            # load data structure from file
            grant_topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold grant topics
            grant_topics = [grant_topic for grant_topic in grant_topics.values() if len(grant_topic[0]) > 1]

            # variable to hold topic links
            topic_links = [[source, target, grant_topic[1]] for grant_topic in grant_topics for source in
                           grant_topic[0] for target in grant_topic[0] if source != target]

            # remove reversed topic links
            [topic_links.remove([topic_link[1], topic_link[0], topic_link[2]]) for topic_link in topic_links
             if [topic_link[1], topic_link[0], topic_link[2]] in topic_links]

            # variable to hold new topic links
            new_topic_links = []

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for topic link in topic links
            for topic_link in topic_links:
                # variable to hold duplicate topic links
                dupe_topic_links = [x for x in topic_links if (x[0], x[1]) == (topic_link[0], topic_link[1])]
                # variable to hold number and value
                number, value = len(dupe_topic_links), 0
                # for duplicate topic link in duplicate topic links
                for dupe_topic_link in dupe_topic_links:
                    # add value to value
                    value += dupe_topic_link[2]
                # variable to hold new topic link
                new_topic_link = [topic_link[0], topic_link[1], number, value]
                # if new topic link is not in new topic links
                if new_topic_link not in new_topic_links:
                    # add new topic link to new topic links
                    new_topic_links += [new_topic_link]

                    # print progress
                    print('> Extraction of grant topic links ({}) in progress ({} grant topic link(s)'
                          ' extracted)'.format(path, extraction_count))

                    # increment extraction count
                    extraction_count += 1

            # set locale to Great Britain
            setlocale(LC_ALL, 'en_GB.utf8')

            # variable to hold output file
            output_file = open('../output/topics/{}/links/grant_topic_links.csv'.format(path), mode='w')

            # for new topic link in new topic links
            for new_topic_link in new_topic_links:
                # write new topic link to file
                output_file.write('"{}","{}","{}","{}"\n'.format(new_topic_link[0], new_topic_link[1],
                                                                 new_topic_link[2], currency(new_topic_link[3],
                                                                                             grouping=True)))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/{}/links/grant_topic_links.pkl'.format(path), 'wb')
            # write data structure to file
            dump(new_topic_links, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of grant topic links ({}) completed ({} grant topic links'
                  ' extracted)'.format(path, len(new_topic_links)))

    ####################################################################################################################

    @staticmethod
    # links researcher topics
    def link_researcher_topics(path):

        # if researcher topic links file does not exist
        if not os.path.isfile('../output/topics/{}/links/researcher_topic_links.csv'.format(path)):

            # print progress
            print('> Extraction of researcher topic links ({}) started'.format(path))

            # variable to hold input file
            input_file = open(r'../output/researchers/{}/info/researcher_topics.pkl'.format(path), 'rb')
            # load data structure from file
            researcher_topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold researcher topics
            researcher_topics = [researcher_topic[1] for researcher_topic in researcher_topics.values()
                                 if len(researcher_topic[1]) > 1]

            # variable to hold topic links
            topic_links = [[source, target] for researcher_topic in researcher_topics for source in researcher_topic
                           for target in researcher_topic if source != target]

            # remove reversed topic links
            [topic_links.remove([topic_link[1], topic_link[0]]) for topic_link in topic_links
             if [topic_link[1], topic_link[0]] in topic_links]

            # variable to hold new topic links
            new_topic_links = []

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for topic link in topic links
            for topic_link in topic_links:
                # variable to hold duplicate topic links
                dupe_topic_links = [x for x in topic_links if (x[0], x[1]) == (topic_link[0], topic_link[1])]
                # variable to hold number
                number = len(dupe_topic_links)
                # variable to hold new topic link
                new_topic_link = [topic_link[0], topic_link[1], number]
                # if new topic link is not in new topic links
                if new_topic_link not in new_topic_links:
                    # add new topic link to new topic links
                    new_topic_links += [new_topic_link]

                    # print progress
                    print('> Extraction of researcher topic links ({}) in progress ({} researcher topic link(s)'
                          ' extracted)'.format(path, extraction_count))

                    # increment extraction count
                    extraction_count += 1

            # variable to hold output file
            output_file = open('../output/topics/{}/links/researcher_topic_links.csv'.format(path), mode='w')

            # for new topic link in new topic links
            for new_topic_link in new_topic_links:
                # write new topic link to file
                output_file.write('"{}","{}","{}"\n'.format(new_topic_link[0], new_topic_link[1],
                                                            new_topic_link[2]))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/{}/links/researcher_topic_links.pkl'.format(path), 'wb')
            # write data structure to file
            dump(new_topic_links, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of researcher topic links ({}) completed ({} researcher topic links'
                  ' extracted)'.format(path, len(new_topic_links)))


########################################################################################################################


# LinkResearchers class
class LinkResearchers:

    @staticmethod
    # runs other functions
    def run():

        # extract researcher info
        LinkResearchers.extract_researcher_info('current')
        LinkResearchers.extract_researcher_info('past/2000-2010')
        LinkResearchers.extract_researcher_info('past/1990-2000')

        # extract grant researcher info
        LinkResearchers.extract_grant_researcher_info('current')
        LinkResearchers.extract_grant_researcher_info('past/2000-2010')
        LinkResearchers.extract_grant_researcher_info('past/1990-2000')

        # link researchers
        LinkResearchers.link_researchers('current')
        LinkResearchers.link_researchers('past/2000-2010')
        LinkResearchers.link_researchers('past/1990-2000')

        # link grant researchers
        LinkResearchers.link_grant_researchers('current')
        LinkResearchers.link_grant_researchers('past/2000-2010')
        LinkResearchers.link_grant_researchers('past/1990-2000')

    ####################################################################################################################

    @staticmethod
    # extracts researcher info
    def extract_researcher_info(path):

        # if researcher information file does not exist
        if not os.path.isfile('../output/researchers/{}/info/researcher_info.csv'.format(path)):

            # print progress
            print('> Extraction of researcher information ({}) started'.format(path))

            # variable to hold input file
            input_file = open(r'../output/researchers/{}/info/researcher_topics.pkl'.format(path), 'rb')
            # load data structure from file
            researcher_topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold researchers
            researchers = OrderedDict((identifier, [attr[0], len(attr[1])]) for identifier, attr in
                                      researcher_topics.items() if attr[0] and len(attr[1]) > 0)

            # variable to hold output file
            output_file = open('../output/researchers/{}/info/researcher_info.csv'.format(path), mode='w')

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for researcher in researchers
            for identifier, attr in researchers.items():
                # write identifier and attributes to file
                output_file.write('"{}","{}","{}"\n'.format(identifier, attr[0], attr[1]))

                # print progress
                print('> Extraction of researcher information ({}) in progress (information for {} researcher(s)'
                      ' extracted)'.format(path, extraction_count))

                # increment extraction count
                extraction_count += 1

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/researchers/{}/info/researcher_info.pkl'.format(path), 'wb')
            # write data structure to file
            dump(researchers, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of researcher information ({}) completed (information for {} researchers'
                  ' extracted)'.format(path, len(researchers)))

    ####################################################################################################################

    @staticmethod
    # extracts grant researcher info
    def extract_grant_researcher_info(path):

        # if grant researcher information file does not exist
        if not os.path.isfile('../output/researchers/{}/info/grant_researcher_info.csv'.format(path)):

            # print progress
            print('> Extraction of grant researcher information ({}) started'.format(path))

            # variable to hold input file
            input_file = open(r'../output/grants/{}/info/grant_researchers.pkl'.format(path), 'rb')
            # load data structure from file
            grant_researchers = load(input_file)
            # close input file
            input_file.close()

            # variable to hold researchers
            researchers = set([(sub_researcher[0], sub_researcher[1]) for grant_researcher in
                               grant_researchers.values() for sub_researcher in grant_researcher[0]
                               if len(grant_researcher[0]) > 1])

            # variable to hold new researchers
            new_researchers = OrderedDict()

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for researcher in researchers
            for researcher in researchers:
                # variables to hold number and value set to 0
                number, value = 0, 0
                # for grant researcher in grant researchers
                for grant_researcher in grant_researchers.values():
                    # for sub researcher in grant researcher
                    for sub_researcher in grant_researcher[0]:
                        # if researcher in sub researcher
                        if researcher[1] in sub_researcher:
                            # increment number
                            number += 1
                            # add value to value
                            value += grant_researcher[1]
                # add researcher to new researchers
                new_researchers[researcher[1]] = [researcher[0], number, value]

                # print progress
                print('> Extraction of grant researcher information ({}) in progress (information for {} researcher(s)'
                      ' extracted)'.format(path, extraction_count))

                # increment extraction count
                extraction_count += 1

            # variable to hold output file
            output_file = open('../output/researchers/{}/info/grant_researcher_info.csv'.format(path), mode='w')

            # set locale to Great Britain
            setlocale(LC_ALL, 'en_GB.utf8')

            # for identifier and attributes in new topics
            for identifier, attr in new_researchers.items():
                # write identifier and attributes to file
                output_file.write('"{}","{}","{}","{}"\n'.format(identifier, attr[0], attr[1],
                                                                 currency(attr[2], grouping=True)))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/researchers/{}/info/grant_researcher_info.pkl'.format(path), 'wb')
            # write data structure to file
            dump(new_researchers, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of grant researcher information ({}) completed (information for {} researchers'
                  ' extracted)'.format(path, len(new_researchers)))

    ####################################################################################################################

    @staticmethod
    # links researchers
    def link_researchers(path):

        # if researcher links file does not exist
        if not os.path.isfile('../output/researchers/{}/links/researcher_links.csv'.format(path)):

            # print progress
            print('> Extraction of researcher links ({}) started'.format(path))

            # variable to hold input file
            input_file = open(r'../output/researchers/{}/info/researcher_topics.pkl'.format(path), 'rb')
            # load data structure from file
            researcher_topics = load(input_file)
            # close input file
            input_file.close()

            # variable to hold researcher links
            researcher_links = []

            # variable to hold copy of researcher topics copy
            researcher_topics_copy = deepcopy(researcher_topics)

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for researcher topic in researcher topics
            for researcher_topic in researcher_topics.items():
                # delete key from researcher topics copy
                del researcher_topics_copy[researcher_topic[0]]
                # add researcher link to researcher links
                researcher_links += LinkResearchers.compare_researchers(researcher_topic, researcher_topics_copy)

                # print progress
                print('> Extraction of researcher links ({}) in progress (researcher links for {} researchers(s)'
                      ' extracted)'.format(path, extraction_count))

                # increment extraction count
                extraction_count += 1

            # variable to hold output file
            output_file = open('../output/researchers/{}/links/researcher_links.csv'.format(path), mode='w')

            # for researcher link in researcher links
            for researcher_link in researcher_links:
                # write researcher link to file
                output_file.write('"{}","{}","{}"\n'.format(researcher_link[0], researcher_link[1],
                                                            researcher_link[2]))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/researchers/{}/links/researcher_links.pkl'.format(path), 'wb')
            # write data structure to file
            dump(researcher_links, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of researcher links ({}) completed ({} researcher links'
                  ' extracted)'.format(path, len(researcher_links)))

    ####################################################################################################################

    @staticmethod
    # compares researchers
    def compare_researchers(default_researcher_topic, researcher_topics_copy):

        # variable to hold researcher links
        researcher_links = []

        # for researcher topic copy in researcher topics copy
        for researcher_topic_copy in researcher_topics_copy.items():
            # variable to hold common topics
            common_topics = [common_topic for common_topic in default_researcher_topic[1][1] if common_topic in
                             researcher_topic_copy[1][1]]
            # if common topics exist
            if common_topics:
                # add research link to researcher links
                researcher_links += [[default_researcher_topic[0], researcher_topic_copy[0], len(common_topics)]]

        # return researcher links
        return researcher_links

    ####################################################################################################################

    @staticmethod
    # links grant researchers
    def link_grant_researchers(path):

        # if grant researcher links file does not exist
        if not os.path.isfile('../output/researchers/{}/links/grant_researcher_links.csv'.format(path)):

            # print progress
            print('> Extraction of grant researcher links ({}) started'.format(path))

            # variable to hold input file
            input_file = open(r'../output/grants/{}/info/grant_researchers.pkl'.format(path), 'rb')
            # load data structure from file
            grant_researchers = load(input_file)
            # close input file
            input_file.close()

            # variable to hold grant researchers
            grant_researchers = [[[sub_researcher[1] for sub_researcher in grant_researcher[0]], grant_researcher[1]]
                                 for grant_researcher in grant_researchers.values() if len(grant_researcher) > 1]

            # variable to hold researcher links
            researcher_links = [[source, target, grant_researcher[1]] for grant_researcher in grant_researchers
                                for source in grant_researcher[0] for target in grant_researcher[0] if source != target]

            # remove reversed researcher links
            [researcher_links.remove([researcher_link[1], researcher_link[0], researcher_link[2]]) for researcher_link
             in researcher_links if [researcher_link[1], researcher_link[0], researcher_link[2]] in researcher_links]

            # variable to hold new researcher links
            new_researcher_links = []

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for researcher link in researcher links
            for researcher_link in researcher_links:
                # variable to hold duplicate researcher links
                dupe_researcher_links = [x for x in researcher_links
                                         if [x[0], x[1]] == [researcher_link[0], researcher_link[1]] or
                                         [x[0], x[1]] == [researcher_link[1], researcher_link[0]]]
                # variable to hold number and value
                number, value = len(dupe_researcher_links), sum(x[2] for x in dupe_researcher_links)
                # variable to hold new researcher link
                new_researcher_link = [researcher_link[0], researcher_link[1], number, value]
                # if new researcher link and reversed new researcher link not in new researcher links
                if new_researcher_link not in new_researcher_links:
                    # add new researcher link to new researcher links
                    new_researcher_links += [new_researcher_link]

                    # print progress
                    print('> Extraction of grant researcher links ({}) in progress ({} grant researcher link(s)'
                          ' extracted)'.format(path, extraction_count))

                    # increment extraction count
                    extraction_count += 1

            # remove reversed new researcher links
            [new_researcher_links.remove([new_researcher_link[1], new_researcher_link[0], new_researcher_link[2],
                                          new_researcher_link[3]]) for new_researcher_link in new_researcher_links
             if [new_researcher_link[1], new_researcher_link[0], new_researcher_link[2], new_researcher_link[3]]
             in new_researcher_links]

            '''
            # for new researcher link in new researcher links
            for new_researcher_link in new_researcher_links:
                # variable to hold reversed new researcher links
                reversed_new_researcher_links = [x for x in new_researcher_links
                                                 if [x[0], x[1]] == [new_researcher_link[1], new_researcher_link[0]]]
                # if reversed new researcher links exist
                if reversed_new_researcher_links:
                    # remove new researcher link from new researcher links
                    new_researcher_links.remove(new_researcher_link)
                    # remove reversed new researcher link from new researcher links
                    new_researcher_links.remove(reversed_new_researcher_links[0])
                    # variable to hold number
                    number = new_researcher_link[2] + reversed_new_researcher_links[0][2]
                    # variable to hold value
                    value = new_researcher_link[3] + reversed_new_researcher_links[0][3]
                    # add new researcher link to new researcher links
                    new_researcher_links += [[new_researcher_link[0], new_researcher_link[1], number, value]]
            '''

            # variable to hold output file
            output_file = open('../output/researchers/{}/links/grant_researcher_links.csv'.format(path), mode='w')

            # set locale to Great Britain
            setlocale(LC_ALL, 'en_GB.utf8')

            # for new researcher link in new researcher links
            for new_researcher_link in new_researcher_links:
                # write new researcher link to file
                output_file.write('"{}","{}","{}","{}"\n'.format(new_researcher_link[0], new_researcher_link[1],
                                                                 new_researcher_link[2],
                                                                 currency(new_researcher_link[3], grouping=True)))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/researchers/{}/links/grant_researcher_links.pkl'.format(path), 'wb')
            # write data structure to file
            dump(new_researcher_links, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of grant researcher links ({}) completed ({} grant researcher links'
                  ' extracted)'.format(path, len(new_researcher_links)))


########################################################################################################################


# main function
def main():

    # link areas
    LinkAreas.run()

    # link topics
    LinkTopics.run()

    # link researchers
    LinkResearchers.run()


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
