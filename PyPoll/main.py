import os
import csv

file_path = 'Resources/election_data.csv'

total_votes = 0
candidates = {}
winner = ""
max_votes = 0

with open(file_path, mode='r') as file:
    csv_reader = csv.DictReader(file)
    
    for row in csv_reader:
        total_votes += 1
        candidate = row["Candidate"]
        
        if candidate in candidates:
            candidates[candidate] += 1
        else:
            candidates[candidate] = 1

print(f'Election Results')
print("-------------------------")
print(f'Total Votes: {total_votes}')
print("-------------------------")
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    if votes > max_votes:
        max_votes = votes
        winner = candidate
    print(f'{candidate}: {percentage:.3f}% ({votes})')
print("-------------------------")
print(f'Winner: {winner}')
print("-------------------------")

text_path = os.path.join('analysis', 'Export_Election_Analysis.txt')
with open(text_path,"w") as text_file:

    text_file.write(f'Election Results' + "\n")
    text_file.write("-------------------------" + "\n")
    text_file.write(f'Total Votes: {total_votes}' + "\n")
    text_file.write("-------------------------" + "\n")
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        if votes > max_votes:
            max_votes = votes
            winner = candidate
        text_file.write(f'{candidate}: {percentage:.3f}% ({votes})' + "\n")
    text_file.write("-------------------------" + "\n")
    text_file.write(f'Winner: {winner}' + "\n")
    text_file.write("-------------------------" + "\n")