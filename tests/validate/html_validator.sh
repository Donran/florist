#!/bin/bash

# Make sure a argument is provided for files to validate
if [ "$1" == "" ]; then
    echo -e "Please provide the root folder as such:\n\t$0 public"
    exit
fi

# Find all files ending in .html to be validated
for i in $(find $1 -iname '*.html'); do
    # Send a request to the w3 API for validating HTML
    # Retrun data is in JSON format
    data=`curl -s -H "Content-Type: text/html" \
    --data-binary @$i \
    https://validator.w3.org/nu/?out=json \
    \;` 
    if [[ $data == *"type"* ]]; then
        # If the result data contains the text "type", an error occured
        # print this error and return 1 as exit status
        echo "Filename: $ei"
        echo $data | jq .
	    echo "Error in validation."
        exit 1
    fi

    echo "Test passed"
done
# Everything passed, return 0 as exit status
exit 0
