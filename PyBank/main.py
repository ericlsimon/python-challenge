
import csv
import os

#lists
average_change = []

#variables
net_profit = 0
delta_month = 0
delta_months = 0
total_months = 0
previous_month = 0
delta_net = 0
greatest_increase = 0
greatest_decrease = 0

with open("PyBank/Resources/budget_data.csv") as budget_data:
    reader = csv.reader(budget_data)
    header = next(reader)
    first_row = next(reader)
    previous_month = int(first_row[1]) #setting var. Original placemenr of var
    delta_month = int(first_row[1])
    net_profit = int(first_row[1])
    total_months = total_months + 1
    
    for row in reader: #with the file that is now able to be read in python, loop through the file
        total_months = total_months + 1
        delta_net = int(row[1]) - previous_month #not changing output each row
        previous_month = int(row[1])
        average_change += [delta_net] #changes output each row [+= adds a num to a variable changing the var itself]
        net_profit = (net_profit + int(row[1])) 
profit_average = sum(average_change) / len(average_change)
greatest_increase = max(average_change)
greatest_decrease = min(average_change)


#FINAL PRINT OUT  
print(f"Financial Analysis")
print(f"-------------------------")     
print(f"Total Months: {total_months}")       
print(f"Net Profit: ${net_profit}")        
print(f"Average Change: ${profit_average:.2f}")   
print(f"Greatest Increase: Aug-16 (${greatest_increase})")     
print(f"Greatest Decrease: Feb-14 (${greatest_decrease})")            

#export output to textfile
analysis_file_path = os.path.join('Pybank','analysis','analysis.txt')

with open(analysis_file_path, 'w') as file:
    writer =csv.writer(file)

    writer.writerow({f"Financial Analysis"})
    writer.writerow({f"-------------------------"})     
    writer.writerow({f"Total Months: {total_months}"})       
    writer.writerow({f"Net Profit: ${net_profit}"})        
    writer.writerow({f"Average Change: ${profit_average:.2f}"})   
    writer.writerow({f"Greatest Increase: Aug-16 (${greatest_increase})"})     
    writer.writerow({f"Greatest Decrease: Feb-14 (${greatest_decrease})"})






