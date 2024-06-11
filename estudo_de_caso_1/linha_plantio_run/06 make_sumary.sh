#!/bin/bash

# cd '/media/sda2/home/j/Dropbox/ufu/2022/paper_segmentation/results/predict_sumary/'
# weights_Base_X/predict_Base_X

# last update: 01/05/2022

cd "results/predict_sumary/"

work=$1
folderWork=$(find . -maxdepth 2 -type d | sort | grep "predict"| cut -d '/' -f2-)

if [ "$work" == "dice" ]; then
    command1="cat U*/*.csv | grep -E "ave.*dice" | cut -d ',' -f2 | tr '\r\n' ' ' | sed 's/  /\t/g' | sed 's/\t\t/\t/g' > 1u"
    command2="cat L*/*.csv | grep -E "ave.*dice" | cut -d ',' -f2 | tr '\r\n' ' ' | sed 's/  /\t/g' | sed 's/\t\t/\t/g' > 2l"
    command3="cat P*/*.csv | grep -E "ave.*dice" | cut -d ',' -f2 | tr '\r\n' ' ' | sed 's/  /\t/g' | sed 's/\t\t/\t/g' > 3p"
    command4="cat 1u > 0all; echo >> 0all; cat 2l >> 0all; echo >> 0all; cat 3p >> 0all"

elif [ "$work" == "iou" ]; then
    command1="cat U*/*.csv | grep -E "ave.*IOU" | cut -d ',' -f2 | tr '\r\n' ' ' | sed 's/  /\t/g' | sed 's/\t\t/\t/g' > 1u"
    command2="cat L*/*.csv | grep -E "ave.*IOU" | cut -d ',' -f2 | tr '\r\n' ' ' | sed 's/  /\t/g' | sed 's/\t\t/\t/g' > 2l"
    command3="cat P*/*.csv | grep -E "ave.*IOU" | cut -d ',' -f2 | tr '\r\n' ' ' | sed 's/  /\t/g' | sed 's/\t\t/\t/g' > 3p"
    command4="cat 1u > 0all; echo >> 0all; cat 2l >> 0all; echo >> 0all; cat 3p >> 0all"
elif [ "$work" == "rm" ]; then
    command1="rm 1u"
    command2="rm 2l"
    command3="rm 3p"
    command4="rm 0all"
else
    echo "Option \"$work\" not recognized!"
    exit 1
fi

startFolder=$PWD
for folder in $(echo "$folderWork"); do
    echo "Folder: $folder"
    cd "$folder"

    eval $command1
    eval $command2
    eval $command3
    eval $command4

    cd $startFolder
done

echo "All done!"
