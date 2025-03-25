#!/bin/bash
# Shell Script for Piping Commands
# Usage: ./piping_commands.sh


list_directory_contents() {
    echo "Listing contents of the current directory:"
    ls -l
    echo ""
}


filter_and_sort_contents() {
    read -p "Enter a pattern to filter files (e.g., .txt for text files): " pattern
    echo "Filtering and sorting files with pattern '$pattern'..."
    # Use ls, grep, and sort in a pipeline
    ls -l | grep "$pattern" | sort
    echo ""
}


search_file() {
    read -p "Enter the name of the file to search for: " filename
    if [ -e "$filename" ]; then
        echo "File '$filename' exists in the current directory."
    else
        echo "File '$filename' does not exist in the current directory."
    fi
    echo ""
}

counting() {
read -p "Enter a pattern to filter files (e.g . , akash.txt files): " count
echo "count '$count' ..."
ls -l| grep "$count" | wc -l
echo ""
}


echo "Piping Commands Manager"
echo "1. List contents of the current directory"
echo "2. Filter and sort directory contents"
echo "3. Search for a file in the current directory"
echo "4. count"
echo "5. Exit"

# Loop until the user chooses to exit
while true; do
    read -p "Select an option (1-5): " option
    case $option in
        1) # List directory contents
            list_directory_contents
            ;;
        2) # Filter and sort directory contents
            filter_and_sort_contents
            ;;
        3) # Search for a file
            search_file
            ;;
        4) # counting
            counting
             ;;
        5) # Exit the script
            echo "Exiting the Piping Commands Manager. Goodbye!"
            exit 0
            ;;
        *) # Invalid option
            echo "Invalid option. Please select 1-4."
            ;;
    esac
    echo "" 
done

