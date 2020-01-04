import os
import csv


poll_csv = os.path.join("PyBank_Resources_election_data.csv")

with open(poll_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

