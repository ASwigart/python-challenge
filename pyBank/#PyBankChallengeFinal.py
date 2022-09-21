#Py Bank Challenge


import os
import csv
import string

#find Budget_data.csv
#relative path

#create blank lists for data
Bankdata=[]
date=[]
totalmonths=0
Netchange=[]
Netchange_list=[]
months=[]
count= []
Sum=0

Increasedpandl =[0,""]
Decreasepandl=[9999999999,""]


file_to_load = os.path.join("..","Resources", "budget_data.csv")
with open(file_to_load) as file:
    csvr = csv.reader(file, delimiter=',')
    print (csvr)
    csv_header = next(csvr)
    # Sum+=int(csv_header[1])
    # pandl=int(csv_header[1])
    firstrow=next(csvr)
    prevpl=int(firstrow[1]) 
    print(f"CSV Header: {csv_header}")
    for row in csvr:
        # print(row[0])
        # print(row[1])
#amend to list of lists
        totalmonths +=1
        Sum +=int(row[1])
        change=int(row[1])-prevpl
        prevpl=int(row[1])
        Netchange+=[change]
        # print("Netchange_list")
        months+=[row[0]]
#The greatest decrease in profits (date and amount) over the entire period
        if change > Increasedpandl[0]:
            Increasedpandl[1]=row[0]
            Increasedpandl[0]=change
#Greatest Decrease, find column 2 min value and find assoicated col 1 date, print both
        if change < Decreasepandl[0]:
            Decreasepandl[1]=row[0]
            Decreasepandl[0]=change    
Avg=sum(Netchange)/len(Netchange)

  

print ("Financial Analysis")
print ("---------------------------------")
print ("Total Months:_", totalmonths)
print ("Total_$", Sum)
print ("Average Change_$", Avg)
print ("Greatest Increase in Profits_$", Increasedpandl)
print ("Greatest Decrease in Profits_$", Decreasepandl)
# Print Financial Analysis
# ----------------------------
#Total Months: 86
#Total: $22564198
#Average Change: $-8311.11
#Greatest Increase in Profits: Aug-16 ($1862002)
#Greatest Decrease in Profits: Feb-14 ($-1825558)
