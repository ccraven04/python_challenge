import os
import csv


poll_csv = os.path.join("C:/Users/canda/Desktop/python_challenge/py_poll/election_data.csv")

file_to_output = os.path.join("Analysis","Poll_Analysis.txt")


voter = []
cand = []
vote_count = []
vote = []

with open(poll_csv, newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)
    
    for row in csvreader:
        voter.append(row[0])
        vote.append(row[2])
        
cand2 = list(set(vote))
cand2.sort()

for cand in cand2:
    vote_count.append(vote.count(cand))





#  ```text
#  Election Results
#  -------------------------
#  Total Votes: 3521001
#  -------------------------
#  Khan: 63.000% (2218231)
#  Correy: 20.000% (704200)
#  Li: 14.000% (492940)
#  O'Tooley: 3.000% (105630)
#  -------------------------
#  Winner: Khan
#  -------------------------
#  ```
 
      
print(f"Election Results")
print(f"------------------")
print(f"Total Votes = {len(voter)}")
print(f"------------------")
for c in range(len(cand2)):
    print(f"{cand2[c]}: {'{:.2%}'.format(vote_count[c]/len(vote))} ({vote_count[c]})")
print(f"------------------")
print(f"Winner: {cand2[vote_count.index(max(vote_count))]}")
print(f"------------------")
    

with open(file_to_output, "w") as txt_file:
    txt_file.write("Voter Analysis")
    txt_file.write("\n")
    txt_file.write("__________________________________")
    txt_file.write("\n")
    txt_file.write(f"Total Votes: {len(voter)}")
    txt_file.write("\n")
    for c in range(len(cand2)):
        txt_file.write(
            f"{cand2[c]}: {'{:.2%}'.format(vote_count[c]/len(vote))} ({vote_count[c]})")
        txt_file.write("\n")
    txt_file.write("__________________________________")
    txt_file.write("\n")
    txt_file.write(f"Winner: {cand2[vote_count.index(max(vote_count))]}")
    txt_file.write("\n")
    txt_file.write("__________________________________")

