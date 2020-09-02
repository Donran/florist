#!/bin/bash

if [ "$1" == "" ]; then
    echo -e "Please provide the root folder as such:\n\t$0 public"
    exit
fi

for i in $(find $1 -iname '*.css'); do
    formatted_file_name=$(echo $i | sed "s/\.css//")
    cat $i | \
    sed -r ':a; s%(.*)/\*.*\*/%\1%; ta; /\/\*/ !b; N; ba' \
    | tr -d '\t' | tr -d ' ' | tr -d '\n' | tr -s ' ' ' ' > $formatted_file_name.min.css
done
exit 0

