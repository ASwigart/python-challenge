#PyPoll Challenge

from ast import Return
import os
import csv
from collections import Counter
from xml.etree.ElementPath import find



# Create Lists & Dictionaries
candidate_votes = {}
election_data=[]
row=[]
candidates = []
candivotes = {}
candiops = []

# Candidates

#winning candidate
sum=0
totalvotes=0
winner_name= ""
winner_votes=0


# total count loop
# Find Election Data
election_data = os.path.join("Resources","election_data.csv")
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print (csvreader)
    csv_header = next(csvreader)
    for row in csvreader:
    #Total Votes
        totalvotes = totalvotes +1
        candidates=row[2]
        if candidates not in candiops:
            candiops.append(candidates)
            candivotes[candidates]=0

        candivotes[candidates]+=1



for candidates, votes in candivotes.items():
    if votes > winner_votes:
        winner_name=candidates
        winner_votes=votes


output= f"""
*Election Results*
-------------------------
Total Votes: {totalvotes}
-------------------------
Charles Casper Stockham: {candivotes["Charles Casper Stockham"]/totalvotes *100:.3f}% ({candivotes["Charles Casper Stockham"]})
Diana DeGette: {candivotes["Diana DeGette"]/totalvotes *100:.3f}% ({candivotes["Diana DeGette"]})
Raymon Anthony Doane: {candivotes["Raymon Anthony Doane"]/totalvotes *100:.3f}% ({candivotes["Raymon Anthony Doane"]})
-------------------------
Winner: {winner_name}
-------------------------
"""

print(output)

# write to text
with open('analysis/election_analysis.txt', 'w') as f:
    f.write(output)

