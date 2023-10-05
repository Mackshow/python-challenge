#####################################################################################################################################
#####################################################################################################################################

import csv
import os

     #set variables
vote_count_Charles = 0
vote_count_Diana = 0
vote_count_Raymon = 0
count = 0 
candidate_total = 0
count3 = 0
    #set blink list
can_hold = []
each_Candidate = [] 
each_Candidate1 = [] 
votelist_ = {}

#vote_percent = vote_count / count
    
    #access file on system
fh = os.path.join("election_data.csv")

    #used csv reader to read csv file ## Split lines using delimiter
with open(fh) as csv_file:
    reader = csv.reader(csv_file, delimiter = ",")

    #Retrieve header
    csv_header = next(reader)
    #print(f'Header: {csv_header}')

    # counter to count each row   
    for row in reader :
        count = count + 1
        can_hold = row
    #Captures info in row 2 
        candidate_name = row[2]
    
    
    #count all individual votes
        if candidate_name ==  'Charles Casper Stockham':
            vote_count_Charles += 1           
            
        if candidate_name ==  'Diana DeGette':
            vote_count_Diana += 1
            
        if candidate_name ==  'Raymon Anthony Doane':           #if exact string exist in loop
            vote_count_Raymon += 1                              #count
            c_percent = ((vote_count_Charles / count) * 100)    #calcuclate vote percent of total vote as whole number
            d_percent = ((vote_count_Diana / count) * 100)
            r_percent = ((vote_count_Raymon / count) * 100)


        for j in range(2, len(can_hold), 3):   #loop through index 2 of 3 total rows (0,1,2), Each index represents a Column 
            cand = can_hold[j]                 #cand become variable J in can_hold() 
        if cand not in each_Candidate:         #if cand not in list 
            each_Candidate.append(cand)        #append list from cand
        elif cand in each_Candidate:           #if can is in list 
            continue                           #skip
        
        count2 = 0
        for j in range(2, len(can_hold), 3):   #loop through index 2 of 3 total rows (0,1,2), Each index represents a Column 
            cand = can_hold[j]                    #cand become variable J in can_hold() 
        if cand not in each_Candidate1:         #if cand not in list 
            each_Candidate1.append(can_hold)    #append list from cand
            count3 = count2 + 1                 #count every instance
            
       ###Prints resutls in desired format
print(f'\nElection Results \n------------------------------------\nTotal votes: {count}\n------------------------------------\n')
print(f'Charles Casper Stockham:  {int(c_percent)}%  ({vote_count_Charles})\n  ')
print(f'Diana DeGette:  {int(d_percent)}%  ({vote_count_Diana})\n  ')
print(f'Raymon Anthony Doane:  {int(r_percent)}%  ({vote_count_Raymon})\n  ')
print("------------------------------------\n")
print("Winner: Diana DeGette\n")
print("------------------------------------\n")

#####################################################################################################################################
#####################################################################################################################################

