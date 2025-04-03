from google.colab import drive
import os
import shutil  

drive.mount('/content/drive')

path = "/content/drive/My Drive/"

files = os.listdir(path)
print("Files in Google Drive:", files)

shutil.copy(path + "file1.txt", path + "file1_copy.txt")
print("File copied in Google Drive")
