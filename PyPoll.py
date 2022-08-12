#The data we want to retrieve
#The total number of votes cast
#The percentage of votes each candidate won
#The total number of votes each candidate won
#The winner of the election based off the popular vote


#add our dependencies
import csv

import os

#Assign a variable for the file to load and path
file_to_load = os.path.join("Resources/election_results.csv")

#Assign a filename variable to a direct or indirect path to the file
file_to_save = os.path.join("analysis", "election_analysis.txt")

# total votes counter 
total_votes = 0

# Candidate Options
candidate_options = [] 

# declare the empty dictionary
candidate_votes = {} 

#winning tracker

winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open election data and read the file
with open(file_to_load) as election_data:
    file_reader =  csv.reader(election_data)


    #read and print the header row
    headers = next(file_reader)
    

    #print each row in the csv file
    for row in file_reader:

        #add to the total vote count
        total_votes += 1

        #print the candidiate name from each row
        candidate_name = row[2]

        # if the candidiate does not match any exsisting 
        if candidate_name not in candidate_options:
        
        # add the candidiate name to the candidate list
            candidate_options.append(candidate_name)

            #begin tracking that candidates votes
            candidate_votes[candidate_name] = 0

            #add a vote to that candidates count
        candidate_votes[candidate_name] += 1

# Determine the percentage of votes for each candidate by looping thru the counts  
# 1 Iterate the candidiate list
for candidate_name in candidate_votes:
    
    # 2 retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]

    #3 calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100


    # Determine winnien vote coutn and candidate 
    # Determine if the votes is greater then the winning count

    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true set winning count = votes and winning percent = to vote percentage

        winning_count = votes
        winning_percentage = vote_percentage

        #3 set winning candidate equal to their name

        winning_candidate = candidate_name

    #print the candidate name and percent of vote
    print(f"{candidate_name}: {vote_percentage:1f}% ({votes:,})\n")

    winning_candidate_summary = (
        f"--------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"---------------\n")

print(winning_candidate_summary)















    #to do read and perform the analysis here

    


# print each row in the csv file
#for row in file_reader:
 #   print(row)


#using with statement open the file as a test file
#with open(file_to_save, "w") as txt_file:

    #write data to the file
    #txt_file.write("Counties in the Election\n-------------------------\nArapahoe\nDenver\nJefferson")



    #to do - perform analysis 
    #print(election_data)




#Removed the close code line
