## Real-Time News Sentiment Analysis Pipeline
This project builds a real-time data pipeline that fetches news articles using the NewsAPI, performs sentiment analysis using TextBlob, and stores the data in HDFS for querying using Apache Hive.

## Project Overview
# Goal:
To extract meaningful insights from online news articles using a real-time ETL pipeline.

# Tools & Technologies:
Python
TextBlob (for sentiment analysis)
Apache Kafka (Producer & Consumer)
HDFS (Hadoop Distributed File System)
Apache Hive
NewsAPI
Jupyter Notebook

# Pipeline Workflow
Fetch News Articles
Use NewsAPI to collect recent articles in Python.
Free tier limits: 100 API calls/day, last 30 days.

# Kafka Producer
Streams article data into a Kafka topic.
Runs sentiment analysis with TextBlob.

# Kafka Consumer
Reads the article data.
Saves the result to a local file.
Uploads it to HDFS using hdfs dfs -copyFromLocal.

# Apache Hive
Creates Hive tables using data stored in HDFS.
Executes SQL queries to gain insights from the dataset.

