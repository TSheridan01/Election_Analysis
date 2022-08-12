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

#open election data and read the file
with open(file_to_load) as election_data:
    file_reader =  csv.reader(election_data)


    #read and print the header row
    headers = next(file_reader)
    print(headers)
















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
