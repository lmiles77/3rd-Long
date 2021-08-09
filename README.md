# Building Machine Learning Model

The raw data used for this machine learning project is 2020 NFL play data. This was a fairly large csv file comprised of 46,189 rows and 43 columns. We decided to build our machine learning project around the analysis of 3rd down plays in the 4th quarter. This machine learning model project will predict the probability of the offensive team to convert a third down play in the 4th quarter of a game. The ability of an offensive team to successfullly convert third downs is key to their ability to move down the field to score if trailing the other team, or to maintain possession, and run the clock down to end game. 

Through analysis of the raw data I learned there were many data points that would not add value to project. A new dataframe was created utilizing six columns.

![image](https://user-images.githubusercontent.com/80069183/128651386-bdc57655-5e57-46a2-a9a2-076fcef7adbc.png)

Further analysis revealed there were thousands of cells in the 'Formation', and 'PlayType' columns without values. These empty cells were filled with 'unk'. Additionally, analysis of 'PlayType' data reveled plays that did not result in positive outcomes. The loc method was use to create dataframe of positive play types. 

![image](https://user-images.githubusercontent.com/80069183/128653631-73305e8d-5851-4d27-b384-114a4b231a5d.png)

The data was then split into training and testing sets. Features and the target were created. The Y/N data in the 'Successful 3rd Down Y/N' columns were replaced with 1 & 0. With 1 meaning the play was successful and 0 meaning it was not. For this model I utilized logistic regression(binary classification) in the machine learning model 

The training set for the machine learning model included 1377 rows and 9 columns of data. the testing set included 460 rows and 9 columns of data. The image below shows an array of the first 10 predictions made by the model. A one means the play was successful. A zero means the play was not. 

![image](https://user-images.githubusercontent.com/80069183/128655526-1e916933-d2f8-426c-a102-603509d991c1.png)

A look at the feature importantance shows the distance the offensive team has to go in order to reach the first down factors greatly into the plays success. Here the top three factors are 'ToGo'/distance to reach a first down, 'PlayType_SACK'/loss of yards, and 'PlayType_PASS'/pass play. 

![image](https://user-images.githubusercontent.com/80069183/128657422-76a8606c-c1c1-4957-9cdb-af2eccef97d9.png)

The following image shows the probability for a given play to result in a first down or not. The X_test predictions(red) are from the image above. The first prediction shows a 61% probability for this play to be succesful. Some additional characteristics of this play are that the distance to go was 1 yard, formation was under center, and the team ran the ball. The next two plays were from 6 and 8 yards, delivered from the shot gun formation, and were both pass plays. You can also see in the image below that both of these plays had a low probalities of being successful at 45% and 37%.

![image](https://user-images.githubusercontent.com/80069183/128656176-84f3676c-f657-42d1-b456-03f6e623aeda.png)

The accuracy score for this model is 68%. I feel the overall accuracy of the model suffered becasue no feature besides distance had any importance greater that 18%. 

![image](https://user-images.githubusercontent.com/80069183/128656886-63fea06f-67ed-4d46-bcc5-4707c89c71b9.png)

The image below of the classification report shows the main classification metrics precision, recall and f1-score on a per-class basis. This report shows the precision of predictions to have a fairly significant range between them, with a difference of 13 percentage points. The recall for Actual 0 (N) predictions was 69% which was just above Actual 1(Y) at 66%. The F1 score (percent of accuracte positive predictions) predictions for Actual 0, and Actual 1 were 72% and 63%. The last columns displays the number of samples for each set of predictions. 

![image](https://user-images.githubusercontent.com/80069183/128660158-68e25f92-1706-475d-b981-f435fa431efc.png)

Additional machine learning models were also considered for this project, however the logistical regreassion model yielded the highest accuracy percentage.

Balanced Random Forest Classifier 62%
Easy Ensemble AdaBoost Classifier 66%
SMOTEENN (Combination Over/Under) 62%



# Dyer Observatory Communication Plan

For this challenge our team will communicate through the following methods:

-Slack (share zoom link w/group)

-Group Text Messaging (organize meeting schedule/times)

-Zoom (video conferencing)
