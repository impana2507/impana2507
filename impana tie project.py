#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

# Step 1: Load data from CSV file
data = pd.read_csv('your_dataset.csv')

# Step 2: Data Cleaning
def clean_text(text):
    # Remove special characters and numbers
    text = re.sub('[^a-zA-Z]', ' ', text)
    
    # Convert text to lowercase
    text = text.lower()
    
    # Tokenize the text into individual words
    words = text.split()
    
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [word for word in words if word not in stop_words]
    
    # Lemmatize words
    lemmatizer = WordNetLemmatizer()
    words = [lemmatizer.lemmatize(word) for word in words]
    
    # Join the cleaned words back into a single string
    cleaned_text = ' '.join(words)
    
    return cleaned_text

# Apply the clean_text() function to the 'text' column and create a new column for cleaned text
data['cleaned_text'] = data['text'].apply(clean_text)


# In[ ]:




