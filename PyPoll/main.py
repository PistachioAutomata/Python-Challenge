#import dependencies
import csv

#set file path 
pollfilepath = "Resources/election_data.csv"

#open file 
with open(pollfilepath) as pollfile:
    filereader = csv.reader(pollfile,delimiter=',')

    print(filereader)

    #read header of import file
    poll_header = next(filereader)
    print(f"Header: {poll_header}")

    #establish variables for calculations
    votecount = 0
    candidates = {}

    #read through rows
    for row in filereader:
        
        #count votes
        votecount += 1

        #find unique candidates
        if row[2] not in candidates:
            candidates[row[2]] = 0
        if row[2] in candidates:
            candidates[row[2]] += 1
        
    #print total votes   
    print(f"Total Votes: {votecount}")

    #inser line break
    print("----------------------------------")
    
    #Print results for each candidate, and calculate voteshare per candidate
    for candidate in candidates:
        print(f"{candidate}: {round((candidates[candidate]/votecount)*100,3)}% ({candidates[candidate]} votes)")

    #insert another line break
    print("----------------------------------")
    
    #Find the winner of the polll via zipping dictionary elements into usable list and applying max function
    winner = max(zip(candidates.values(), candidates.keys()))[1]

    #Print Winner 
    print(f"Winner: {winner}")

#set writing output path
outputpath = "Analysis/Analysis.txt"

#open output file for writing
with open(outputpath, "w", newline='') as output:
    writer = csv.writer(output)

    #write total votes to output
    writer.writerow([f"Total Votes: {votecount}"])
    
    #write individual candidate counts to output
    for candidate in candidates:
        writer.writerow([f"{candidate}: {round((candidates[candidate]/votecount)*100,3)}% ({candidates[candidate]} votes)"])

    #write Winner entry to output
    writer.writerow([f"Winner: {winner}"])