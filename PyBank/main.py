# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
import csv
from collections import defaultdict
from collections import Counter

list_of_files=['election_data_1.csv']

# # Method 1: Plain Reading of CSVs
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

candidates=[]
# Method 2: Improved Reading using CSV module
for csv_file in list_of_files:
    csvpath = os.path.join('raw-data', csv_file)

    with open(csvpath, newline='') as csv_input:

        # CSV reader specifies delimiter and variable that holds contents
       
        csvreader = csv.reader(csv_file, delimiter=',')
        next(csvreader,None)

        #  Each row is read as a row
        for row in csvreader:
            candidates.append(row[2])
            
print(candidates)
votes_per_candidate = Counter(candidates)
print(votes_per_candidate)

