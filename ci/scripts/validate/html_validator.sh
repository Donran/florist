#!/bin/bash

if [ "$1" == "" ]; then
    echo -e "Please provide the root folder as such:\n\t$0 public"
    exit
fi
for i in $(find $1 -iname '*.html'); do
    data=`curl -s -H "Content-Type: text/html" \
    --data-binary @$i \
    https://validator.w3.org/nu/?out=json \
    \;` 
    if [[ $data == *"type"* ]]; then
        echo "Filename: $ei"
        echo $data | jq .
	    echo "Error in validation."
        exit 1
    fi

    echo "Test passed"
done
exit 0