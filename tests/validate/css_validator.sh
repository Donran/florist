#!/bin/bash

# Constant for the mssage return if no errors occured
if [ "$1" == "" ]; then
    echo -e "Please provide the root folder as such\n\t$0 public"
    exit
fi

# Go through all files ending in .css
for file in $(find $1 -iname '*.css'); do
    # Send a request to the w3 API for validating CSS
    # files need to be submitted as a multipart/form-data
    # Select the css3 profile and output as text/plain
    data=`curl -s -H "Content-Type: multipart/form-data" \
        -F "text=<$file;type=text/plain" \
        -F "profile=css3" \
        -F "output=json" \
        https://jigsaw.w3.org/css-validator/validator`
    json=`jq .cssvalidation <<< "$data"`
    # Check if any errors occured
    error_count=`echo $json | jq .result.errorcount`
    if [ "$error_count" = "0" ]; then
        echo "Success for $file"
    else
        # If errors are found, print them.
        echo "Errors:"
        for i in $(seq 0 `expr $error_count - "1"`); do
            error=`echo $json | jq .errors[$i]`
            echo "$(echo $error | jq -r .context): L$(echo $error | jq -r .line) {type: $(echo $error | jq -r .type)}"
            echo -e "\t $(echo $error | jq -r .message)"
        done
        exit 1
    fi
done
exit 0
