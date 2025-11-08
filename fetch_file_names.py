# Bring all files with a wildcard in directory
import os
import csv

folder_path = r"C:\Users\Your\Path\Here"

opus_files = []

# Finding all .opus here
def list_opus_files(folder):
    for root, dirs, files in os.walk(folder):
        for file in files:
            if file.endswith(".opus"):
                opus_files.append(os.path.splitext(file)[0])

list_opus_files(folder_path)

# put it in a csv
with open('opus_files_list.csv', 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile)
    filewriter.writerow(['File Name'])
    for file in opus_files:
        filewriter.writerow([file])