#! /usr/bin/bash

# make a directory FOUNDFILES if it doesn't exist
echo "Find and copy"
read -r -p "Enter folder name to search: " search_folder # ask for folder to search
read -r -p "Enter folder to save files: " save_folder # ask for folder to save the files
# mkdir -p "$save_folder" # make the save folder if it doesn't exist

find_search_folder=$(find C:/Users/Administrator/Downloads/'Study Resources/' -type d -name "$search_folder")
find_save_folder=$(find C:/Users/Administrator/Downloads/'Study Resources/' -type d -name "$save_folder")

echo "Checking if $save_folder and $search_folder exist..."

if [ -n "$find_save_folder" ]; then
echo "$save_folder exists"
else
mkdir -p "$save_folder"
fi

read -r -p "Enter filename (include extension): " file 

if [ -n "$find_search_folder" ]; then
SEARCH=$(find "$search_folder" -name "$file")
else
echo "$search_folder doesn't exist"
fi


if [ -n "$SEARCH" ]; then
cp "$SEARCH" "$save_folder"
echo "copied '$file' to $save_folder"
else 
echo "'$file' not found"
fi