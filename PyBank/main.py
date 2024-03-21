# Import the OS module to create file paths across operating systems
import os

# Import module for reading CSV files
import csv

# Set path for the source file
budget_csv = os.path.join ('Resources','budget_data.csv')

# Open and read the CSV source file
# Specify the delimiter and CSV reader variable to hold content
with open(budget_csv,encoding='utf-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

# Read the header row and store it
    csv_header = next(csvreader)
    # Note: I printed the Header while testing but commenting it as not required in assignment instructions
    # print(f"CSV Header: {csv_header}")


# Declare Variables for data analysis and their starting values
    months = 0
    net_total = 0
    previous_profit = ""
    change = 0
    total_change = 0
    change_periods = 0

# Declare/ initiate Lists and Dictionaries to store values
    date_list = []
    profit_loss_list = []
    changes_list =[]
    increase = {"date":"", "amount":0}
    decrease = {"date":"", "amount":0}


# Loop through the data

    for row in csvreader:

        # Create Lists to store source data for 'Date' and 'Profit/Losses' separately
        date_list.append(row[0])
        profit_loss_list.append(row[1])


        # Calculate the Net Total Amount of 'Profit/Losses' over the entire period 
        # by adding values in that column as we move through the loop and store it
        net_total += int(row[1])


        # Calculate Changes in Profit/ Losses over the entire period
        # Set the starting value for Profit/Losses
        profit_loss = int(row[1])
        
        # As we do not have a previous Profit/Loss value to compare for the data in first entry,
        # exclude the first row by using appropriate If statement
        if previous_profit != "":

            # Calculate Change by deducting previous value from current value in 'Profit/Losses'
            # and storing the calculated Change value by adding to the list
            change = profit_loss - previous_profit
            changes_list.append(change)

            # Calculate Cumulative/ Ongoing Change by adding all change values
            total_change += int(change)

        previous_profit = profit_loss

    
        # Calculate the Greatest Increase in Profits (date and amount) over the entire period
        if change > increase["amount"]:
            increase["amount"] = change
            increase["date"] = row[0]


        # Calculate the Greatest Decrease in Profits (date and amount) over the entire period
        if change < decrease["amount"]:
            decrease["amount"] = change
            decrease["date"] = row[0] 
    

# Calculate Total Number of Months in dataset by counting length of the list containing all dates
months = len(date_list)


# Calculate Average of all Changes by dividing sum of all change values by number of change periods
change_periods=len(changes_list)
average_change = round((total_change / change_periods), 2)
    

# Print all results to the terminal

print(f'Financial Analysis')
print(f'----------------------------')
print(f'Total Months = {months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change}')
print(f'Greatest Increase in Profits: {increase["date"]} (${increase["amount"]})')
print(f'Greatest Decrease in Profits: {decrease["date"]} (${decrease["amount"]})')


# Create an output text file to export the Analysis results and set the path
output = os.path.join("Analysis", "PyBank_results.txt")

# Open the file using "write" mode and write the required results
with open(output, 'w') as datafile:
    datafile.write(f'Financial Analysis\n')
    datafile.write(f'----------------------------\n')
    datafile.write(f'Total Months = {months}\n')
    datafile.write(f'Total: ${net_total}\n')
    datafile.write(f'Average Change: ${average_change}\n')
    datafile.write(f'Greatest Increase in Profits: {increase["date"]} (${increase["amount"]})\n')
    datafile.write(f'Greatest Decrease in Profits: {decrease["date"]} (${decrease["amount"]})')    