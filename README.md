# Election Analysis
## Purpose of Election Audit
Colorado has three voting methods for the election process in their congressional precinct.  These are mail-in ballots, punch cards, and direct recoding electronic machines.  The Colorado board of elections has compiled these three voting tallies into a comma delimited file for analysis, and it is desired to write a Python program to perform the analysis.  As an overview report, it is desired to confirm the total votes, total votes for each candidate with percentage of total, and the election winner.  Then a more detailed by county analysis is desired.  This python program can then be leveraged for other voter analysis in senatorial districts and local elections.

## Election Audit Results
* Total Votes in Congressional Election was
  *  ```369,711```

* By County Votes Results -- Percent of Total and (Total Votes)
    - Jefferson: 10.5% (38,855)
    - ```Denver: 82.8% (306,055)```
    - Arapahoe: 6.7% (24,801)  <br>

* County with the Largest Nummber of Votes
  * ```Denver```

* Candidate Votes Results -- Percent of Total and (Total Votes)
  - Charles Casper Stockham: 23.0% (85,213)
  - ```Diana DeGette: 73.8% (272,892)```
  - Raymon Anthony Doane: 3.1% (11,606)  <br>

* Election Winner -- Percent of Total and (Total Votes)
  - Winner: ```Diana DeGette```
  - Winning Percentage: ```73.8%```
  - Winning Vote Count: ```272,892```

### Python File Output
These election analysis results are also written out to a text file and the terminal as shown below.

![alt text](https://github.com/jj2773/Election_Analysis/blob/main/analysis/python_analysis_output.PNG)

## Election Audit Summary
In summary, this python code could be used for any election with some adjustements.  For example, if it was desired to have an election analysis where the plurality rule applies (e.g. Senatorial elections).  Then the below code block if statement could be changed to just check the vote total counts and not require the percentage of votes.  It should be noted that the code could also be changed to allow the user to input the election type so that the correct if statement code block is selected giving more flexibility to various election analysis.  


![alt text](https://github.com/jj2773/Election_Analysis/blob/main/analysis/ifstatement_counts_and_percentage.PNG)