#Import dependencies
import csv

#set file path for reading
bankfilepath = "Resources/budget_data.csv"

#open file and set cursor
with open(bankfilepath) as bankfile:
    bankreader = csv.reader(bankfile,delimiter = ',')

    print(bankreader)

    #Reads header of import file
    bank_header = next(bankreader)
    print(f"CSV Header: {bank_header}")

    #establish variables for storing and calculating data 
    monthcount = 0
    running_profit = 0
    change = 0
    previous_row_profit = 0
    greatest_increase = 0
    greatest_decrease = 0

    #read through rows
    for row in bankreader:
        
        #running total of number of months
        monthcount += 1
        
        #running total of profits over period
        running_profit = running_profit + int(row[1])
        
        #skipping first month for finding the change in profits month to month
        if row[0] != "Jan-10":
            
            #running total of change in profits for finding average change in profit
            change = change + (float(row[1]) - previous_row_profit)
            
            #searching for greatest increase in profits month to month
            if (float(row[1]) - previous_row_profit) > greatest_increase:
                greatest_increase = (float(row[1]) - previous_row_profit)
                increase_month = row[0]
            
            #searching for greatest decrease in profits month to month
            if (float(row[1]) - previous_row_profit) < greatest_decrease:
                greatest_decrease = (float(row[1]) - previous_row_profit)
                decrease_month = row[0]
        
        #storing current row's profit as variable for use in the next row's calculations of change
        previous_row_profit = float(row[1])

    #calculation for average change in profits over time period
    average_change = change/(monthcount - 1)

    #printing various statistics to terminal
    print(f"Total Months: {monthcount}")
    print(f"Total Profit: ${running_profit}")    
    print(f"Avg Change: ${round(average_change, 2)}")
    print(f"Greatest Increase in Profits: {increase_month} (${int(greatest_increase)})")
    print(f"Greatest Decrease in Profits: {decrease_month} (${int(greatest_decrease)})")

#setting path for writing to text file
outputpath = "Analysis/Analysis.txt"

#opening output file for writing
with open(outputpath, "w", newline='') as output:
    writer = csv.writer(output)

    #writing statistics to text file
    writer.writerow([f"Total Months: {monthcount}"])
    writer.writerow([f"Total Profit: ${running_profit}"])
    writer.writerow([f"Avg Change: ${round(average_change, 2)}"])
    writer.writerow([f"Greatest Increase in Profits: {increase_month} (${int(greatest_increase)})"])
    writer.writerow([f"Greatest Decrease in Profits: {decrease_month} (${int(greatest_decrease)})"])