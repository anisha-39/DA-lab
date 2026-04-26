import time 
from textblob import TextBlob 
tweets = [ 
"I love this product! Amazing quality.", 
"Terrible experience with customer service.", 
    "The product is okay, nothing special.", 
    "Absolutely fantastic! Will buy again.", 
    "Worst purchase ever. Completely dissatisfied.", 
    "Meh. It’s just average, not worth the hype." 
] 
def analyze_sentiment(tweet): 
    analysis = TextBlob(tweet) 
    if analysis.sentiment.polarity > 0: 
        return "Positive" 
    elif analysis.sentiment.polarity == 0: 
        return "Neutral" 
    else: 
        return "Negative" 
print("Starting real-time sentiment analysis...\n") 
for tweet in tweets: 
    sentiment = analyze_sentiment(tweet) 
    print(f"Tweet: {tweet}") 
    print(f"Sentiment: {sentiment}\n") 
    time.sleep(2) 