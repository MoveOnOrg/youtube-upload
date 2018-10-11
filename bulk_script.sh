#!/bin/bash

# to use this script for bulk uploading:
# sign into a google account that has at least one associated
# youtube channel.
# create video_data.csv with the desired metadata fields and a 
# blank line at the end of the file.
# create a videos dir at the root dir of the youtube-upload repo
# and copy all the video files into it.
# edit the code below to read and output all the metadata
# you want to use.
# run the script with `bash bulk_script.sh`.
# the first upload will prompt you to load a url and 
# verify your identity to get a token.

file="video_data.csv" 
# absolute path to file with video file names and titles.
# don't forget to add a blank line to the end of the csv 
# or this script will skip the last row

while IFS=, read -r f1 f2 # f1 is title and f2 is filename
do
  # edit this command to include all the fields you want
  # see README.md in the youtube-upload repo for reference 
  youtube-upload --title="$f1" videos/$f2 --privacy private
done < "$file"