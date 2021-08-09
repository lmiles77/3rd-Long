# Building Machine Learning Model

The raw data used for this machine learning project is 2020 NFL play data. This was a fairly large csv file comprised of 46,189 rows and 43 columns. We decided to build our machine learning project around the analysis of 3rd down plays in the 4th quarter. The ability of an offensive team to successfullly convert third downs is key to their ability to move down the field to score if trailing the other team, or to maintain possession, and run the clock down to end game. 

Through analysis of the raw data I learned there were many data points that were uneeded for this analysis. A new dataframe was created utilizing six columns.

![image](https://user-images.githubusercontent.com/80069183/128651386-bdc57655-5e57-46a2-a9a2-076fcef7adbc.png)

Further analysis revealed there were thousands of cells in the 'Formation', and 'PlayType' columns without values. These empty cells were filled with 'unk'. Additionally, analysis of PlayTypes reveled plays that did not result in positive outcomes. The loc method was use to create dataframe of positive play types.  

How does it work?
Why this specific model?
What is the model's accuracy?
If there are statistics involved, what stats are being included in analysis and why?

# Dyer Observatory Communication Plan

For this challenge our team will communicate through the following methods:

-Slack (share zoom link w/group)

-Group Text Messaging (organize meeting schedule/times)

-Zoom (video conferencing)
