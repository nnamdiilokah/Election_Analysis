# -*- coding: UTF-8 -*-
"""PyPoll Homework Challenge Solution."""

# Add our dependencies.
import csv
import os

# Add a variable to load a file from a path.
file_to_load = os.path.join("resources", "election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Initialize a total vote counter.
total_votes = 0

# 1: Create a county list and county votes dictionary.
candidate_options = []
candidate_votes = {}

# 2: Track the largest county and county voter turnout.
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Read the csv and convert it into a list of dictionaries
with open(file_to_load) as election_data:
    reader = csv.reader(election_data)

    # Read the header
    header = next(reader)

    # For each row in the CSV file.
    for row in reader:

        # Add to the total vote count
        total_votes = total_votes + 1

        # 3: Extract the county name from each row.
        county_name = row[1]

         # 4a: Write an if statement that checks that the
        # county does not match any existing county in the county list.
        if county_name not in candidate_options:

            # 4b: Add the existing county to the list of counties.
            candidate_options.append(county_name)
            # 4c: Begin tracking the county's vote count.
            candidate_votes[county_name] = 0

        # 5: Add a vote to that county's vote count.
        candidate_votes[county_name] += 1





        