#import dependencies
import csv

#set file path 
pollfilepath = "Resources/election_data.csv"

#open file 
with open(pollfilepath) as pollfile:
    filereader = csv.reader(pollfile,delimiter=',')

    print(filereader)

    #read header of import file
    poll_header = next(pollfile)
    print(f"Header: {poll_header}")
