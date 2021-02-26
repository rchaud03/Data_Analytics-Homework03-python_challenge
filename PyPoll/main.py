'''
The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote.
'''

import os
import csv
from collections import Counter as ct

voter_data = os.path.join("Resources","election_data.csv")
with open(voter_data, "r") as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csv_reader)
    output_file = "analysis/election_results.txt"

    casted_vote_count = 0
    candidates_list = []
    votes = []
    #candidates_list = str(list(set(votes)))
    candidates_list = list(set(votes))


    for row in csv_reader:
        vote = row[2]
        casted_vote_count += 1
        votes.append(vote)
        if vote not in candidates_list:
            candidates_list.append(vote)

    print(f"\nElection Results:\n------------------------------------------\nTotal votes casted: {casted_vote_count:,}.\nCandidates list {candidates_list}\n------------------------------------------\n")

    #Count the amount of times each candidate in the candidate list shows up in the votes list
    for i in candidates_list:
        tally = votes.count(i)
        print(f"{i} : {round((tally/casted_vote_count) * 100)}%  ({tally:,} votes)")
        with open(output_file, "w") as txt_file:
            txt_file.write(f"{i} : {round((tally / casted_vote_count) * 100)}%  ({tally:,} votes)\n")

with open(output_file, "w") as txt_file:
    txt_file.write(f"\nElection Results:\n------------------------------------------\nTotal votes casted: {casted_vote_count:,}.\nCandidates list {candidates_list}\n------------------------------------------\n")
