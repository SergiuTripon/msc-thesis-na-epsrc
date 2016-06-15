#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
import graphistry
import pandas as pd
from igraph import *

########################################################################################################################


# analyses network uses graphistry
def graphistry_analysis():

    # variable to hold API key
    api_key = 'cd97e75121bb38884873b5e6dd0b51222d2986658c51371ab94ba7dd060d93f15684fb8dbf128cbb7a63349ca9d02558'
    # set API key
    graphistry.register(key=api_key)

    # variable to hold edges
    edges = pd.read_csv('../../data/networks/areas/edges_graphistry.tsv', delimiter='\t', encoding='utf-8')

    # variable to hold plotter
    plotter = graphistry.bind(source="source", destination="target")
    # plot edges
    plotter.plot(edges)


########################################################################################################################

# analyses network using igraph
def igraph_analysis():

    # variable to hold epsrc network
    epsrc = Graph.Read_GraphML('../../data/networks/areas/nodes_edges.graphml')
    # get summary of epsrc network
    summary(epsrc)
    # set layout for plotting epsrc network
    layout = epsrc.layout("circular")
    # plot epsrc network
    plot(epsrc, layout=layout, bbox=(3000, 2000), margin=20, keep_aspect_ratio=True, edge_curved=True)


########################################################################################################################


# main function
def main():

    # analyse network using graphistry
    # graphistry_analysis()

    # analyse network using igraph
    igraph_analysis()


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
