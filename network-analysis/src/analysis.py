#!/usr/bin/env python3

########################################################################################################################

import pandas as pd
import graphistry

########################################################################################################################

# variable to hold API key
api_key = 'cd97e75121bb38884873b5e6dd0b51222d2986658c51371ab94ba7dd060d93f15684fb8dbf128cbb7a63349ca9d02558'
# set API key
graphistry.register(key=api_key)

########################################################################################################################


# main function
def main():

    # variable to hold edges
    edges = pd.read_csv('../../data/networks/areas/edges_graphistry.tsv', delimiter='\t', encoding='utf-8')

    # variable to hold plotter
    plotter = graphistry.bind(source="source", destination="target")
    # plot edges
    plotter.plot(edges)


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
