from newsapi import NewsApiClient
import json
from kafka import KafkaProducer
from textblob import TextBlob

# Get your free API key from https://newsapi.org/, just need to sign up for an account
key = "8b331c71e2294e45bfae1d93054177df"

# Initialize API endpoint
newsapi = NewsApiClient(api_key=key)

# Define the list of media sources
sources = 'bbc-news,cnn,fox-news,nbc-news,the-guardian-uk,the-new-york-times,the-washington-post,usa-today,independent,daily-mail'

query = 'bitcoin'

# Fetch news articles
all_articles = newsapi.get_everything(q=query,
                                      sources=sources,
                                      from_param='2024-11-01',
                                      to='2024-11-12',
                                      language='en',
                                      sort_by='relevancy')

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092',
                         value_serializer=lambda v: json.dumps(v).encode('utf-8'))


for article in all_articles['articles']:
    title = article['title']
    description = article['description'] or "No description provided"
    source = article['source']['name']

    # Analyze sentiment
    polarity = TextBlob(description).sentiment.polarity  # Polarity ranges from -1 (negative) to 1 (positive)
    
    # Prepare the message
    message = {
        "source": source,
        "title": title,
        "description": description,
        "polarity": polarity
    }

    # Send the message to Kafka
    producer.send('my-news', value=message)
    print(f"Sent to Kafka: {message}")
