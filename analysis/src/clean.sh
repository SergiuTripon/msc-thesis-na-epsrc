#!/usr/bin/env bash

########################################################################################################################

# cleans topics
function clean_topics() {

    # variables to hold methods
    method1='louvain'
    method2='spinglass'
    method3='fastgreedy'
    # variables to hold time periods
    time_period1='current'
    time_period2='past1'
    time_period3='past2'

    if [ $1 = 'a' ] && [ $2 = ${time_period1} ]; then
        clean_topics_a ${time_period1} ${method1}
        clean_topics_a ${time_period1} ${method2}
        clean_topics_a ${time_period1} ${method3}
    fi

    if [ $1 = 'a' ] && [ $2 = ${time_period2} ]; then
        clean_topics_a ${time_period2} ${method1}
        clean_topics_a ${time_period2} ${method2}
        clean_topics_a ${time_period2} ${method3}
    fi

    if [ $1 = 'a' ] && [ $2 = ${time_period3} ]; then
        clean_topics_a ${time_period3} ${method1}
        clean_topics_a ${time_period3} ${method2}
        clean_topics_a ${time_period3} ${method3}
    fi

    ####################################################################################################################

    if [ $1 = 'b' ] && [ $2 = ${time_period1} ]; then
        clean_topics_b ${time_period1} ${method1}
        clean_topics_b ${time_period1} ${method2}
        clean_topics_b ${time_period1} ${method3}
    fi

    if [ $1 = 'b' ] && [ $2 = ${time_period2} ]; then
        clean_topics_b ${time_period2} ${method1}
        clean_topics_b ${time_period2} ${method2}
        clean_topics_b ${time_period2} ${method3}
    fi

    if [ $1 = 'b' ] && [ $2 = ${time_period3} ]; then
        clean_topics_b ${time_period3} ${method1}
        clean_topics_b ${time_period3} ${method2}
        clean_topics_b ${time_period3} ${method3}
    fi

}

########################################################################################################################

# clean topics a
function clean_topics_a() {

    path1='topics/current/network-a'
    path2='topics/past/2000-2010/network-a'
    path3='topics/past/1990-2000/network-a'

    edge_type1='uw'
    edge_type2='wn'
    edge_type3='wv'
    edge_type4='wnn'
    edge_type5='wnv'

    method1='louvain'
    method2='spinglass'
    method3='fastgreedy'

    if [ $1 = "current" ] && [ $2 = "louvain" ]; then
        clean_folders ${path1} ${edge_type1} ${method1}
        clean_folders ${path1} ${edge_type2} ${method1}
        clean_folders ${path1} ${edge_type3} ${method1}
        clean_folders ${path1} ${edge_type4} ${method1}
        clean_folders ${path1} ${edge_type5} ${method1}
    fi

    if [ $1 = "current" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path1} ${edge_type1} ${method2}
        clean_folders ${path1} ${edge_type2} ${method2}
        clean_folders ${path1} ${edge_type3} ${method2}
        clean_folders ${path1} ${edge_type4} ${method2}
        clean_folders ${path1} ${edge_type5} ${method2}
    fi

    if [ $1 = "current" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path1} ${edge_type1} ${method3}
        clean_folders ${path1} ${edge_type2} ${method3}
        clean_folders ${path1} ${edge_type3} ${method3}
        clean_folders ${path1} ${edge_type4} ${method3}
        clean_folders ${path1} ${edge_type5} ${method3}
    fi

    ####################################################################################################################

    if [ $1 = "past1" ] && [ $2 = "louvain" ]; then
        clean_folders ${path2} ${edge_type1} ${method1}
        clean_folders ${path2} ${edge_type2} ${method1}
        clean_folders ${path2} ${edge_type3} ${method1}
        clean_folders ${path2} ${edge_type4} ${method1}
        clean_folders ${path2} ${edge_type5} ${method1}
    fi

    if [ $1 = "past1" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path2} ${edge_type1} ${method2}
        clean_folders ${path2} ${edge_type2} ${method2}
        clean_folders ${path2} ${edge_type3} ${method2}
        clean_folders ${path2} ${edge_type4} ${method2}
        clean_folders ${path2} ${edge_type5} ${method2}
    fi

    if [ $1 = "past1" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path2} ${edge_type1} ${method3}
        clean_folders ${path2} ${edge_type2} ${method3}
        clean_folders ${path2} ${edge_type3} ${method3}
        clean_folders ${path2} ${edge_type4} ${method3}
        clean_folders ${path2} ${edge_type5} ${method3}
    fi

    ####################################################################################################################

    if [ $1 = "past2" ] && [ $2 = "louvain" ]; then
        clean_folders ${path3} ${edge_type1} ${method1}
        clean_folders ${path3} ${edge_type2} ${method1}
        clean_folders ${path3} ${edge_type3} ${method1}
        clean_folders ${path3} ${edge_type4} ${method1}
        clean_folders ${path3} ${edge_type5} ${method1}
    fi

    if [ $1 = "past2" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path3} ${edge_type1} ${method2}
        clean_folders ${path3} ${edge_type2} ${method2}
        clean_folders ${path3} ${edge_type3} ${method2}
        clean_folders ${path3} ${edge_type4} ${method2}
        clean_folders ${path3} ${edge_type5} ${method2}
    fi

    if [ $1 = "past2" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path3} ${edge_type1} ${method3}
        clean_folders ${path3} ${edge_type2} ${method3}
        clean_folders ${path3} ${edge_type3} ${method3}
        clean_folders ${path3} ${edge_type4} ${method3}
        clean_folders ${path3} ${edge_type5} ${method3}
    fi
}

########################################################################################################################

# clean topics b
function clean_topics_b() {

    path1='topics/current/network-b'
    path2='topics/past/2000-2010/network-b'
    path3='topics/past/1990-2000/network-b'

    edge_type1='uw'
    edge_type2='wn'
    edge_type3='wnn'

    method1='louvain'
    method2='spinglass'
    method3='fastgreedy'

    if [ $1 = "current" ] && [ $2 = "louvain" ]; then
        clean_folders ${path1} ${edge_type1} ${method1}
        clean_folders ${path1} ${edge_type2} ${method1}
        clean_folders ${path1} ${edge_type3} ${method1}
    fi

    if [ $1 = "current" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path1} ${edge_type1} ${method2}
        clean_folders ${path1} ${edge_type2} ${method2}
        clean_folders ${path1} ${edge_type3} ${method2}
    fi

    if [ $1 = "current" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path1} ${edge_type1} ${method3}
        clean_folders ${path1} ${edge_type2} ${method3}
        clean_folders ${path1} ${edge_type3} ${method3}
    fi

    ####################################################################################################################

    if [ $1 = "past1" ] && [ $2 = "louvain" ]; then
        clean_folders ${path2} ${edge_type1} ${method1}
        clean_folders ${path2} ${edge_type2} ${method1}
        clean_folders ${path2} ${edge_type3} ${method1}
    fi

    if [ $1 = "past1" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path2} ${edge_type1} ${method2}
        clean_folders ${path2} ${edge_type2} ${method2}
        clean_folders ${path2} ${edge_type3} ${method2}
    fi

    if [ $1 = "past1" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path2} ${edge_type1} ${method3}
        clean_folders ${path2} ${edge_type2} ${method3}
        clean_folders ${path2} ${edge_type3} ${method3}
    fi

    ####################################################################################################################

    if [ $1 = "past2" ] && [ $2 = "louvain" ]; then
        clean_folders ${path3} ${edge_type1} ${method1}
        clean_folders ${path3} ${edge_type2} ${method1}
        clean_folders ${path3} ${edge_type3} ${method1}
    fi

    if [ $1 = "past2" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path3} ${edge_type1} ${method2}
        clean_folders ${path3} ${edge_type2} ${method2}
        clean_folders ${path3} ${edge_type3} ${method2}
    fi

    if [ $1 = "past2" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path3} ${edge_type1} ${method3}
        clean_folders ${path3} ${edge_type2} ${method3}
        clean_folders ${path3} ${edge_type3} ${method3}
    fi
}

########################################################################################################################

# cleans researchers
function clean_researchers() {

    # variables to hold methods
    method1='louvain'
    method2='spinglass'
    method3='fastgreedy'
    # variables to hold time periods
    time_period1='current'
    time_period2='past1'
    time_period3='past2'

    if [ $1 = 'a' ] && [ $2 = ${time_period1} ]; then
        clean_researchers_a ${time_period1} ${method1}
        clean_researchers_a ${time_period1} ${method2}
        clean_researchers_a ${time_period1} ${method3}
    fi

    if [ $1 = 'a' ] && [ $2 = ${time_period2} ]; then
        clean_researchers_a ${time_period2} ${method1}
        clean_researchers_a ${time_period2} ${method2}
        clean_researchers_a ${time_period2} ${method3}
    fi

    if [ $1 = 'a' ] && [ $2 = ${time_period3} ]; then
        clean_researchers_a ${time_period3} ${method1}
        clean_researchers_a ${time_period3} ${method2}
        clean_researchers_a ${time_period3} ${method3}
    fi

    ####################################################################################################################

    if [ $1 = 'b' ] && [ $2 = ${time_period1} ]; then
        clean_researchers_b ${time_period1} ${method1}
        clean_researchers_b ${time_period1} ${method2}
        clean_researchers_b ${time_period1} ${method3}
    fi

    if [ $1 = 'b' ] && [ $2 = ${time_period2} ]; then
        clean_researchers_b ${time_period2} ${method1}
        clean_researchers_b ${time_period2} ${method2}
        clean_researchers_b ${time_period2} ${method3}
    fi

    if [ $1 = 'b' ] && [ $2 = ${time_period3} ]; then
        clean_researchers_b ${time_period3} ${method1}
        clean_researchers_b ${time_period3} ${method2}
        clean_researchers_b ${time_period3} ${method3}
    fi

}

########################################################################################################################

# clean researchers a
function clean_researchers_a() {

    path1='researchers/current/network-a'
    path2='researchers/past/2000-2010/network-a'
    path3='researchers/past/1990-2000/network-a'

    edge_type1='uw'
    edge_type2='wn'
    edge_type3='wnn'

    method1='louvain'
    method2='spinglass'
    method3='fastgreedy'

    if [ $1 = "current" ] && [ $2 = "louvain" ]; then
        clean_folders ${path1} ${edge_type1} ${method1}
        clean_folders ${path1} ${edge_type2} ${method1}
        clean_folders ${path1} ${edge_type3} ${method1}
    fi

    if [ $1 = "current" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path1} ${edge_type1} ${method2}
        clean_folders ${path1} ${edge_type2} ${method2}
        clean_folders ${path1} ${edge_type3} ${method2}
    fi

    if [ $1 = "current" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path1} ${edge_type1} ${method3}
        clean_folders ${path1} ${edge_type2} ${method3}
        clean_folders ${path1} ${edge_type3} ${method3}
    fi

    ####################################################################################################################

    if [ $1 = "past1" ] && [ $2 = "louvain" ]; then
        clean_folders ${path2} ${edge_type1} ${method1}
        clean_folders ${path2} ${edge_type2} ${method1}
        clean_folders ${path2} ${edge_type3} ${method1}
    fi

    if [ $1 = "past1" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path2} ${edge_type1} ${method2}
        clean_folders ${path2} ${edge_type2} ${method2}
        clean_folders ${path2} ${edge_type3} ${method2}
    fi

    if [ $1 = "past1" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path2} ${edge_type1} ${method3}
        clean_folders ${path2} ${edge_type2} ${method3}
        clean_folders ${path2} ${edge_type3} ${method3}
    fi

    ####################################################################################################################

    if [ $1 = "past2" ] && [ $2 = "louvain" ]; then
        clean_folders ${path3} ${edge_type1} ${method1}
        clean_folders ${path3} ${edge_type2} ${method1}
        clean_folders ${path3} ${edge_type3} ${method1}
    fi

    if [ $1 = "past2" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path3} ${edge_type1} ${method2}
        clean_folders ${path3} ${edge_type2} ${method2}
        clean_folders ${path3} ${edge_type3} ${method2}
    fi

    if [ $1 = "past2" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path3} ${edge_type1} ${method3}
        clean_folders ${path3} ${edge_type2} ${method3}
        clean_folders ${path3} ${edge_type3} ${method3}
    fi

}

########################################################################################################################

# clean researchers b
function clean_researchers_b() {

    path1='researchers/current/network-b'
    path2='researchers/past/2000-2010/network-b'
    path3='researchers/past/1990-2000/network-b'

    edge_type1='uw'
    edge_type2='wn'
    edge_type3='wv'
    edge_type4='wnn'
    edge_type5='wnv'

    method1='louvain'
    method2='spinglass'
    method3='fastgreedy'

    if [ $1 = "current" ] && [ $2 = "louvain" ]; then
        clean_folders ${path1} ${edge_type1} ${method1}
        clean_folders ${path1} ${edge_type2} ${method1}
        clean_folders ${path1} ${edge_type3} ${method1}
        clean_folders ${path1} ${edge_type4} ${method1}
        clean_folders ${path1} ${edge_type5} ${method1}
    fi

    if [ $1 = "current" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path1} ${edge_type1} ${method2}
        clean_folders ${path1} ${edge_type2} ${method2}
        clean_folders ${path1} ${edge_type3} ${method2}
        clean_folders ${path1} ${edge_type4} ${method2}
        clean_folders ${path1} ${edge_type5} ${method2}
    fi

    if [ $1 = "current" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path1} ${edge_type1} ${method3}
        clean_folders ${path1} ${edge_type2} ${method3}
        clean_folders ${path1} ${edge_type3} ${method3}
        clean_folders ${path1} ${edge_type4} ${method3}
        clean_folders ${path1} ${edge_type5} ${method3}
    fi

    ####################################################################################################################

    if [ $1 = "past1" ] && [ $2 = "louvain" ]; then
        clean_folders ${path2} ${edge_type1} ${method1}
        clean_folders ${path2} ${edge_type2} ${method1}
        clean_folders ${path2} ${edge_type3} ${method1}
        clean_folders ${path2} ${edge_type4} ${method1}
        clean_folders ${path2} ${edge_type5} ${method1}
    fi

    if [ $1 = "past1" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path2} ${edge_type1} ${method2}
        clean_folders ${path2} ${edge_type2} ${method2}
        clean_folders ${path2} ${edge_type3} ${method2}
        clean_folders ${path2} ${edge_type4} ${method2}
        clean_folders ${path2} ${edge_type5} ${method2}
    fi

    if [ $1 = "past1" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path2} ${edge_type1} ${method3}
        clean_folders ${path2} ${edge_type2} ${method3}
        clean_folders ${path2} ${edge_type3} ${method3}
        clean_folders ${path2} ${edge_type4} ${method3}
        clean_folders ${path2} ${edge_type5} ${method3}
    fi

    ####################################################################################################################

    if [ $1 = "past2" ] && [ $2 = "louvain" ]; then
        clean_folders ${path3} ${edge_type1} ${method1}
        clean_folders ${path3} ${edge_type2} ${method1}
        clean_folders ${path3} ${edge_type3} ${method1}
        clean_folders ${path3} ${edge_type4} ${method1}
        clean_folders ${path3} ${edge_type5} ${method1}
    fi

    if [ $1 = "past2" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path3} ${edge_type1} ${method2}
        clean_folders ${path3} ${edge_type2} ${method2}
        clean_folders ${path3} ${edge_type3} ${method2}
        clean_folders ${path3} ${edge_type4} ${method2}
        clean_folders ${path3} ${edge_type5} ${method2}
    fi

    if [ $1 = "past2" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path3} ${edge_type1} ${method3}
        clean_folders ${path3} ${edge_type2} ${method3}
        clean_folders ${path3} ${edge_type3} ${method3}
        clean_folders ${path3} ${edge_type4} ${method3}
        clean_folders ${path3} ${edge_type5} ${method3}
    fi

}

########################################################################################################################

# cleans folders
function clean_folders() {

    # delete network stats file
    rm -rf ../../data/networks/$1/network/txt/$2/$3/stats.txt
    # delete network modularity file
    rm -rf ../../data/networks/$1/network/txt/$2/$3/modularity.txt
        # delete network robustness file
    rm -rf ../../data/networks/$1/network/txt/$2/$3/robustness.txt
    # delete network plot file
    rm -rf ../../data/networks/$1/network/png/$2/$3/network.png

    ####################################################################################################################

    # delete community modularity file
    rm -rf ../../data/networks/$1/communities/txt/$2/$3/modularity*.txt

    # delete community network files
    rm -rf ../../data/networks/$1/communities/graphml/$2/$3/community*.graphml

    # delete community numbers file
    rm -rf ../../data/networks/$1/communities/txt/$2/$3/numbers*.txt

    # delete community grants file
    rm -rf ../../data/networks/$1/communities/txt/$2/$3/grants*.txt

    # delete community membership network file
    rm -rf ../../data/networks/$1/network/graphml/$2/$3/membership*.graphml

    # delete community topics file file
    rm -rf ../../data/networks/$1/communities/txt/$2/$3/topics*.txt

    # delete community overview plot file
    rm -rf ../../data/networks/$1/communities/png/$2/$3/overview1*.png

    # delete community overview plot file
    rm -rf ../../data/networks/$1/communities/png/$2/$3/overview2*.png

    # delete communities plot files
    rm -rf ../../data/networks/$1/communities/png/$2/$3/community*.png

####################################################################################################################

    # delete sub-community network files
    rm -rf ../../data/networks/$1/sub-communities/graphml/$2/$3/community*.graphml

    # delete sub-community stats files
    rm -rf ../../data/networks/$1/sub-communities/txt/$2/$3/numbers*.txt

    # delete sub-community grants files
    rm -rf ../../data/networks/$1/sub-communities/txt/$2/$3/grants*.txt

    # delete sub-community membership network files
    rm -rf ../../data/networks/$1/communities/graphml/$2/$3/membership*.graphml

    # delete sub-community topics files
    rm -rf ../../data/networks/$1/sub-communities/txt/$2/$3/topics*.txt

    # delete sub-community overview plot file
    rm -rf ../../data/networks/$1/sub-communities/png/$2/$3/overview1*.png

    # delete sub-community overview plot file
    rm -rf ../../data/networks/$1/sub-communities/png/$2/$3/overview2*.png

    ####################################################################################################################

    echo "> Folders cleaned ($1/$2/$3)."

}

########################################################################################################################

# clean topics
# clean_topics 'a' 'current'
# clean_topics 'a' 'past1'
# clean_topics 'a' 'past2'

# clean_topics 'b' 'current'
clean_topics 'b' 'past1'
# clean_topics 'b' 'past2'

# clean researchers
# clean_researchers 'a' 'current'
# clean_researchers 'a' 'past1'
# clean_researchers 'a' 'past2'

# clean_researchers 'b' 'current'
# clean_researchers 'b' 'past1'
# clean_researchers 'b' 'past2'