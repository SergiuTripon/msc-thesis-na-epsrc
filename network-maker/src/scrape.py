#!/usr/bin/env python3

########################################################################################################################

# standard library modules
import os
from lxml import html
from locale import setlocale, LC_ALL, atoi, currency

# third-party library modules
import requests
from pickle import dump, load
from collections import OrderedDict

########################################################################################################################


# ExtractAreas class
class ExtractAreas:

    @staticmethod
    def run():

        # extract area information
        ExtractAreas.extract_area_info()
        # extract grant information
        ExtractAreas.extract_grant_info()

    ####################################################################################################################

    @staticmethod
    # extracts area information
    def extract_area_info():

        # if areas file does not exist
        if not os.path.isfile('../output/areas/info/area_info.csv'):

            # variable to hold page
            page = requests.get('http://gow.epsrc.ac.uk/NGBOListResearchAreas.aspx')
            # variable to hold tree
            tree = html.fromstring(page.content)

            # variable to hold name xpath
            name_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=1]/a/text()"
            # variable to hold url xpath
            url_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=1]/a/@href"
            # variable to hold grant number xpath
            grant_num_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=2]/text()"
            # variable to hold proportional value xpath
            prop_val_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=3]/span/text()"
            # variable to hold grant value xpath
            grant_val_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=4]/span/text()"

            # variable to hold names
            names = tree.xpath(name_xpath)
            # variable to hold urls
            urls = tree.xpath(url_xpath)
            # variable to hold grant numbers
            grant_nums = tree.xpath(grant_num_xpath)
            # variable to hold proportional values
            prop_vals = tree.xpath(prop_val_xpath)
            # variable to hold grant values
            grant_vals = tree.xpath(grant_val_xpath)

            # variable to hold output file
            output_file = open('../output/areas/info/area_info.csv', mode='a')

            # variable to hold zipped attributes
            attr_zip = zip(names, urls, grant_nums, prop_vals, grant_vals)

            # variable to hold areas dictionary
            areas = OrderedDict()

            # set locale to Great Britain
            setlocale(LC_ALL, 'en_GB.utf8')

            # for attributes in zipped attributes
            for name, url, grant_num, prop_val, grant_val in attr_zip:
                # variable to hold grant number
                grant_num = int(grant_num)
                # variable to hold proportional value
                prop_val = atoi(prop_val)
                # variable to hold grant value
                grant_val = atoi(grant_val)
                # add area to areas dictionary
                areas[name] = [url, grant_num, prop_val, grant_val]

                # write area to file
                output_file.write('"{}","{}","{}","{}","{}"\n'.format(name, url, grant_num,
                                                                      currency(prop_val, grouping=True),
                                                                      currency(grant_val, grouping=True)))

            # variable to hold output file
            output_file = open(r'../output/areas/info/area_info.pkl', 'wb')
            # write data structure to file
            dump(areas, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of areas completed ({} areas extracted)'.format(len(areas)))

    ####################################################################################################################

    @staticmethod
    # extracts grant information
    def extract_grant_info():

        # if grants file does not exist
        if not os.path.isfile('../output/areas/info/grant_info.csv'):

            # variable to hold input file
            input_file = open(r'../output/areas/info/area_info.pkl', 'rb')
            # load data structure from file
            areas = load(input_file)
            # close input file
            input_file.close()

            # variable to hold output file
            output_file = open('../output/areas/info/grant_info.csv', mode='a')

            # variable to hold grants dictionary
            grants = OrderedDict()

            # set locale to Great Britain
            setlocale(LC_ALL, 'en_GB.utf8')

            # for area names and attributes in areas dictionary
            for area_name, area_attr in areas.items():

                # variable to hold page
                page = requests.get('http://gow.epsrc.ac.uk/' + area_attr[0])
                # variable to hold tree
                tree = html.fromstring(page.content)

                # variable to hold reference xpath
                ref_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=1]/a/@title"
                # variable to hold total value xpath
                total_val_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=5]/span/text()"

                # variable to hold references
                refs = tree.xpath(ref_xpath)
                # variable to hold total values
                total_vals = tree.xpath(total_val_xpath)
                # variable to hold unique references list
                unique_refs = []

                # for reference in references
                for ref in refs:
                    # if reference is not in unique references
                    if ref not in unique_refs:
                        # add reference to unique references list
                        unique_refs += [ref]

                # merge references and total values, converted to raw numbers
                refs_total_vals_raw = [[ref, atoi(total_val)] for ref, total_val in zip(unique_refs, total_vals)]
                # merge references and total values, converted to currency
                refs_total_vals_currency = [[ref, currency(atoi(total_val), grouping=True)] for ref, total_val in
                                            zip(unique_refs, total_vals)]

                # add grant to grants dictionary
                grants[area_name] = refs_total_vals_raw

                # write grant to file
                output_file.write('"{}","{}"\n'.format(area_name, refs_total_vals_currency))

            # variable to hold output file
            output_file = open(r'../output/areas/info/grant_info.pkl', 'wb')
            # write data structure to file
            dump(grants, output_file)
            # close output file
            output_file.close()

            # variable to hold total number of grants
            grants_num_total = 0
            # for grant reference in grant references
            for grant_ref in grants.values():
                # add number of grants within an area to total number of grants
                grants_num_total += len(grant_ref)

            # print progress
            print('> Extraction of grants completed ({} grants extracted)'.format(grants_num_total))


########################################################################################################################


# ExtractTopics class
class ExtractTopics:

    @staticmethod
    # runs other functions
    def run():

        # extract topic urls
        ExtractTopics.extract_topic_urls()
        # extract grant urls
        ExtractTopics.extract_grant_urls()
        # extract researcher urls
        ExtractTopics.extract_researcher_urls()

        # extract topic information
        ExtractTopics.extract_topic_info()
        # extract grant information
        ExtractTopics.extract_grant_info()

        # extract grant topics
        ExtractTopics.extract_grant_topics()
        # extract grant researchers
        ExtractTopics.extract_grant_researchers()

        # extract researcher topics
        ExtractTopics.extract_researcher_topics()

    ####################################################################################################################

    @staticmethod
    # extracts topic urls
    def extract_topic_urls():

        # if topic urls file does not exist
        if not os.path.isfile('../output/topics/urls/topics/topics.txt'):

            # print progress
            print('> Extraction of topic urls started')

            # variable to hold page
            page = open(r'../output/topics/html/topics/NGBOListTopics.aspx').read()
            # variable to hold tree
            tree = html.fromstring(page)

            # variable to hold url xpath
            url_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=1]/a/@href"

            # variable to hold urls
            urls = tree.xpath(url_xpath)

            # variable to hold output file
            output_file = open('../output/topics/urls/topics/topics.txt', mode='w')

            # write topics page url to file
            output_file.write('http://gow.epsrc.ac.uk/NGBOListTopics.aspx\n')

            # variable to hold full urls
            full_urls = []

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for url in urls
            for url in urls:
                # if url is not in full urls
                if url not in full_urls:
                    # add url to full urls
                    full_urls += [url]
                    # write url to file
                    output_file.write('http://gow.epsrc.ac.uk/{}\n'.format(url))

                    # print progress
                    print('> Extraction of topics urls in progress'
                          ' ({} topic url(s) extracted)'.format(extraction_count))
                    # increment extraction count
                    extraction_count += 1

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/urls/topics/topics.pkl', 'wb')
            # write data structure to file
            dump(full_urls, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of topic urls completed ({} topic urls extracted)'.format(len(full_urls)))

    ####################################################################################################################

    @staticmethod
    # extracts grant urls
    def extract_grant_urls():

        # if grant urls file does not exist
        if not os.path.isfile('../output/topics/urls/grants/grants.txt'):

            # print progress
            print('> Extraction of grant urls started')

            # variable to hold input file
            input_file = open(r'../output/topics/urls/topics/topics.pkl', 'rb')
            # load data structure from file
            topic_urls = load(input_file)
            # close input file
            input_file.close()

            # variable to hold urls
            urls = []

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for topic url in topic urls
            for topic_url in topic_urls:

                # variable to hold page
                page = open(r'../output/topics/html/topics/{}'.format(topic_url.replace('/', '%2F'))).read()
                # variable to hold tree
                tree = html.fromstring(page)

                # variable to hold url xpath
                url_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=1]/a/@href"

                # add urls to urls
                urls += tree.xpath(url_xpath)

                # print progress
                print('> Extraction of grant urls in progress (grant urls for {} topic(s)'
                      ' extracted)'.format(extraction_count))

                # increment extraction count
                extraction_count += 1

            # variable to hold full urls
            full_urls = []

            # variable to hold output file
            output_file = open('../output/topics/urls/grants/grants.txt', mode='w')

            # for url in urls
            for url in urls:
                # if url is not in full urls
                if url not in full_urls:
                    # add url to full urls
                    full_urls += [url]
                    # write url to file
                    output_file.write('http://gow.epsrc.ac.uk/{}\n'.format(url))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/urls/grants/grants.pkl', 'wb')
            # write data structure to file
            dump(full_urls, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of grant urls completed ({} grant urls extracted)'.format(len(full_urls)))

    ####################################################################################################################

    @staticmethod
    # extracts research urls
    def extract_researcher_urls():

        # if researcher urls file does not exist
        if not os.path.isfile('../output/topics/urls/researchers/researchers.txt'):

            # print progress
            print('> Extraction of researcher urls started')

            # variable to hold input file
            input_file = open(r'../output/topics/urls/grants/grants.pkl', 'rb')
            # load data structure from file
            grant_urls = load(input_file)
            # close input file
            input_file.close()

            # variable to hold urls
            urls = []

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for grant url in grant urls
            for grant_url in grant_urls:

                # variable to hold page
                page = open(r'../output/topics/html/grants/{}'.format(grant_url.replace('/', '%2F')), "r").read()
                # variable to hold tree
                tree = html.fromstring(page)

                # variable to hold main url xpath
                main_url_xpath = "//table[@id='tblFound']/tr[position()=3]/td[position()=2]/a/@href"
                # variable to hold other url xpath
                other_url_xpath = "//table[@id='tblFound']/tr[position()=4]/td[position()=2]/table/tr/td/a/@href"

                # add main urls to urls
                urls += tree.xpath(main_url_xpath)
                # add other urls to urls
                urls += tree.xpath(other_url_xpath)

                # print progress
                print('> Extraction of researcher urls in progress (researcher urls for {} grant(s)'
                      ' extracted)'.format(extraction_count))

                # increment extraction count
                extraction_count += 1

            # variable to hold full urls
            full_urls = []

            # variable to hold output file
            output_file = open('../output/topics/urls/researchers/researchers.txt', mode='w')

            # for url in urls
            for url in urls:
                # if url is not in full urls
                if url not in full_urls:
                    # add url to full urls
                    full_urls += [url]
                    # write url to file
                    output_file.write('http://gow.epsrc.ac.uk/{}\n'.format(url))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/urls/researchers/researchers.pkl', 'wb')
            # write data structure to file
            dump(full_urls, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of researcher urls completed ({} researcher urls extracted)'.format(len(full_urls)))

    ####################################################################################################################

    @staticmethod
    # extracts topic information
    def extract_topic_info():

        # if topic information file does not exist
        if not os.path.isfile('../output/topics/info/topics/topic_info.csv'):

            # print progress
            print('> Extraction of topic information started')

            # variable to hold page
            page = open(r'../output/topics/html/topics/NGBOListTopics.aspx', "r").read()
            # variable to hold tree
            tree = html.fromstring(page)

            # variable to hold name xpath
            name_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=1]/a/text()"
            # variable to hold url xpath
            url_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=1]/a/@href"
            # variable to hold grant number xpath
            grant_num_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=2]/text()"
            # variable to hold value xpath
            val_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=3]/span/text()"

            # variable to hold names
            names = tree.xpath(name_xpath)
            # variable to hold urls
            urls = tree.xpath(url_xpath)
            # variable to hold grant numbers
            grant_nums = tree.xpath(grant_num_xpath)
            # variable to hold values
            vals = tree.xpath(val_xpath)

            # variable to hold zipped attributes
            attr_zip = zip(names, urls, grant_nums, vals)

            # set locale to Great Britain
            setlocale(LC_ALL, 'en_GB.utf8')

            # variable to hold topics
            topics = OrderedDict((name, [url, int(grant_num), atoi(val)]) for name, url, grant_num, val in attr_zip)

            # variable to hold output file
            output_file = open('../output/topics/info/topics/topic_info.csv', mode='w')

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for name and attributes in topics
            for name, attr in topics.items():
                # write name and attributes to file
                output_file.write('"{}","{}","{}","{}"\n'.format(name, attr[0], attr[1],
                                                                 currency(attr[2], grouping=True)))
                # print progress
                print('> Extraction of topic information in progress (information for {} topic(s)'
                      ' extracted)'.format(extraction_count))

                # increment extraction count
                extraction_count += 1

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/info/topics/topic_info.pkl', 'wb')
            # write data structure to file
            dump(topics, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of topic information completed (information for {} topics'
                  ' extracted)'.format(len(topics)))

    ####################################################################################################################

    @staticmethod
    # extracts grant information
    def extract_grant_info():

        # if grants information file does not exist
        if not os.path.isfile('../output/topics/info/grants/grant_info.csv'):

            # print progress
            print('> Extraction of grant information started')

            # variable to hold input file
            input_file = open(r'../output/topics/urls/topics/topics.pkl', 'rb')
            # load data structure from file
            topic_urls = load(input_file)
            # close input file
            input_file.close()

            # variable to hold grants
            grants = []

            # for topic url in topics urls
            for topic_url in topic_urls:

                # variable to hold page
                page = open(r'../output/topics/html/topics/{}'.format(topic_url), "r").read()
                # variable to hold tree
                tree = html.fromstring(page)

                # variable to hold reference xpath
                ref_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=1]/a/@title"
                # variable to hold url xpath
                url_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=1]/a/@href"
                # variable to hold total value xpath
                total_val_xpath = "//table[@id='dgDetails']/tr[position()>1]/td[position()=5]/span/text()"

                # variable to hold references
                refs = tree.xpath(ref_xpath)
                # variable to hold urls
                urls = tree.xpath(url_xpath)
                # variable to hold total values
                total_vals = tree.xpath(total_val_xpath)

                # variable to hold unique references
                unique_refs = []

                # for reference in references
                for ref in refs:
                    # if reference is not in unique references
                    if ref not in unique_refs:
                        # add reference to unique references
                        unique_refs += [ref]

                # variable to hold zipped attributes
                attr_zip = zip(unique_refs, urls, total_vals)

                # set locale to Great Britain
                setlocale(LC_ALL, 'en_GB.utf8')

                # add grant to grants
                grants += [[unique_ref, url, atoi(total_val)] for unique_ref, url, total_val in attr_zip]

            # variable to hold grants
            grants = OrderedDict((grant[0], [grant[1], grant[2]]) for grant in grants)

            # variable to hold output file
            output_file = open('../output/topics/info/grants/grant_info.csv', mode='w')

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for name and attributes in grants
            for ref, attr in grants.items():
                # write name and attributes to file
                output_file.write('"{}","{}","{}"\n'.format(ref, attr[0], currency(attr[1], grouping=True)))

                # print progress
                print('> Extraction of grant information in progress (information for {} grant(s)'
                      ' extracted)'.format(extraction_count))

                # increment extraction count
                extraction_count += 1

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/info/grants/grant_info.pkl', 'wb')
            # write data structure to file
            dump(grants, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of grant information completed (information for {} grants'
                  ' extracted)'.format(len(grants)))

    ####################################################################################################################

    @staticmethod
    # extracts grant topics
    def extract_grant_topics():

        # if grant topics file does not exist
        if not os.path.isfile('../output/topics/info/grants/grant_topics.csv'):

            # print progress
            print('> Extraction of grant topics started')

            # variable to hold input file
            input_file = open(r'../output/topics/urls/grants/grants.pkl', 'rb')
            # load data structure from file
            grant_urls = load(input_file)
            # close input file
            input_file.close()

            # variable to hold grant topics
            grant_topics = OrderedDict()

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for grant url in grant urls
            for grant_url in grant_urls:

                # variable to hold page
                page = open(r'../output/topics/html/grants/{}'.format(grant_url.replace('/', '%2F')), "r").read()
                # variable to hold tree
                tree = html.fromstring(page)

                # variable to hold value xpath
                value_xpath = "//table[@id='tblFound']/tr[position()=10]/td[position()=6]/span/text()"
                # variable to hold topics xpath
                topics_xpath = "//table[@id='tblFound']/tr[position()=11]/td[position()=2]/table/tr/td/text()"

                # variable to hold values
                values = tree.xpath(value_xpath)
                # variable to hold topics
                topics = tree.xpath(topics_xpath)

                # variable to hold clean topics
                clean_topics = []

                # for topic in topics
                for topic in topics:
                    # remove spaces
                    topic = topic.strip().lower()
                    # if topic is not empty and is not in clean topics
                    if topic and topic not in clean_topics:
                        # add topic to clean topics
                        clean_topics += [topic]

                # set locale to Great Britain
                setlocale(LC_ALL, 'en_GB.utf8')

                # add grant topics to grant topics
                grant_topics[grant_url.strip('NGBOViewGrant.aspx?GrantRef=')] = [clean_topics, atoi(values[0])]

                # print progress
                print('> Extraction of grant topics in progress (topics for {} grant(s)'
                      ' extracted)'.format(extraction_count))

                # increment extraction count
                extraction_count += 1

            # variable to hold output file
            output_file = open('../output/topics/info/grants/grant_topics.csv', mode='w')

            # for reference and attributes in grant topics
            for ref, attr in grant_topics.items():
                # write reference and attributes to file
                output_file.write('"{}","{}","{}"\n'.format(ref, attr[0], currency(attr[1], grouping=True)))

            # close input file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/info/grants/grant_topics.pkl', 'wb')
            # write data structure to file
            dump(grant_topics, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of grant topics completed (topics for {} grants'
                  ' extracted)'.format(len(grant_topics)))

    ####################################################################################################################

    @staticmethod
    # extract grant researchers
    def extract_grant_researchers():

        # if grant researchers file does not exist
        if not os.path.isfile('../output/topics/info/grants/grant_researchers.csv'):

            # print progress
            print('> Extraction of grant researchers started')

            # variable to hold input file
            input_file = open(r'../output/topics/urls/grants/grants.pkl', 'rb')
            # load data structure from file
            grant_urls = load(input_file)
            # close input file
            input_file.close()

            # variable to hold grant researchers
            grant_researchers = OrderedDict()

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for grant url in grant urls
            for grant_url in grant_urls:

                # variable to hold page
                page = open(r'../output/topics/html/grants/{}'.format(grant_url.replace('/', '%2F')), "r").read()
                # variable to hold tree
                tree = html.fromstring(page)

                # variable to hold main url xpath
                main_url_xpath = "//table[@id='tblFound']/tr[position()=3]/td[position()=2]/a/@href"
                # variable to hold other url xpath
                other_url_xpath = "//table[@id='tblFound']/tr[position()=4]/td[position()=2]/table/tr/td/a/@href"

                # variable to hold main urls
                main_urls = tree.xpath(main_url_xpath)
                # variable to hold other urls
                other_urls = tree.xpath(other_url_xpath)

                # variable to hold all urls
                all_urls = main_urls + other_urls

                # variable to hold all urls
                all_urls = [url.strip('NGBOViewPerson.aspx?PersonId=') for url in all_urls]

                # add grant researchers to grant researchers
                grant_researchers[grant_url.strip('NGBOViewGrant.aspx?GrantRef=')] = all_urls

                # print progress
                print('> Extraction of grant researchers in progress (researchers for {} grant(s)'
                      ' extracted)'.format(extraction_count))

                # increment extraction count
                extraction_count += 1

            # variable to hold output file
            output_file = open('../output/topics/info/grants/grant_researchers.csv', mode='w')

            # for reference and researchers in grant researchers
            for ref, researchers in grant_researchers.items():
                # write reference and researchers to file
                output_file.write('"{}","{}"\n'.format(ref, researchers))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/info/grants/grant_researchers.pkl', 'wb')
            # write data structure to file
            dump(grant_researchers, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of grant researchers completed (researchers for {} grants'
                  ' extracted)'.format(len(grant_researchers)))

    ####################################################################################################################

    @staticmethod
    # extracts researcher topics
    def extract_researcher_topics():

        # if researcher topics file does not exist
        if not os.path.isfile('../output/topics/info/researchers/researcher_topics.csv'):

            # print progress
            print('> Extraction of researcher topics started')

            # variable to hold researcher urls
            researcher_urls = [researcher_url.strip('http://gow.epsrc.ac.uk/') for researcher_url in
                               open(r'../output/topics/urls/researchers/researchers.txt', "r").read().splitlines()]

            # variable to hold researcher topics
            researcher_topics = OrderedDict()

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for researcher url in researcher urls
            for researcher_url in researcher_urls:

                # variable to hold page
                page = open(r'../output/topics/html/researchers/{}'.format(researcher_url), "r").read()
                # variable to hold tree
                tree = html.fromstring(page)

                # variable to hold topics xpath
                topics_xpath = "//span[starts-with(@id, 'dgResearchTopics_ctl')]/text()"

                # variable to hold topics
                topics = tree.xpath(topics_xpath)

                # variable to hold clean topics
                clean_topics = []

                # for topic in topics
                for topic in topics:
                    # remove space
                    topic = topic.strip().lower()
                    # if topic is not empty and is not in clean topics
                    if topic and topic not in clean_topics:
                        # add topic to clean topics
                        clean_topics += [topic]

                # add researcher topics to researcher topics
                researcher_topics[researcher_url.replace('NGBOViewPerson.aspx?PersonId=', '')] = clean_topics

                # print progress
                print('> Extraction of researcher topics in progress (topics for {} researcher(s)'
                      ' extracted)'.format(extraction_count))

                # increment extraction count
                extraction_count += 1

            # variable to hold output file
            output_file = open('../output/topics/info/researchers/researcher_topics.csv', mode='w')

            # for identifier and topics in researcher topics
            for identifier, topics in researcher_topics.items():
                # write identifier and topics to file
                output_file.write('"{}","{}"\n'.format(identifier, topics))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/topics/info/researchers/researcher_topics.pkl', 'wb')
            # write data structure to file
            dump(researcher_topics, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of researcher topics completed (topics for {} researchers'
                  ' extracted)'.format(len(researcher_topics)))

########################################################################################################################


# ExtractPastTopics class
class ExtractPastTopics:

    @staticmethod
    # runs other functions
    def run():

        # extract researcher urls from 1990 to 2000
        ExtractPastTopics.extract_researcher_urls('_1990_2000')
        # extract researcher urls from 2000 to 2010
        ExtractPastTopics.extract_researcher_urls('_2000_2010')

        # extract grant topics from 1990 to 2000
        ExtractPastTopics.extract_grant_topics('_1990_2000')
        # extract grant topics from 2000 to 2010
        ExtractPastTopics.extract_grant_topics('_2000_2010')

        # extract grant researchers from 2000 to 2010
        ExtractPastTopics.extract_grant_researchers('_1990_2000')
        # extract grant researchers from 2000 to 2010
        ExtractPastTopics.extract_grant_researchers('_2000_2010')

        # extract researcher topics from 1990 to 2000
        ExtractPastTopics.extract_researcher_topics('_1990_2000')
        # extract researcher topics from 2000 to 2010
        ExtractPastTopics.extract_researcher_topics('_2000_2010')

    ####################################################################################################################

    @staticmethod
    # extracts researcher urls from 1990/2000 to 2000/2010
    def extract_researcher_urls(years):

        # if researcher urls file does not exist
        if not os.path.isfile('../output/past-topics/urls/researchers/researchers{}.txt'.format(years)):

            # print progress
            print('> Extraction of researcher urls ({}) started'.format(years[1:].replace('_', '-')))

            # variable to hold grant urls
            grant_urls = [grant_url.strip('http://gow.epsrc.ac.uk/') for grant_url in
                          open(r'../output/past-topics/urls/grants/grants{}.txt'.format(years),
                               "r").read().splitlines()]

            # variable to hold urls
            urls = []

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for grant url in grant urls
            for grant_url in grant_urls:

                # variable to hold page
                page = open(r'../output/past-topics/html/grants{}/{}'.format(years, grant_url.replace('/', '%2F')),
                            "r").read()
                # variable to hold tree
                tree = html.fromstring(page)

                # variable to hold main url xpath
                main_url_xpath = "//table[@id='tblFound']/tr[position()=3]/td[position()=2]/a/@href"
                # variable to hold other url xpath
                other_url_xpath = "//table[@id='tblFound']/tr[position()=4]/td[position()=2]/table/tr/td/a/@href"

                # add main urls to urls
                urls += tree.xpath(main_url_xpath)
                # add other urls to urls
                urls += tree.xpath(other_url_xpath)

                # print progress
                print('> Extraction of researcher urls ({}) in progress (researcher urls for {} grant(s)'
                      ' extracted)'.format(years[1:].replace('_', '-'), extraction_count))

                # increment extraction count
                extraction_count += 1

            # variable to hold full urls
            full_urls = []

            # variable to hold output file
            output_file = open('../output/past-topics/urls/researchers/researchers{}.txt'.format(years), mode='w')

            # for url in urls
            for url in urls:
                # if url is not in full urls
                if url not in full_urls:
                    # add url to full urls
                    full_urls += [url]
                    # write url to file
                    output_file.write('http://gow.epsrc.ac.uk/{}\n'.format(url))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/past-topics/urls/researchers/researchers{}.pkl'.format(years), 'wb')
            # write data structure to file
            dump(full_urls, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of researcher urls ({}) completed ({} researcher urls extracted)'
                  .format(years[1:].replace('_', '-'), len(full_urls)))

    ####################################################################################################################

    @staticmethod
    # extracts grant topics from 1990/2000 to 2000/2010
    def extract_grant_topics(years):

        # if grant topics file does not exist
        if not os.path.isfile('../output/past-topics/info/grants/grant_topics{}.csv'.format(years)):

            # print progress
            print('> Extraction of grant topics ({}) started'.format(years[1:].replace('_', '-')))

            # variable to hold grant urls
            grant_urls = [grant_url.strip('http://gow.epsrc.ac.uk/') for grant_url in
                          open(r'../output/past-topics/urls/grants/grants{}.txt'.format(years),
                               "r").read().splitlines()]

            # variable to hold grant topics
            grant_topics = OrderedDict()

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for grant url in grant urls
            for grant_url in grant_urls:

                # variable to hold page
                page = open(r'../output/past-topics/html/grants{}/{}'.format(years, grant_url.replace('/', '%2F')),
                            "r").read()
                # variable to hold tree
                tree = html.fromstring(page)

                # variable to hold value xpath
                value_xpath = "//table[@id='tblFound']/tr[position()=10]/td[position()=6]/span/text()"
                # variable to hold topics xpath
                topics_xpath = "//table[@id='tblFound']/tr[position()=11]/td[position()=2]/table/tr/td/text()"

                # variable to hold values
                values = tree.xpath(value_xpath)
                # variable to hold topics
                topics = tree.xpath(topics_xpath)

                # variable to hold clean topics
                clean_topics = []

                # for topic in topics
                for topic in topics:
                    # remove spaces
                    topic = topic.strip().lower()
                    # if topic is not empty and is not in clean topics
                    if topic and topic not in clean_topics:
                        # add topic to clean topics
                        clean_topics += [topic]

                # set locale to Great Britain
                setlocale(LC_ALL, 'en_GB.utf8')

                # add grant topics to grant topics
                grant_topics[grant_url.replace('NGBOViewGrant.aspx?GrantRef=', '')] = [clean_topics, atoi(values[0])]

                # print progress
                print('> Extraction of grant topics ({}) in progress (topics for {} grant(s)'
                      ' extracted)'.format(years[1:].replace('_', '-'), extraction_count))

                # increment extraction count
                extraction_count += 1

            # variable to hold output file
            output_file = open('../output/past-topics/info/grants/grant_topics{}.csv'.format(years), mode='w')

            # for reference and attributes in grant topics
            for ref, attr in grant_topics.items():
                # write reference and attributes to file
                output_file.write('"{}","{}","{}"\n'.format(ref, attr[0], currency(attr[1], grouping=True)))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/past-topics/info/grants/grant_topics{}.pkl'.format(years), 'wb')
            # write data structure to file
            dump(grant_topics, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of grant topics ({}) completed (topics for {} grants'
                  ' extracted)'.format(years[1:].replace('_', '-'), len(grant_topics)))

    ####################################################################################################################

    @staticmethod
    # extract grant researchers from 1990/2000 to 2000/2010
    def extract_grant_researchers(years):

        # if grant researchers file does not exist
        if not os.path.isfile('../output/past-topics/info/grants/grant_researchers{}.csv'.format(years)):

            # print progress
            print('> Extraction of grant researchers ({}) started'.format(years[1:].replace('_', '-')))

            # variable to hold grant urls
            grant_urls = [grant_url.strip('http://gow.epsrc.ac.uk/') for grant_url in
                          open(r'../output/past-topics/urls/grants/grants{}.txt'.format(years),
                               "r").read().splitlines()]

            # variable to hold grant researchers
            grant_researchers = OrderedDict()

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for grant url in grant urls
            for grant_url in grant_urls:

                # variable to hold page
                page = open(r'../output/past-topics/html/grants{}/{}'.format(years, grant_url.replace('/', '%2F')),
                            "r").read()
                # variable to hold tree
                tree = html.fromstring(page)

                # variable to hold main url xpath
                main_url_xpath = "//table[@id='tblFound']/tr[position()=3]/td[position()=2]/a/@href"
                # variable to hold other url xpath
                other_url_xpath = "//table[@id='tblFound']/tr[position()=4]/td[position()=2]/table/tr/td/a/@href"

                # variable to hold main urls
                main_urls = tree.xpath(main_url_xpath)
                # variable to hold other urls
                other_urls = tree.xpath(other_url_xpath)

                # variable to hold all urls
                all_urls = main_urls + other_urls

                # variable to hold all ids
                all_ids = [identifier.strip('NGBOViewPerson.aspx?PersonId=') for identifier in all_urls]

                # add grant researchers to grant researchers
                grant_researchers[grant_url.strip('NGBOViewGrant.aspx?GrantRef=')] = all_ids

                # print progress
                print('> Extraction of grant researchers ({}) in progress (researchers for {} grant(s)'
                      ' extracted)'.format(years[1:].replace('_', '-'), extraction_count))

                # increment extraction count
                extraction_count += 1

            # variable to hold output file
            output_file = open('../output/past-topics/info/grants/grant_researchers{}.csv'.format(years), mode='w')

            # for reference and researchers in grant researchers
            for ref, researchers in grant_researchers.items():
                # write reference and researchers to file
                output_file.write('"{}","{}"\n'.format(ref, researchers))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/past-topics/info/grants/grant_researchers{}.pkl'.format(years), 'wb')
            # write data structure to file
            dump(grant_researchers, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of grant researchers ({}) completed (researchers for {} grants'
                  ' extracted)'.format(years[1:].replace('_', '-'), len(grant_researchers)))

    ####################################################################################################################

    @staticmethod
    # extracts researcher topics from 1990/2000 to 2000/2010
    def extract_researcher_topics(years):

        # if researcher topics file does not exist
        if not os.path.isfile('../output/past-topics/info/researchers/researcher_topics{}.csv'.format(years)):

            # print progress
            print('> Extraction of researcher topics ({}) started'.format(years[1:].replace('_', '-')))

            # variable to hold researcher urls
            researcher_urls = [researcher_url.strip('http://gow.epsrc.ac.uk/') for researcher_url in
                               open(r'../output/past-topics/urls/researchers/researchers{}.txt'.format(years),
                                    "r").read().splitlines()]

            # variable to hold researcher topics
            researcher_topics = OrderedDict()

            # variable to hold extraction count set to 1
            extraction_count = 1

            # for researcher url in researcher urls
            for researcher_url in researcher_urls:

                # variable to hold page
                page = open(r'../output/past-topics/html/researchers{}/{}'.format(years, researcher_url), "r").read()
                # variable to hold tree
                tree = html.fromstring(page)

                # variable to hold topics xpath
                topics_xpath = "//span[starts-with(@id, 'dgResearchTopics_ctl')]/text()"

                # variable to hold topics
                topics = tree.xpath(topics_xpath)

                # variable to hold clean topics
                clean_topics = []

                # for topic in topics
                for topic in topics:
                    # remove spaces
                    topic = topic.strip().lower()
                    # if topic is not empty and is not in clean topics
                    if topic and topic not in clean_topics:
                        # add topic to clean topics
                        clean_topics += [topic]

                # add researcher topics to researcher topics
                researcher_topics[researcher_url.replace('NGBOViewPerson.aspx?PersonId=', '')] = clean_topics

                # print progress
                print('> Extraction of researcher topics ({}) in progress (topics for {} researcher(s)'
                      ' extracted)'.format(years[1:].replace('_', '-'), extraction_count))

                # increment extraction count
                extraction_count += 1

            # variable to hold output file
            output_file = open('../output/past-topics/info/researchers/researcher_topics{}.csv'.format(years), mode='w')

            # for identifier and topics in researcher topics
            for identifier, topics in researcher_topics.items():
                # write identifier and topics to file
                output_file.write('"{}","{}"\n'.format(identifier, topics))

            # close output file
            output_file.close()

            # variable to hold output file
            output_file = open(r'../output/past-topics/info/researchers/researcher_topics{}.pkl'.format(years), 'wb')
            # write data structure to file
            dump(researcher_topics, output_file)
            # close output file
            output_file.close()

            # print progress
            print('> Extraction of researcher topics ({}) completed (topics for {} researchers'
                  ' extracted)'.format(years[1:].replace('_', '-'), len(researcher_topics)))


########################################################################################################################


# main function
def main():

    # extract areas
    ExtractAreas.run()
    # extract topics
    ExtractTopics.run()
    # extract past topics
    ExtractPastTopics.run()


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
