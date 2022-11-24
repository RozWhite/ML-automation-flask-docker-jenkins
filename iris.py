#!/usr/bin/env python
# coding: utf-8

# In[21]:


import numpy as np
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from sklearn.model_selection import StratifiedKFold, cross_val_score
import pickle
import json


# In[26]:


#Load the data as a numpy array , target classes: ['setosa' 'versicolor' 'virginica']
X, y = load_iris(return_X_y=True)


# In[3]:


#print(X.shape , y.shape)


# In[4]:


X_train, X_test, y_train,y_test = train_test_split(X, y, random_state=75 , test_size=0.25)


# In[5]:


#print(X_train.shape , y_test.shape)


# # Build and Train the Model

# In[6]:


lg=LogisticRegression(solver='lbfgs',
                                  max_iter=1000,
                                  multi_class='multinomial')


# In[7]:


lg.fit(X_train, y_train)


# In[8]:


# Cross validation
cv = StratifiedKFold(n_splits=3) 
val_lg = cross_val_score(lg, X_train, y_train, cv=cv).mean()
#print("Validation accuracy: ", val_lg )


# In[9]:


# Save Validation accuracy to JSON
train_metadata = {
    'validation_acc': val_lg
}


# In[17]:


# Serialize and save model
with open("lg.pkl", "wb") as lg_pickle:
    pickle.dump(lg, lg_pickle)


# In[15]:


# Serialize and save metadata
with open("train_metadata.json", 'w') as outfile:
    json.dump(train_metadata, outfile)


# # Load the Model 

# In[18]:


pickle_in = open("lg.pkl","rb")
classifier=pickle.load(pickle_in)


# # Test Data Accuracy

# In[27]:


prediction= classifier.predict(X_test)
test_lg = accuracy_score(y_test,prediction)


# In[28]:


# Save Test accuracy to JSON
test_metadata = {
    'test_acc': test_lg
}


# In[29]:


# Serialize and save metadata
with open("test_metadata.json", 'w') as outfile:
    json.dump(test_metadata, outfile)

