#!/usr/bin/env bash

########################################################################################################################

# if topics folder does not exist
if [ ! -d ../output/topics/html/topics/ ]; then
    # variable to hold start date and time
    start=$(date "+%d-%m-%Y %H:%M:%S")
    # print start
    echo "> Start date and time: ${start}"

    # download pages at the topic urls in the file
    xargs -P 20 -n 1 wget -bqc --directory-prefix=../output/topics/html/topics/ < ../output/topics/urls/topics.txt

    # variable to hold end date and time
    end=$(date "+%d-%m-%Y %H:%M:%S")
    # print end
    echo "> End date and time: ${end}"
# close if statement
fi

########################################################################################################################

# if grants folder does not exist
if [ ! -d ../output/topics/html/grants/ ]; then
    # variable to hold start date and time
    start=$(date "+%d-%m-%Y %H:%M:%S")
    # print start
    echo "> Start date and time: ${start}"

    # download pages at the grant urls in the file
    xargs -P 20 -n 1 wget -bqc --directory-prefix=../output/topics/html/grants/ < ../output/topics/urls/grants.txt

    # variable to hold end date and time
    end=$(date "+%d-%m-%Y %H:%M:%S")
    # print end
    echo "> End date and time: ${end}"
# close if statement
fi

########################################################################################################################

# if grants folder does not exist
if [ ! -d ../output/past-topics/html/grants/ ]; then
    # variable to hold start date and time
    start=$(date "+%d-%m-%Y %H:%M:%S")
    # print start
    echo "> Start date and time: ${start}"

    # download pages at the grant urls in the file
    xargs -P 20 -n 1 wget -bqc --directory-prefix=../output/past-topics/html/grants/ < ../output/past-topics/urls/grants.txt

    # variable to hold end date and time
    end=$(date "+%d-%m-%Y %H:%M:%S")
    # print end
    echo "> End date and time: ${end}"
# close if statement
fi

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