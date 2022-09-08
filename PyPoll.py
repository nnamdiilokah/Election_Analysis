# The data we need to retrieve
# 1. The total numbers of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies.
import csv
import os
# Assisgn a variable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
#Open the election results and read the file
with open(file_to_load) as election_data:
    # Read the file object with reader function
    file_reader = csv.reader(election_data)
    # Read and print the header row
    headers = next(file_reader)
    print(headers)
#print each row in the csv file
    for row in file_reader:
        print(row)
# print the file object
    print(election_data)
# create a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis","election_analysis.txt")
#using the with statement open 
with open(file_to_save, "w") as txt_file:
#write three counties to the file
    txt_file.write("Arapahoe\nDenver\nJefferson")


