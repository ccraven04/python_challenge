import os
import csv

date = []
pl = []


bank_csv = os.path.join("C:/Users/canda/Desktop/python_challenge/py_bank/budget_data.csv")
file_to_output = os.path.join("Analysis","Budget_Analysis.txt")
with open(bank_csv, newline='') as csvfile:
    
    csvreader = csv.reader(csvfile, delimiter=",")
     
    next(csvreader)
     
    for row in csvreader:
        date.append(row[0])
        pl.append(int(row[1]))
        
     

    

plChange = []

for i in range(1, len(pl)):
    plChange.append(pl[i] - pl[i-1])

output = (
    f"\nFinancial Analysis\n"
    f"------------------\n"
    f"Total Months = {len(date)}\n"
    f"Total = ${sum(pl)}\n"
    f"Average Change = {round(sum(plChange)/len(plChange),2)}\n"
    f"Greatest Increase = {date[plChange.index(max(plChange))+1]} ({max(plChange)})\n"
    f"Greatest Decrease = {date[plChange.index(min(plChange))+1]} ({min(plChange)})\n"

)

print(output)

with open(file_to_output,"w") as txt_file:
    txt_file.write(output)




