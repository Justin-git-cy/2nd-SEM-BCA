from google.colab import drive
drive.mount('/content/drive')

# List files in a Google Drive folder
import os
path = "/content/drive/My Drive/"
files = os.listdir(path)
print("Files in Google Drive:", files)

# Copying a file in Google Drive
shutil.copy(path + "file1.txt", path + "file1_copy.txt")
print("File copied in Google Drive")
