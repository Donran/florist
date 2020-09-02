#!/bin/bash

# Constant for the message return if no errors occured
SUCCESS_MSG="No Error Found."


# Make sure a directory to look in is provided
if [ "$1" == "" ]; then
    echo -e "Please provide the root folder as such:\n\t$0 public"
    exit
fi

# Go through all files ending in .css 
for i in $(find $1 -iname '*.css'); do
    # Send a request to the w3 API for validating CSS
    # files need to be submitted as a multipart/form-data
    # Select the css3 profile and output as text/plain 
    data=`curl -s -H "Content-Type: multipart/form-data" \
        -F "text=<$i;type=text/plain" \
        -F "profile=css3" \
        -F "output=text/plain" \
            https://jigsaw.w3.org/css-validator/validator`
    # If we find SUCCESS_MSG the file is valid
    if echo $data | grep -q "$SUCCESS_MSG"; then
        echo "Success for $i"
    else
        # If the file is not valid, print all errors provided
        echo "Found errors in file $i"
        errors=$(echo $data | cut -c 112-)
        IFS=':' read -ra err_arr <<< "$errors"
        
        # Print all errors        
        for err in "${err_arr[@]}"
        do
            if [ "$err" == " Line " ]; then
                echo "=============================="
            else
                echo "$err"
            fi
        done

        echo "=============================="
        # Return 1 as exit status because an error occured
        exit 1
    fi

done
exit 0

