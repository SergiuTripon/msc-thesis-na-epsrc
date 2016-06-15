#!/usr/bin/env python3

########################################################################################################################

# third-party library modules
from igraph import *

########################################################################################################################


# experiments with igraph
def igraph_analysis():

    '''
    g = Graph()
    g.add_vertices(3)
    g.add_edges([(0, 1), (1, 2)])
    g.add_edges([(2, 0)])
    g.add_vertices(3)
    g.add_edges([(2, 3), (3, 4), (4, 5), (5, 3)])
    print(g)
    print(g.get_eid(2, 3))
    g.delete_edges(3)
    print(g)
    '''

    '''
    g = Graph.Tree(127, 2)
    summary(g)
    g2 = Graph.Tree(127, 2)
    print(g2.get_edgelist() == g.get_edgelist())
    print(g2.get_edgelist()[0:10])

    g = Graph.GRG(100, 0.2)
    summary(g)
    g2 = Graph.GRG(100, 0.2)
    print(g2.get_edgelist() == g.get_edgelist())
    print(g.isomorphic(g2))
    '''

    g = Graph([(0, 1), (0, 2), (2, 3), (3, 4), (4, 2), (2, 5), (5, 0), (6, 3), (5, 6)])

    g.vs["name"] = ["Alice", "Bob", "Claire", "Dennis", "Esther", "Frank", "George"]
    g.vs["age"] = [25, 31, 18, 47, 22, 23, 50]
    g.vs["gender"] = ["f", "m", "f", "m", "f", "m", "m"]
    g.es["is_formal"] = [False, False, True, True, True, False, True, False, False]

    g["date"] = "2009-01-10"
    print(g["date"])

    print(g.degree())
    print(g.degree(6))
    print(g.degree([2, 3, 4]))

    print(g.edge_betweenness())
    ebs = g.edge_betweenness()
    max_eb = max(ebs)
    print([g.es[idx].tuple for idx, eb in enumerate(ebs) if eb == max_eb])

    print(g.vs.degree())
    print(g.es.edge_betweenness())
    print(g.vs[2].degree())
    print(g.vs.select(_degree=g.maxdegree())["name"])
    print(g.vs(age_lt=30)["name"])

    layout = g.layout("fr")
    g.vs["label"] = g.vs["name"]
    color_dict = {"m": "blue", "f": "pink"}
    g.vs["color"] = [color_dict[gender] for gender in g.vs["gender"]]
    plot(g, layout=layout, bbox=(300, 300), margin=20)


########################################################################################################################


# main function
def main():

    # experiment with igraph
    igraph_analysis()


########################################################################################################################


# runs main function
if __name__ == '__main__':
    main()


########################################################################################################################
