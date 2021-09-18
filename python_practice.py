#print("Hello World")

# Example 1
# How many votes did you get?
# my_votes = int(input("How many votes did you get in the election? "))
#  Total votes in the election
#total_votes = int(input("What is the total votes in the election? "))
# Calculate the percentage of votes you received.
#percentage_votes = (my_votes / total_votes) * 100
#print("I received " + str(percentage_votes)+"% of the total votes.")

# Example 2

#counties = ["Arapahoe","Denver","Jefferson"]
#if counties[1] == 'Denver':
#    print(counties[1])

# Example 3

#temperature = int(input("What is the temperature outside? "))

#if temperature > 80:
#    print("Turn on the AC.")
#else:
#    print("Open the windows.")



# Example 4

#counties = ["Arapahoe","Denver","Jefferson"]

#if "El Paso" not in counties:
#    print('El Paso is not in the list of counties.')
#else:
#    print('El Paso is in the list of counties')

# Example 5

#voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                {"county":"Denver", "registered_voters": 463353},
#                {"county":"Jefferson", "registered_voters": 432438}]

                
#print('list dictionary')
#for iterator in voting_data:
#    print(iterator)

#print('list county components')
#for iterator in voting_data:
#    print(iterator['county'])

#print('list registered_voters components')
#for iterator in voting_data:
#    print(iterator['registered_voters'])



#print('iterate to get each dictionary')
#for i in range(len(voting_data)):
#    print(voting_data[i])

#print('Nested Iteration to get key values')
#for county_dict in voting_data:
#    for value in county_dict.values():
#        print(value)
    

#print('iterate to get dictionary values')
#for county_dict in voting_data:
#        print(county_dict.values())

#print('Interesting that iterator is a vector')
#for county_dict in voting_data:
#    print(county_dict['registered_voters'])


#print('Interesting that iterator is a vector')
#for i in voting_data:
#    print(i['registered_voters'])



#counties_dict = {"Arapahoe": 369237, "Denver":413229, "Jefferson": 390222}

#print('typical print statement')
#for county, voters in counties_dict.items():
#    print(county + " county has " + str(voters) + " registered voters.")

#print('leveraging f strings')
#for county, voters in counties_dict.items():
#    print(f"{county} county has {voters} registered voters.")


#candidate_votes = int(input("How many votes did the candidate get in the election? "))
#total_votes = int(input("What is the total number of votes in the election? "))
#message_to_candidate = (
#    f"You received {candidate_votes:,} number of votes. "
#    f"The total number of votes in the election was {total_votes:,}. "
#    f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

#print(message_to_candidate)


#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#for i in counties_dict:
#    message_output=(
#            f"{i} county has {counties_dict[i]:,} registered voters."
#    )
#    print(message_output)




#voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

#for i in voting_data:
#    message_output=(f"{i['county']} county has {i['registered_voters']:,} registered voters."
#    )
#    print(message_output)


#counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

#print(dir(counties_dict))
















import datetime as dt

now=dt.datetime.now()

print("The time right now is",now)








    






