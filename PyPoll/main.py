import os
import csv
import numpy as np
from collections import OrderedDict 
from pathlib import Path

def print_solution(voterids,uniquecandidates):
    votecountdict = OrderedDict()    
    for candidate in uniquecandidates:
        votecountdict[candidate] = candidates.count(candidate)        
    
    print("Election Results")
    print("--------------------------")    
    print("Total votes:", len(voterids))
    print("--------------------------")    
    for candidate, votecount in sorted(votecountdict.items(), key=lambda x: x[1], reverse=True):
        print("{}:".format(candidate),"{:.3%}".format(votecount/len(voterids)),"({})".format(votecount))
    print("--------------------------")
    print("Winner:",sorted(votecountdict.items(), key=lambda x: x[1], reverse=True)[0][0])

    output_file = Path(os.path.dirname(__file__),"analysis","outputfile.txt")

    with open(output_file,"w") as file:
        
        file.write("Election Results")
        file.write("\n")
        file.write("--------------------------")
        file.write("\n")
        file.write(f"Total votes:{len(voterids)}")
        file.write("\n")
        file.write("--------------------------")
        file.write("\n")
        for candidate, votecount in sorted(votecountdict.items(), key=lambda x: x[1], reverse=True):
            file.write(f"{candidate}:{'{:.3%}'.format(votecount/len(voterids))} ({votecount})")
            file.write("\n")
        
        file.write(f"--------------------------")
        file.write("\n")
        file.write(f"Winner:{sorted(votecountdict.items(), key=lambda x: x[1], reverse=True)[0][0]}")
  


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
        
    analyze_votes = 0
    row_count = 0
    for row in csv_reader:   
        # Read through each row of data after the header
        voterids.append(row[0])
        counties.append(row[1])
        candidates.append(row[2])
    
    npcandidates = np.array(candidates) 
    uniquecandidates = np.unique(npcandidates)
    votecount = []
    print_solution(voterids,uniquecandidates)
       

