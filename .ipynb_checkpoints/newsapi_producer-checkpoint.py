# -*- coding: utf-8 -*-
"""NewsAPI_Producer.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ffU2vdapKws1BnooyM-NWesssbVT-8n1

# News API
This API can get news articles from different sources and different topics.

---


Documentation for Python API can be found at:
https://github.com/mattlisiv/newsapi-python
"""

'''
You do need to install following packages using pip package manager
pip install newsapi
pip install newsapi-python
pip install kafka-python
'''
from newsapi import NewsApiClient
import json
from kafka import KafkaProducer

# Get your free API key from https://newsapi.org/, just need to sign up for an account
key = "8b331c71e2294e45bfae1d93054177df"

# Initialize api endpoint
newsapi = NewsApiClient(api_key=key)

# Define the list of media sources
sources = 'reuters,the-guardian-uk,the-new-york-times,the-washington-post'

# /v2/everything
all_articles = newsapi.get_everything(q='AAPL',
                                      sources=sources,
                                      language='en')

# Print the titles of the articles
for article in all_articles['articles']:
    print(article['title'])
    producer = KafkaProducer(bootstrap_servers='localhost:9092')
    producer.send('my-news', json.dumps(article).encode('utf-8'))