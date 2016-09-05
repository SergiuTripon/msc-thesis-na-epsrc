#!/usr/bin/env bash

########################################################################################################################

# downloads topics
function download_topics {
    # if topics folder does not exist
    if [ ! -d ../output/topics/current/html/ ]; then
        # variable to hold start date and time
        start=$(date "+%d-%m-%Y %H:%M:%S")
        # print start
        echo "> Start date and time: ${start}"

        # variable to hold source
        source=../output/topics/current/urls/topics.txt
        # variable to hold target
        target=../output/topics/current/html/
        # download pages at the topic urls in the file
        xargs -P 20 -n 1 wget -q --directory-prefix=${target} < ${source}

        # variable to hold end date and time
        end=$(date "+%d-%m-%Y %H:%M:%S")
        # print end
        echo "> End date and time: ${end}"
    # close if statement
    fi
}

########################################################################################################################

# downloads grants
function download_grants {
    # if grants folder does not exist
    if [ ! -d ../output/grants/current/html/ ]; then
        # variable to hold start date and time
        start=$(date "+%d-%m-%Y %H:%M:%S")
        # print start
        echo "> Start date and time: ${start}"

        # variable to hold source
        source=../output/grants/current/urls/grants.txt
        # variable to hold target
        target=../output/grants/current/html/
        # download pages at the grant urls in the file
        xargs -P 20 -n 1 wget -q --directory-prefix=${target} < ${source}

        # variable to hold end date and time
        end=$(date "+%d-%m-%Y %H:%M:%S")
        # print end
        echo "> End date and time: ${end}"
    # close if statement
    fi
}

########################################################################################################################

# downloads researchers
function download_researchers() {
    # if researchers folder does not exist
    if [ ! -d ../output/researchers/current/html/ ]; then
        # variable to hold start date and time
        start=$(date "+%d-%m-%Y %H:%M:%S")
        # print start
        echo "> Start date and time: ${start}"

        # variable to hold source
        source=../output/researchers/current/urls/researchers.txt
        # variable to hold target
        target=../output/researchers/current/html/
        # download pages at the researcher urls in the file
        xargs -P 20 -n 1 wget -q --directory-prefix=${target} < ${source}

        # variable to hold end date and time
        end=$(date "+%d-%m-%Y %H:%M:%S")
        # print end
        echo "> End date and time: ${end}"
    # close if statement
    fi
}

########################################################################################################################

# downloads past grants
function download_past_grants() {
    # if grants folder does not exist
    if [ ! -d ../output/grants/past/$1/html/ ]; then
        # variable to hold start date and time
        start=$(date "+%d-%m-%Y %H:%M:%S")
        # print start
        echo "> Start date and time: ${start}"

        # variable to hold source
        source=../output/past-topics/urls/grants$1.txt
        # variable to hold target
        target=../output/grants/past/$1/html/
        # download pages at the grant urls in the file
        xargs -P 20 -n 1 wget -q --directory-prefix=${target} < ${source}

        # variable to hold end date and time
        end=$(date "+%d-%m-%Y %H:%M:%S")
        # print end
        echo "> End date and time: ${end}"
    # close if statement
    fi
}

########################################################################################################################

# downloads past researchers
function download_past_researchers() {
    # if researchers folder does not exist
    if [ ! -d ../output/researchers/past/$1/html/ ]; then
        # variable to hold start date and time
        start=$(date "+%d-%m-%Y %H:%M:%S")
        # print start
        echo "> Start date and time: ${start}"

        # variable to hold source
        source=../output/past-topics/urls/researchers$1.txt
        # variable to hold target
        target=../output/researchers/past/$1/html/
        # download pages at the researcher urls in the file
        xargs -P 20 -n 1 wget -q --directory-prefix=${target} < ${source}

        # variable to hold end date and time
        end=$(date "+%d-%m-%Y %H:%M:%S")
        # print end
        echo "> End date and time: ${end}"
    # close if statement
    fi
}

########################################################################################################################

# run functions

# download topics
download_topics
# download grants
download_grants
# download researchers
download_researchers

# download past grants
download_past_grants '1990-2000'
download_past_grants '2000-2010'

# download past researchers
download_past_researchers '1990-2000'
download_past_researchers '2000-2010'

########################################################################################################################
