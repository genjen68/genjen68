#first import csv election data
import os
import csv

election_data = os.path.join("..","Resources","election_data.csv")
#open and read budget data csv
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    #skip header row
    csv_header = next(csv_file)
    print(f"Header: {csv_header}")
    

   # Calculate the total number of votes cast in election as total_votes
   
   # Complete list of all candidate in election
   
   # For each candidate, calculate number of votes and add % of total 

   #Determine overall winner as Winner
   
   #  Print "Election Results" as header

# Print total_votes as "Total Votes"

#Print candidate list with total votes and percentages

#

   
   # Print Winner of election as "Winner:(name)"  