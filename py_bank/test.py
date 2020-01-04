print ("hello world")


bank_csv = os.path.join("PyBank_Resources_budget_data.csv")

with open(bank_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")

    print(csvreader)

    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")
