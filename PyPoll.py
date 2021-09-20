import csv
import os

#load file to variable
file_to_load=os.path.join("Resources","election_results.csv")

#create a filename to save
file_to_save=os.path.join("analysis","election_analysis.txt")

#initialize variables
total_votes=0
candidate_options=[]
candidate_votes={}
winning_candidate=""
winning_count=0
winning_percentage=0
county_options=[]
county_votes={}
highest_vote_county=0

#Open the election results and read the file
with open(file_to_load) as election_data:
    file_reader=csv.reader(election_data)

    #Read the header rows thus indexing to second row for the next portion of the code
    headers=next(file_reader)
    
    #step through each row in the CSV file
    for row in file_reader:
        #2. Add to the total vote count
        total_votes+=1
        # get the candidate names
        candidate_name=row[2]
        # get the county name
        county_name=row[1]

        #add to candidate option list if not already there
        if candidate_name not in candidate_options:
            candidate_options.append(candidate_name)

            #Begin tracking the candidate's vote count by setting to zero
            candidate_votes[candidate_name]=0

        #Add a vote count each row of a candidate
        candidate_votes[candidate_name]+=1

        #add to county option list if not already there
        if county_name not in county_options:
            county_options.append(county_name)

            #Begin tracking the county's vote count by setting to zero
            county_votes[county_name]=0

        #Add a vote count each row of a candidate
        county_votes[county_name]+=1


with open(file_to_save,"w") as txt_file:
    #report out the results
    #iterate through the candidate_votes 
    
    election_results = (
    f"\nElection Results\n"
    f"-------------------------\n"
    f"Total Votes: {total_votes:,}\n"
    f"-------------------------\n"
    f"\n"
    f"County Votes\n")
    print(election_results, end="")
    txt_file.write(election_results)
    
    for county_name in county_votes:
        #retrieve the vote count of the county
        cty_votes=county_votes[county_name]
        #calculate percentage of total votes
        cty_vote_percentage=float(cty_votes)/float(total_votes)*100

        if (cty_votes>highest_vote_county):
            highest_vote_county=cty_votes
            highest_county=county_name
 
        county_results = (
                f"{county_name}: {cty_vote_percentage:.1f}% ({cty_votes:,})\n")

        # Print each county's voter count and percentage to the terminal.
        print(county_results)
        #  Save the candidate results to our text file.
        txt_file.write(county_results)
    
    highest_county_summary = (
        f"\n"
        f"-------------------------\n"
        f"Largest County Turnout: {highest_county}\n"
        f"-------------------------\n")
    print(highest_county_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(highest_county_summary)

    #iterate through the candidate_votes 
    for candidate_name in candidate_votes:
        #retrieve the vote count of the candidate
        votes=candidate_votes[candidate_name]
        #calculate percentage of total votes
        vote_percentage=float(votes)/float(total_votes)*100

        if (votes>winning_count) and (vote_percentage>winning_percentage):
            winning_count=votes
            winning_percentage=vote_percentage
            winning_candidate=candidate_name
 
        candidate_results = (
                f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate's voter count and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)
    
    
    # Save the final vote count to the text file.
    winning_candidate_summary = (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Vote Count: {winning_count:,}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
    print(winning_candidate_summary)
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)









