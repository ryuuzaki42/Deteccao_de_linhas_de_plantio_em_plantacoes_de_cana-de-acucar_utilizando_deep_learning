#!/bin/bash
#
# Autor= João Batista Ribeiro
#
# Last update: 03/11/2022
#
## Example run:
## ./grep_results_JBs.sh results_02_11_2022_t9_m/ > results_02_11_2022_t9_m/results_sumary.txt
#
folder_to_work=$1
if [ "$folder_to_work" == '' ]; then
    echo -e "\\nError: Need a a folder of results to work!\\n"
    exit 1
fi

cd "$folder_to_work"

folders_local=$(ls -vd -- */) # List folder names
folders_count=$(echo "$folders_local" | wc -l)

i='0'
while [ "$i" -lt "$folders_count" ]; do
    i=$((i + 1))
    folder=$(echo -e "$folders_local" | head -n "$i" | tail -n 1)

    echo -e "\\n$folder"
    cd "$folder"
    grep "dice_score avg:" result_images/results_sumary.txt | cut -d " " -f3

    cd .. || exit
done

echo -e "\\nEnd script!\\n"
