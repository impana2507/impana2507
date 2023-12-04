import nltk
import pandas as pd
from nltk.sentiment import SentimentIntensityAnalyzer

def sentiment_analysis(keyword):
    sia = SentimentIntensityAnalyzer()
    sentiment = sia.polarity_scores(keyword)
    
    if sentiment['compound'] >= 0.05:
        return 'Positive'
    elif sentiment['compound'] <= -0.05:
        return 'Negative'
    else:
        return 'Neutral'

# Load the dataset from a CSV file
dataset_path = input("Enter the path to the dataset CSV file: ")
dataset = pd.read_csv(dataset_path)

# Perform sentiment analysis on each row of the dataset
sentiments = dataset['column_name'].apply(sentiment_analysis)  # Replace 'column_name' with the actual column containing the text

# Add the sentiment analysis results to the dataset
dataset['sentiment'] = sentiments

# Write the modified dataset back to a new CSV file
output_path = 'output.csv'  # Enter the desired output path or filename
dataset.to_csv(output_path, index=False)

print("Sentiment analysis completed. Results saved to", output_path)
