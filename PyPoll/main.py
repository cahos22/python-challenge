# First we'll import the os module 
# This will allow us to create file paths across operating systems
import os
import csv
from collections import defaultdict
from collections import Counter

list_of_files=["election_data_1.csv","election_data_2.csv"]

# # Method 1: Plain Reading of CSVs
# with open(csvpath, 'r') as file_handler:
#     lines = file_handler.read()
#     print(lines)
#     print(type(lines))

candidates=[]
# Method 2: Improved Reading using CSV module
for csv_file in list_of_files:
    csvpath = os.path.join("raw_data", str(csv_file))
    print(csvpath)
    with open(csvpath, newline='') as csv_input:

        # CSV reader specifies delimiter and variable that holds contents
       
        csvreader = csv.reader(csv_input, delimiter=',')
        next(csvreader,None)

        #  Each row is read as a row
        
        for row in csvreader:
            candidates.append(row[2])

total_votes= len(candidates)           
votes_per_candidate = Counter(candidates)
percentage_per_candidate = {}
for key in votes_per_candidate.keys():
    percentage_per_candidate[key] = (votes_per_candidate[key] / total_votes) * 100

print("Election Results")
print("-" * 15)
print("Total Votes : "+str(total_votes))
print("-" * 15)

for key,value in votes_per_candidate.items:
    print("{}: {}% ({})".format(key,percentage_per_candidate[key],value))



