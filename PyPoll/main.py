# Import the OS module to create file paths across operating systems
import os

# Import module for reading CSV files
import csv

# Set path for the source file
election_csv = os.path.join ('Resources','election_data.csv')

# Open and read the CSV source file
# Specify the delimiter and CSV reader variable to hold content
with open(election_csv,encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row and store it
    csv_header = next(csvreader)
    # Note: I printed the Header while testing but commenting it as not required in assignment instructions
    # print(f"CSV Header: {csv_header}")


# Declare Variables for data analysis and their starting values
    total_vote_count = 0
    candidate_vote_count = 0
    winner_vote_count = 0
    winner = ""

# Declare/ initiate Lists to store values
    total_candidate_list =[]
    unique_candidate_list =[]
    count_list =[]
    percentage_list =[]


# Loop through the full dataset

    for row in csvreader:

        # Create List to store all entries for Candidates
        total_candidate_list.append(row[2])

        # Calculate Total Number of Votes cast by counting total number of data entries/ rows
        total_vote_count += 1

        # Create List of Unique Candidate names
        candidate = row[2]
        if candidate not in unique_candidate_list:
            unique_candidate_list.append(candidate)
 

# Calculate Total Number and Percentage of Votes for each Candidate, and name of Winner
# Loop through Unique Candidate list and within that loop through the list of all Candidate name entries
    
    for candidate_name in unique_candidate_list:

        for value in total_candidate_list:

            # Calculate total and percentage votes for each Unique Candidate name
            if value == candidate_name:
                candidate_vote_count += 1

        candidate_vote_percentage = round(((candidate_vote_count/total_vote_count)*100),3)

        # Create Lists to Store Total and Percentage Votes for each Candidate
        count_list.append(candidate_vote_count)
        percentage_list.append(candidate_vote_percentage)

        # Identify the Winner of election based on popular vote
        if candidate_vote_count > winner_vote_count:
            winner_vote_count = candidate_vote_count
            winner = candidate_name

        # Reset the Vote count to loop through next candidate
        candidate_vote_count = 0


# Print all results to the terminal

print(f'Election Results')
print('----------------------------')
print(f'Total Votes: {total_vote_count}')
print('----------------------------')
# Print statistics for each Unique Candidate by iterating through the 3 lists storing data
for (name, percentage, count) in zip(unique_candidate_list, percentage_list, count_list):
    print(f"{name}: {percentage}% ({count})")
print(f'----------------------------') 
print(f'Winner: {winner}')
print(f'----------------------------')


# Create an output text file to export the Analysis results and set the path
output = os.path.join("Analysis", "election_analysis.txt")

# Open the file using "write" mode and write the required results
with open(output, 'w') as datafile:
    datafile.write(f'Election Results\n')
    datafile.write(f'----------------------------\n')
    datafile.write(f'Total Votes: {total_vote_count}\n')
    datafile.write(f'----------------------------\n')
    # Print statistics for each Unique Candidate by iterating through the 3 lists storing data
    for (name, percentage, count) in zip(unique_candidate_list, percentage_list, count_list):
        datafile.write(f'{name}: {percentage}% ({count})\n')
    datafile.write(f'----------------------------\n')
    datafile.write(f'Winner: {winner}\n')
    datafile.write(f'----------------------------\n')