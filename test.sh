#!/bin/bash
#Replace the variables with your github repo url, repo name, test
#video name, json named by your UIN
GIT_REPO_URL="https://github.com/heavytrowa/TRN-pytorch.git"
REPO="TRN-pytorch"
VIDEO="sample_data/testing.mp4"
UIN_JSON="625009877.json"
UIN_JPG="625009877.jpg"
git clone $GIT_REPO_URL
cd $REPO
#Replace this line with commands for running your test python file.
echo $VIDEO
echo "This might take a while..."
python test_segment.py --output_file timeLabel.json --video_file  $VIDEO  --weight model/bestnewmodel/TRN_moments_RGB_InceptionV3_TRNmultiscale_segment8_best.pth.tar --arch InceptionV3 --dataset moments

python plot.py timeLabel.json timeLabel.jpg
#rename the generated timeLabel.json and figure with your UIN.
cp timeLabel.json $UIN_JSON
cp timeLabel.jpg $UIN_JPG
