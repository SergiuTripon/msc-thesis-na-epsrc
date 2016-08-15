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

    if [ $1 = "current" ] && [ $2 = "louvain" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
        clean_folders ${path1} ${edge_type4} $2
        clean_folders ${path1} ${edge_type5} $2
    fi

    if [ $1 = "current" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
        clean_folders ${path1} ${edge_type4} $2
        clean_folders ${path1} ${edge_type5} $2
    fi

    if [ $1 = "current" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
        clean_folders ${path1} ${edge_type4} $2
        clean_folders ${path1} ${edge_type5} $2
    fi

    ####################################################################################################################

    if [ $1 = "past1" ] && [ $2 = "louvain" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
        clean_folders ${path2} ${edge_type4} $2
        clean_folders ${path2} ${edge_type5} $2
    fi

    if [ $1 = "past1" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
        clean_folders ${path2} ${edge_type4} $2
        clean_folders ${path2} ${edge_type5} $2
    fi

    if [ $1 = "past1" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
        clean_folders ${path2} ${edge_type4} $2
        clean_folders ${path2} ${edge_type5} $2
    fi

    ####################################################################################################################

    if [ $1 = "past2" ] && [ $2 = "louvain" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
        clean_folders ${path3} ${edge_type4} $2
        clean_folders ${path3} ${edge_type5} $2
    fi

    if [ $1 = "past2" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
        clean_folders ${path3} ${edge_type4} $2
        clean_folders ${path3} ${edge_type5} $2
    fi

    if [ $1 = "past2" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
        clean_folders ${path3} ${edge_type4} $2
        clean_folders ${path3} ${edge_type5} $2
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

    if [ $1 = "current" ] && [ $2 = "louvain" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
    fi

    if [ $1 = "current" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
    fi

    if [ $1 = "current" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
    fi

    ####################################################################################################################

    if [ $1 = "past1" ] && [ $2 = "louvain" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
    fi

    if [ $1 = "past1" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
    fi

    if [ $1 = "past1" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
    fi

    ####################################################################################################################

    if [ $1 = "past2" ] && [ $2 = "louvain" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
    fi

    if [ $1 = "past2" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
    fi

    if [ $1 = "past2" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
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

    if [ $1 = "current" ] && [ $2 = "louvain" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
    fi

    if [ $1 = "current" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
    fi

    if [ $1 = "current" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
    fi

    ####################################################################################################################

    if [ $1 = "past1" ] && [ $2 = "louvain" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
    fi

    if [ $1 = "past1" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
    fi

    if [ $1 = "past1" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
    fi

    ####################################################################################################################

    if [ $1 = "past2" ] && [ $2 = "louvain" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
    fi

    if [ $1 = "past2" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
    fi

    if [ $1 = "past2" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
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

    if [ $1 = "current" ] && [ $2 = "louvain" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
        clean_folders ${path1} ${edge_type4} $2
        clean_folders ${path1} ${edge_type5} $2
    fi

    if [ $1 = "current" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
        clean_folders ${path1} ${edge_type4} $2
        clean_folders ${path1} ${edge_type5} $2
    fi

    if [ $1 = "current" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path1} ${edge_type1} $2
        clean_folders ${path1} ${edge_type2} $2
        clean_folders ${path1} ${edge_type3} $2
        clean_folders ${path1} ${edge_type4} $2
        clean_folders ${path1} ${edge_type5} $2
    fi

    ####################################################################################################################

    if [ $1 = "past1" ] && [ $2 = "louvain" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
        clean_folders ${path2} ${edge_type4} $2
        clean_folders ${path2} ${edge_type5} $2
    fi

    if [ $1 = "past1" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
        clean_folders ${path2} ${edge_type4} $2
        clean_folders ${path2} ${edge_type5} $2
    fi

    if [ $1 = "past1" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path2} ${edge_type1} $2
        clean_folders ${path2} ${edge_type2} $2
        clean_folders ${path2} ${edge_type3} $2
        clean_folders ${path2} ${edge_type4} $2
        clean_folders ${path2} ${edge_type5} $2
    fi

    ####################################################################################################################

    if [ $1 = "past2" ] && [ $2 = "louvain" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
        clean_folders ${path3} ${edge_type4} $2
        clean_folders ${path3} ${edge_type5} $2
    fi

    if [ $1 = "past2" ] && [ $2 = "spinglass" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
        clean_folders ${path3} ${edge_type4} $2
        clean_folders ${path3} ${edge_type5} $2
    fi

    if [ $1 = "past2" ] && [ $2 = "fastgreedy" ]; then
        clean_folders ${path3} ${edge_type1} $2
        clean_folders ${path3} ${edge_type2} $2
        clean_folders ${path3} ${edge_type3} $2
        clean_folders ${path3} ${edge_type4} $2
        clean_folders ${path3} ${edge_type5} $2
    fi

}

########################################################################################################################

# cleans folders
function clean_folders() {

    # clean network graphml folder
    rm -rf ../../data/networks/$1/network/graphml/$2/$3/*

    # clean network png folder
    rm -rf ../../data/networks/$1/network/png/$2/$3/*

    # clean network txt folder
    rm -rf ../../data/networks/$1/network/txt/$2/$3/*

    ####################################################################################################################

    # clean communities graphml folder
    rm -rf ../../data/networks/$1/communities/graphml/$2/$3/*

    # clean communities png folder
    rm -rf ../../data/networks/$1/communities/png/$2/$3/*

    # clean communities txt folder
    rm -rf ../../data/networks/$1/communities/txt/$2/$3/*

    ####################################################################################################################

    # clean sub-communities graphml folder
    rm -rf ../../data/networks/$1/sub-communities/graphml/$2/$3/*

    # clean sub-communities png folder
    rm -rf ../../data/networks/$1/sub-communities/png/$2/$3/*

    # clean sub-communities txt folder
    rm -rf ../../data/networks/$1/sub-communities/txt/$2/$3/*

    ####################################################################################################################

    echo "> Folders cleaned ($1/$2/$3)."

}

########################################################################################################################

# clean topics
# clean_topics 'a' 'current'
# clean_topics 'a' 'past1'
# clean_topics 'a' 'past2'

# clean_topics 'b' 'current'
# clean_topics 'b' 'past1'
# clean_topics 'b' 'past2'

# clean researchers
clean_researchers 'a' 'current'
clean_researchers 'a' 'past1'
clean_researchers 'a' 'past2'

clean_researchers 'b' 'current'
clean_researchers 'b' 'past1'
clean_researchers 'b' 'past2'