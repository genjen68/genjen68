#first import csv and join
import os   
import csv
election_data = os.path.join("Resources","election_data.csv")

#open csv file
with open(election_data) as csv_file:
    csv_reader = csv.reader(csv_file,delimiter=',')
    #skip header
    csv_header = next(csv_reader)
#next calculate the total votes cast in electionm
    total_votes = 0
    for row in csv_reader:
        total_votes = total_votes =+ int(row[0])
print(f"Total Votes: {total_votes}")

# find a list of the candidates in the election
    
empty_list = []
def unique(list1,candidate):
    if candidate not in list1:
        list1.append(candidate)
print(empty_list)