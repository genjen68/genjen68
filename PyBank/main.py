#first import csv budget data
import os
import csv
#csv path
budget_data = os.path.join("..","Resources","budget_data.csv")

#open and read budget data csv
with open(budget_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first 
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")

   
 #Count the total number of months in data as total_months (should this be value_count?)
   next(csv_reader,none)
   for row in csv_reader
    

   

#Total the amount of profit/losses columm as total_profit
total_profit =

#calculate the average changes over the time frame as average_change as currency

#Print title "Financial Analysis" over data

#Print total_months as "Total Months"

#Print average_change as "Average Change"

#Print Month with greatest increase in profits and amount as "Greatest Increase in Profits"
 
#Print Month with Greatest decrease in profits and amount as "Greatest Decrease in Profits"

    