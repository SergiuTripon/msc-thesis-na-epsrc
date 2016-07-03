#!/usr/bin/env bash

########################################################################################################################

# downloads topics
function download_topics {
    # if topics folder does not exist
    if [ ! -d ../output/topics/html/topics/ ]; then
        # variable to hold start date and time
        start=$(date "+%d-%m-%Y %H:%M:%S")
        # print start
        echo "> Start date and time: ${start}"

        # variable to hold source
        source=../output/topics/html/topics/
        # variable to hold target
        target=../output/topics/urls/topics.txt
        # download pages at the topic urls in the file
        xargs -P 20 -n 1 wget -q --directory-prefix=${source} < ${target}

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
    if [ ! -d ../output/topics/html/grants/ ]; then
        # variable to hold start date and time
        start=$(date "+%d-%m-%Y %H:%M:%S")
        # print start
        echo "> Start date and time: ${start}"

        # variable to hold source
        source=../output/topics/html/grants/
        # variable to hold target
        target=../output/topics/urls/grants.txt
        # download pages at the grant urls in the file
        xargs -P 20 -n 1 wget -q --directory-prefix=${source} < ${target}

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
    if [ ! -d ../output/topics/html/researchers/ ]; then
        # variable to hold start date and time
        start=$(date "+%d-%m-%Y %H:%M:%S")
        # print start
        echo "> Start date and time: ${start}"

        # variable to hold source
        source=../output/topics/html/researchers/
        # variable to hold target
        target=../output/topics/urls/researchers.txt
        # download pages at the researcher urls in the file
        xargs -P 20 -n 1 wget -q --directory-prefix=${source} < ${target}

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
    if [ ! -d ../output/past-topics/html/grants$1/ ]; then
        # variable to hold start date and time
        start=$(date "+%d-%m-%Y %H:%M:%S")
        # print start
        echo "> Start date and time: ${start}"

        # variable to hold source
        source=../output/past-topics/html/grants$1/
        # variable to hold target
        target=../output/past-topics/urls/grants$1.txt
        # download pages at the grant urls in the file
        xargs -P 20 -n 1 wget -q --directory-prefix=${source} < ${target}

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
    if [ ! -d ../output/past-topics/html/researchers$1/ ]; then
        # variable to hold start date and time
        start=$(date "+%d-%m-%Y %H:%M:%S")
        # print start
        echo "> Start date and time: ${start}"

        # variable to hold source
        source=../output/past-topics/html/researchers$1/
        # variable to hold target
        target=../output/past-topics/urls/researchers$1.txt
        # download pages at the researcher urls in the file
        xargs -P 20 -n 1 wget -q --directory-prefix=${source} < ${target}

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

# years='_1990_2000'
years='_2000_2010'
# download past grants
download_past_grants ${years}
# download past researchers
download_past_researchers ${years}

########################################################################################################################

: '
# variable to hold start date and time
start=$(date "+%d-%m-%Y %H:%M:%S")
# print start
echo "> Start date and time: ${start}"

########################################################################################################################

# if topics page does not exist
if [ ! -f ../output/topics/html/topics/NGBOListTopics.aspx ]; then
    # download topics page
    wget -q --directory-prefix=../output/topics/html/topics/ http://gow.epsrc.ac.uk/NGBOListTopics.aspx
    # print progress
    echo "> Downloaded topics web page (${topic_url})."
# close if statement
fi

########################################################################################################################

# if topics folder does not exist
if [ ! -d ../output/topics/html/topics/ ]; then
    # load topic urls file into topic urls array
    readarray -t topic_urls < ../output/topics/urls/topics.txt
    # variable to hold topic url count set to 1
    topic_url_count=1
    # for topic url in topic urls
    for topic_url in ${topic_urls[@]};
    # download page at topic url
    do wget -q --directory-prefix=../output/topics/html/topics/ ${topic_url};
    # print progress
    echo "> Downloaded ${topic_url_count} topic web page(s) (${topic_url})."
    # increment topic url count
    topic_url_count=$[$topic_url_count+1]
    # done
    done
# close if statement
fi

# print empty row
echo ""

# if grants folder does not exist
if [ ! -d ../output/topics/html/grants/ ]; then
    # load grant urls file into grant urls array
    readarray -t grant_urls < ../output/topics/urls/grants.txt
    # variable to hold grant url count set to 1
    grant_url_count=1
    # for grant url in grant urls
    for grant_url in ${grant_urls[@]};
    # download page at grant url
    do wget -q --directory-prefix=../output/topics/html/grants/ ${grant_url};
    # print progress
    echo "> Downloaded ${grant_url_count} grant web page(s) (${grant_url})."
    # increment grant url count
    grant_url_count=$[$grant_url_count+1]
    # done
    done
# close if statement
fi

########################################################################################################################

# variable to hold end date and time
end=$(date "+%d-%m-%Y %H:%M:%S")
# print end
echo "> End date and time: ${end}"

########################################################################################################################

# variable to hold duration
duration=$((end-start))
# print duration
echo "> Total duration of script execution: ${duration}"

########################################################################################################################
'