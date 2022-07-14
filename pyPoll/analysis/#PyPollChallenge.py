#PyPoll Challenge

from ast import Return
import os
import csv
from collections import Counter
from xml.etree.ElementPath import find


election_data=[]
sum=0
tvotes=0

row=[]
# Candidates
candidates = []
candivotes = {}
candiops = []
#winning candidate
wincandi=""
wincount = 0
winpercent = 0


#Find electiondata.csv
election_data = os.path.join("..","Resources","election_data.csv")
with open(election_data) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    print (csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
    for row in csvreader:
        print(row)
    #Total Votes
        tvotes = tvotes +1
        sum +=int(row[0])
        # print(Total Votes Are_, [tvotes])
        candidates=row[2]
        if candidates not in candiops:
            candiops.append(candidates)
            candivotes[candidates]=0 


# declaring the list




    # for candidates in election_data       
        # counter={row[2]}
        # for candidates in election_data:
        #     counter[election_data]=0
        # counter[candidates] +=1 
        # Python code to count the number of occurrences




    # # find unique strings and total
        # count = candidates.count(election_data)
        #     if row[2] == "Charles Casper Stockham",
        #         count = count +1
        #         elecresultsccs = 

        #     else row[2] == "Diana DeGette",
        #         count = count +1
        #         elecresultsdeg =

        #     else row[2] == "Raymon Anthony Doane")
        #         count = +1
        #         elecresultsrad = 
        # print ()

#     Percent of total vote
# csstotalper = (electresultsccs/tvotes) *100
# degtotalper = (electresultsdeg/tvotes) *100
# radtotalper = (electresultsrad/tvotes) *100
#     total winning votes for winners


#The winner of the election


#The percentage of votes each candidate won
    #Percent of total vote


#The total number of votes each candidate won
    #total winning votes


#The winner of the election based on popular vote.
    #winner of popular vote
print ("Election Results")
print ("------------------------")
print ("Total Votes:_" & tvotes)
print ("-------------------------")
# print (f{candidate1}":"csstotalper", "csstotal")
# print (f{candidate2}":" "degtotalper","degtotal")
# print (f{candidate3}":" "radtotalper", "radtotal")
# print ["----------------------------"]
# print ["Winner "]
#Print Election Results
#-------------------------
#Total Votes: 369711
#-------------------------
#Charles Casper Stockham: 23.049% (85213)
#Diana DeGette: 73.812% (272892)
#Raymon Anthony Doane: 3.139% (11606)
#-------------------------
#Winner: Diana DeGette
#-------------------------
