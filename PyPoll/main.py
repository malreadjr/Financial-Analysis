import os
import csv
from pathlib import Path

                        
voterids = []
counties = []
candidates = []


script_path = os.path.dirname(__file__)
file_path = "Resources\\election_data.csv"
election_csv = os.path.join(script_path,file_path)

# Open and read csv
with open(election_csv, "r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    
    for row in csv_reader:   
        # Read through each row of data after the header
        voterids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
    