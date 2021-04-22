# first import the csv file
import os
import csv
bank_data = os.path.join("Resources","budget_data.csv")

#open csv file
with open (bank_data) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=",")

#skip header for counts
    csv_header = next(csv_reader)

#calculate the total number of months in data
#calculate the total profit/loss as integer
    Total_Months = 0
    Total_Profit = 0
 
    for row in csv_reader:
        Total_Months = Total_Months + 1
        Total_Profit = Total_Profit + int(row[1])
#Print test Total_Months as "Total Months:"
#Print test Total Profit/Loss as "Total:"
print(f"Total Months: {Total_Months}")
print(f"Total: {Total_Profit}")


