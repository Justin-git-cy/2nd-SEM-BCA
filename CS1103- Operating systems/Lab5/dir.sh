echo "Enter directory name:"
read Documents
if [ -d "$dirname" ]; then
  echo "Directory exists."
else
  echo "Directory does not exist."
fi


