#!/bin/bash

SUCCESS_MSG="No Error Found."

if [ "$1" == "" ]; then
    echo -e "Please provide the root folder as such:\n\t$0 public"
    exit
fi

for i in $(find $1 -iname '*.css'); do
    echo "trying $i"
    data=`curl -s -H "Content-Type: multipart/form-data" \
        -F "text=<$i;type=text/plain" \
        -F "profile=css3" \
        -F "output=text/plain" \
            https://jigsaw.w3.org/css-validator/validator`
    if echo $data | grep -q "$SUCCESS_MSG"; then
        echo "Success for $i"
    else
        echo "Found errors in file $i"
        errors=$(echo $data | cut -c 112-)
        IFS=':' read -ra err_arr <<< "$errors"
                
        for err in "${err_arr[@]}"
        do
            if [ "$err" == " Line " ]; then
                echo "=============================="
            else
                echo "$err"
            fi
        done

        echo "=============================="
        exit 1
    fi

done
exit 0

