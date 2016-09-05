#!/usr/bin/env bash

########################################################################################################################

# gets grants stats
function get_grants_stats() {
    echo "Grants Stats ($1)"
    echo "URLs:" $(wc -l < ../output/grants/$2/urls/grants.txt)
    echo "Grant Researchers:" $(wc -l < ../output/grants/$2/info/grant_researchers.csv)
    echo "Grant Topics:" $(wc -l < ../output/grants/$2/info/grant_topics.csv)

    echo ""
}

########################################################################################################################

# gets topics stats
function get_topics_stats() {
    echo "Topics Stats ($1)"
    echo "Grant Topic Info:" $(wc -l < ../output/topics/$2/info/grant_topic_info.csv)
    echo "Researcher Topic Info:" $(wc -l < ../output/topics/$2/info/researcher_topic_info.csv)
    echo "Grant Topic Links": $(wc -l < ../output/topics/$2/links/grant_topic_links.csv)
    echo "Researcher Topic Links": $(wc -l < ../output/topics/$2/links/researcher_topic_links.csv)

    echo ""
}

########################################################################################################################

# gets researchers stats
function get_researchers_stats() {
    echo "Researchers Stats ($1)"
    echo "URLs:" $(wc -l < ../output/researchers/$2/urls/researchers.txt)
    echo "Grant Researcher Info:" $(wc -l < ../output/researchers/$2/info/grant_researcher_info.csv)
    echo "Researcher Info:" $(wc -l < ../output/researchers/$2/info/researcher_info.csv)
    echo "Researcher Topics:" $(wc -l < ../output/researchers/$2/info/researcher_topics.csv)
    echo "Researcher Links": $(wc -l < ../output/researchers/$2/links/researcher_links.csv)
    echo "Grant Researcher Links": $(wc -l < ../output/researchers/$2/links/grant_researcher_links.csv)

    echo ""
}

########################################################################################################################

# gets topic network a stats
function get_topic_network_a_stats() {
    echo "Research Topic-based Network A ($1)"
    echo "Topics: " $(wc -l < ../output/topics/$2/info/grant_topic_info.csv)
    echo "Nodes: " $(wc -l < ../../data/networks/topics/$2/network-a/network/tsv/nodes.tsv)
    echo "Links: " $(wc -l < ../output/topics/$2/links/grant_topic_links.csv)
    echo "Edges: " $(wc -l < ../../data/networks/topics/$2/network-a/network/tsv/edges.tsv)

    echo ""
}

########################################################################################################################

# gets topic network b stats
function get_topic_network_b_stats() {
    echo "Research Topic-based Network B ($1)"
    echo "Topics: " $(wc -l < ../output/topics/$2/info/researcher_topic_info.csv)
    echo "Nodes: " $(wc -l < ../../data/networks/topics/$2/network-b/network/tsv/nodes.tsv)
    echo "Links: " $(wc -l < ../output/topics/$2/links/researcher_topic_links.csv)
    echo "Edges: " $(wc -l < ../../data/networks/topics/$2/network-b/network/tsv/edges.tsv)

    echo ""
}

########################################################################################################################

# gets researcher network a stats
function get_researcher_network_a_stats() {
    echo "Researcher-based Network A ($1)"
    echo "Researchers: " $(wc -l < ../output/researchers/$2/info/researcher_info.csv)
    echo "Nodes: " $(wc -l < ../../data/networks/researchers/$2/network-a/network/tsv/nodes.tsv)
    echo "Links: " $(wc -l < ../output/researchers/$2/links/researcher_links.csv)
    echo "Edges: " $(wc -l < ../../data/networks/researchers/$2/network-a/network/tsv/edges.tsv)

    echo ""
}

########################################################################################################################

# gets researcher network b stats
function get_researcher_network_b_stats() {
    echo "Researcher-based Network B ($1)"
    echo "Researchers: " $(wc -l < ../output/researchers/$2/info/grant_researcher_info.csv)
    echo "Nodes: " $(wc -l < ../../data/networks/researchers/$2/network-b/network/tsv/nodes.tsv)
    echo "Links: " $(wc -l < ../output/researchers/$2/links/grant_researcher_links.csv)
    echo "Edges: " $(wc -l < ../../data/networks/researchers/$2/network-b/network/tsv/edges.tsv)

    echo ""
}

########################################################################################################################

# get grants stats
# get_grants_stats 'Current' 'current'
# get_grants_stats '1990-2000' 'past/1990-2000'
# get_grants_stats '2000-2010' 'past/2000-2010'

# get topics stats
# get_topics_stats 'Current' 'current'
# get_topics_stats '1990-2000' 'past/1990-2000'
# get_topics_stats '2000-2010' 'past/2000-2010'

# get researchers stats
# get_researchers_stats 'Current' 'current'
# get_researchers_stats '1990-2000' 'past/1990-2000'
# get_researchers_stats '2000-2010' 'past/2000-2010'

# get topic network a stats
get_topic_network_a_stats 'Current' 'current'
get_topic_network_a_stats '1990-2000' 'past/1990-2000'
get_topic_network_a_stats '2000-2010' 'past/2000-2010'

# get topic network b stats
get_topic_network_b_stats 'Current' 'current'
get_topic_network_b_stats '1990-2000' 'past/1990-2000'
get_topic_network_b_stats '2000-2010' 'past/2000-2010'

# get researcher network a stats
get_researcher_network_a_stats 'Current' 'current'
get_researcher_network_a_stats '1990-2000' 'past/1990-2000'
get_researcher_network_a_stats '2000-2010' 'past/2000-2010'

# get researcher network b stats
get_researcher_network_b_stats 'Current' 'current'
get_researcher_network_b_stats '1990-2000' 'past/1990-2000'
get_researcher_network_b_stats '2000-2010' 'past/2000-2010'
