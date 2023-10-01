# First we'll import the os module
# This will allow us to create file paths across operating systems
import os
# Module for reading CSV files
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')


with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')
 
    # Read the header row first (skip this step if there is no header)
    csv_header = next(csvreader)
    
    total_votes = 0
    candidates = {}
    
    # Read each row of data after the header
    for row in csvreader:
        total_votes += 1
        if row[2] not in candidates.keys():
            candidates[row[2]] = 1
        else:    
            candidates[row[2]] += 1
    
    print('Election Results \n')
    print('------------------------- \n')
    print('Total Votes: ',total_votes)
    print('------------------------- \n')
    for (k, v) in candidates.items():
        print( str(k) , ' : ', format(v/total_votes, ".3%"),"(", str(v) ,")")
        
    print('------------------------- \n')
    Winner = max(candidates, key = lambda x: candidates[x] )
    print('Winner:', Winner)
    
    
with open('output.txt', 'w') as op_file:
    op_file.write('Election Results \n \n')
    op_file.write('------------------------- \n \n')
    op_file.write('Total Votes: %s \n \n' %(total_votes))
    op_file.write('------------------------- \n \n')
    for (k, v) in candidates.items():
        op_file.write("%s: %s (%s)\n \n" % (k, format(v/total_votes, ".3%"), v))
        
    op_file.write('------------------------- \n \n')
    op_file.write('Winner: %s \n \n '%(Winner))
    op_file.write('------------------------- ')
    
    
    
    
    
    
    
    
    
    
    
    
    





