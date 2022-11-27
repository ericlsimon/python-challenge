
#define the variables
total_votes = 0
row_count = 0 
highest_votes = 0
winning_candidate = ""
winning_percentage = 0.00

#lists/dictionaries
votes_by_candidate = {} #output ex: Charles Stockham: 23.049%
keys = [] #unique candidates
values = 0 #variable containing sum of votes by candidate
found = False

#imports
import csv
import os
with open("PyPoll/Resources/election_data.csv") as election_data:
    reader = csv.reader(election_data)
    header = next(reader)


    for row in reader:
        unique_candidates = row[2] #next(reader)
        total_votes = total_votes + 1
        if unique_candidates not in keys:
            keys.append(unique_candidates)  
            votes_by_candidate[unique_candidates] = 0 #tracker begins
        votes_by_candidate[unique_candidates] = votes_by_candidate[unique_candidates] + 1 #take candidates in the dict and add each time
    print(f"Election Results")
    print(f"-------------------------")        
    print(f"Total Votes: {total_votes}")
    print(f"-------------------------")   

analysis_file_path = os.path.join('PyPoll','analysis','analysis.txt')

with open(analysis_file_path, 'w') as file:
    writer =csv.writer(file)
    writer.writerow({f"Election Results"})
    writer.writerow({f"-------------------------"})     
    writer.writerow({f"Total Votes: {total_votes}"})       
    writer.writerow({f"-------------------------"}) 

    for candidate, vote_count in votes_by_candidate.items(): #vote = vote count
        vote_winner = votes_by_candidate.get(candidate) #trying to get vote in dict - - #dict.get(unique_candidates)
        vote_percentage =float(vote_winner)/float(total_votes)
        if vote_winner > highest_votes: 
            highest_votes = vote_winner
            winning_candidate = candidate
            winning_percentage = vote_percentage
        print(f"{candidate}: {vote_percentage:.3%} ({vote_winner})")
 
        writer.writerow({f"{candidate}: {vote_percentage:.3%} ({vote_winner})"})
    writer.writerow({f"-------------------------"})      
    writer.writerow({f"Winner: {winning_candidate}"})
    writer.writerow({f"-------------------------"}) 

print(f"-------------------------") 
print(f"Winner: {winning_candidate}")
print(f"-------------------------") 


