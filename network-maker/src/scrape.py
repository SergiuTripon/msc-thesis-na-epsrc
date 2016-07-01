#!/usr/bin/env python3

########################################################################################################################

# standard library modules
import os
import locale
from lxml import html

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
        if not os.path.isfile('../output/areas/areas.csv'):

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
            output_file = open('../output/areas/areas.csv', mode='a')

            # variable to hold zipped attributes
            attr_zip = zip(names, urls, grant_nums, prop_vals, grant_vals)

            # variable to hold areas dictionary
            areas = OrderedDict()

            # set locale to Great Britain
            locale.setlocale(locale.LC_ALL, 'en_GB.utf8')

            # for attributes in zipped attributes
            for name, url, grant_num, prop_val, grant_val in attr_zip:
                # variable to hold grant number
                grant_num = int(grant_num)
                # variable to hold proportional value
                prop_val = locale.atoi(prop_val)
                # variable to hold grant value
                grant_val = locale.atoi(grant_val)
                # add area to areas dictionary
                areas[name] = [url, grant_num, prop_val, grant_val]

                # write area to file
                output_file.write('"{}","{}","{}","{}","{}"\n'.format(name, url, grant_num,
                                                                      locale.currency(prop_val, grouping=True),
                                                                      locale.currency(grant_val, grouping=True)))

            # variable to hold output file
            output_file = open(r'../output/areas/areas.pkl', 'wb')
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
        if not os.path.isfile('../output/areas/grants.csv'):

            # variable to hold input file
            input_file = open(r'../output/areas/areas.pkl', 'rb')
            # load data structure from file
            areas = load(input_file)
            # close input file
            input_file.close()

            # variable to hold output file
            output_file = open('../output/areas/grants.csv', mode='a')

            # variable to hold grants dictionary
            grants = OrderedDict()

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
                refs_total_vals_raw = [[ref, locale.atoi(total_val)] for ref, total_val in zip(unique_refs, total_vals)]
                # merge references and total values, converted to currency
                refs_total_vals_currency = [[ref, locale.currency(locale.atoi(total_val), grouping=True)]
                                            for ref, total_val in zip(unique_refs, total_vals)]

                # add grant to grants dictionary
                grants[area_name] = refs_total_vals_raw

                # write grant to file
                output_file.write('"{}","{}"\n'.format(area_name, refs_total_vals_currency))

            # variable to hold output file
            output_file = open(r'../output/areas/grants.pkl', 'wb')
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


# main function
def main():

    # extract areas
    ExtractAreas.run()


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
