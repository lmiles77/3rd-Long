#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
from pathlib import Path
from collections import Counter


# In[2]:


import warnings
warnings.filterwarnings('ignore')
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split


# In[3]:


# Load the .csv dataset.
file_path = "../Resources/Use me 2020 NFL 3rd & Long Raw Dataset.csv"
df = pd.read_csv(file_path)
df


# In[4]:



df.columns


# In[5]:


df["OffenseTeam"].unique()


# In[6]:


#Keep
df = df[['Quarter', 'OffenseTeam', 'DefenseTeam' , 'Down' , 'ToGo', 'Yards', 'Yards (+,-)', 'Successful 3rd Down Y/N' , 'Formation','PlayType', 'GameDate']]
df.head()


# In[7]:


df.isna().sum()


# In[8]:


#Drop all null values
df = df.dropna()
df.head()


# In[9]:


playlist=df['PlayType'].unique().tolist()
playlist2=['PASS','RUSH','FUMBLE','SACK','SCRAMBLE']


# In[10]:


q4_df=df.loc[(df['Quarter']==4)&       (df['Down']== 3)&      (df['PlayType'].isin(playlist2))      ].reset_index()


# In[11]:


q4_df['PlayType'].value_counts()


# In[12]:


q4_df


# # Split Data into Training and Testing

# In[13]:


# Create our features
y = q4_df["Successful 3rd Down Y/N"]
X = q4_df.drop("Successful 3rd Down Y/N", axis=1)
X = pd.get_dummies(X)


# In[14]:


# Create our target
y = y.replace({"N":0, "Y":1})
y.value_counts()


# In[15]:


X.describe()


# In[16]:


from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

X_train, X_test, y_train, y_test = train_test_split(X, 
                                                    y, 
                                                    random_state=1)
# Creating a StandardScaler instance.
scaler = StandardScaler()
# Fitting the Standard Scaler with the training data.
X_scaler = scaler.fit(X_train)

# Scaling the data.
X_train_scaled = X_scaler.transform(X_train)
X_test_scaled = X_scaler.transform(X_test)


# # Logistic Regression

# In[17]:


from sklearn.linear_model import LogisticRegression
classifier = LogisticRegression(solver='lbfgs', random_state=1)
classifier


# In[18]:


# Train the data
classifier.fit(X_train, y_train)


# In[19]:





# In[20]:


from sklearn.metrics import accuracy_score
accuracy_score(y_test, predictions)


# # Balanced Random Forest Classifier

# In[21]:


# Resample the training data with the BalancedRandomForestClassifier
# Create a random forest classifier.
from imblearn.ensemble import BalancedRandomForestClassifier
from sklearn.metrics import balanced_accuracy_score
from sklearn.metrics import confusion_matrix
from imblearn.metrics import classification_report_imbalanced
brf_model = BalancedRandomForestClassifier(n_estimators=100, random_state=78) 
# Fitting the model
brf_model = brf_model.fit(X_train_scaled, y_train)
y_pred = brf_model.predict(X_test_scaled)


# In[22]:


# Calculated the balanced accuracy score
# Calculating the accuracy score.
acc_score = balanced_accuracy_score(y_test,y_pred)
acc_score


# In[23]:


# Display the confusion matrix
# Calculating the confusion matrix.
cm = confusion_matrix(y_test, y_pred)

# Create a DataFrame from the confusion matrix.
cm_df = pd.DataFrame(
    cm, index=["Actual 0", "Actual 1"], columns=["Predicted 0", "Predicted 1"])

cm_df


# In[24]:


from sklearn.metrics import confusion_matrix, accuracy_score, classification_report
# Print the imbalanced classification report
# Displaying results
print("Confusion Matrix")
display(cm_df)
print(f"Balanced Accuracy Score : {acc_score}")
print("Classification Report")
print(classification_report(y_test, y_pred))


# In[25]:


# List the features sorted in descending order by feature importance
importances = brf_model.feature_importances_
sorted(zip(importances, X.columns), reverse=True)


# # Easy Ensemble AdaBoost Classifier

# In[26]:


# Train the EasyEnsembleClassifier
from imblearn.ensemble import EasyEnsembleClassifier
classifier = EasyEnsembleClassifier(n_estimators=100)

classifier.fit(X_train_scaled, y_train)
predictions = classifier.predict(X_test_scaled)


# In[27]:


# Calculated the balanced accuracy score
from sklearn.metrics import confusion_matrix
from sklearn.metrics import accuracy_score
from sklearn.metrics import classification_report
acc_score = accuracy_score(y_test, y_pred)
print(f"Accuracy Score : {acc_score}")


# In[28]:


# Display the confusion matrix
cm = confusion_matrix(y_test, y_pred)
cm_df = pd.DataFrame(
   cm, index=["Actual 0", "Actual 1"],
   columns=["Predicted 0", "Predicted 1"]
)
display(cm_df)


# In[29]:


# Print the imbalanced classification report
print("Classification Report")
print(classification_report(y_test, y_pred))


# # Combination (Over and Under)

# In[30]:


# Resample the training data with SMOTEENN
from imblearn.combine import SMOTEENN

smote_enn = SMOTEENN(random_state=0)
X_resampled, y_resampled = smote_enn.fit_resample(X, y)
Counter(y_resampled)


# In[31]:


# Train the Logistic Regression model using the resampled data
from sklearn.linear_model import LogisticRegression
model = LogisticRegression(solver='lbfgs', random_state=1)
model.fit(X_resampled, y_resampled)


# In[32]:


# Calculated the balanced accuracy score
from sklearn.metrics import balanced_accuracy_score

balanced_accuracy_score(y_test, y_pred)


# In[33]:


# Display the confusion matrix
from sklearn.metrics import confusion_matrix

y_pred = model.predict(X_test)
confusion_matrix(y_test, y_pred)


# In[34]:


# Print the imbalanced classification report
from imblearn.metrics import classification_report_imbalanced

print(classification_report_imbalanced(y_test, y_pred))


# # SMOTE Oversampling

# In[35]:


# Resample the training data with SMOTE
from imblearn.over_sampling import SMOTE
X_resampled, y_resampled = SMOTE(random_state=1,
sampling_strategy='auto').fit_resample(
   X_train, y_train)

Counter(y_resampled)


# In[36]:


# Train the Logistic Regression model using the resampled data
model = LogisticRegression(solver='lbfgs', random_state=1)
model.fit(X_resampled, y_resampled)


# In[37]:


# Train the Logistic Regression model using the resampled data
model = LogisticRegression(solver='lbfgs', random_state=1)
model.fit(X_resampled, y_resampled)


# In[38]:


# Display the confusion matrix
confusion_matrix(y_test, y_pred)


# In[39]:


# Print the imbalanced classification report
print(classification_report_imbalanced(y_test, y_pred))


# In[ ]:




