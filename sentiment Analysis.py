# sentiment_analysis_np_pd.py

import pandas as pd
import numpy as np

# Sample data: You can also read from CSV
data = {
    'text': [
        "I love this product, it's amazing!",
        "This is the worst experience ever.",
        "The service was okay, nothing special.",
        "Absolutely fantastic quality and service.",
        "I am not happy with this item."
    ]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Define lists of positive and negative words
positive_words = ['love', 'amazing', 'fantastic', 'good', 'happy', 'great', 'excellent']
negative_words = ['worst', 'bad', 'terrible', 'boring', 'sad', 'awful', 'not happy']

# Function to calculate sentiment
def get_sentiment(text):
    text_lower = text.lower()
    pos_count = np.sum([word in text_lower for word in positive_words])
    neg_count = np.sum([word in text_lower for word in negative_words])
    
    if pos_count > neg_count:
        return "Positive"
    elif neg_count > pos_count:
        return "Negative"
    else:
        return "Neutral"

# Apply sentiment function to DataFrame
df['sentiment'] = df['text'].apply(get_sentiment)

# Display results
print(df)
