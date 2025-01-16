#! /usr/bin/bash

# make a directory FOUNDFILES if it doesn't exist
echo "Find and copy"
read -r -p "Enter folder or path to search: " search_folder # ask for folder to search
read -r -p "Enter folder to save files: " save_folder # ask for folder to save the files
mkdir -p "$save_folder" # make the save folder if it doesn't exist

# taking file name from user including file extension

read -r -p "Enter filename: " file

SEARCH=$(find "$search_folder" -name "$file")

if [ -n "$SEARCH" ]; then
cp "$SEARCH" "$save_folder"
echo "copied '$file' to $save_folder"
else 
echo "file '$file' not found"
fi