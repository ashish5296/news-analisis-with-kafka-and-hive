from kafka import KafkaConsumer
import json

# Kafka consumer configuration
topic = "my-news"               
brokers = "localhost:9092"       

# Create the Kafka consumer
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=brokers,
    auto_offset_reset='latest',              
    enable_auto_commit=False,                
    auto_commit_interval_ms=5000   
)

# File path where the data will be saved
file_path = "/home/a_ashish5296/news_data.json"

# Start consuming the data from the topic
for message in consumer:
    # Deserialize the message value (assuming it's in JSON format)
    news_data = json.loads(message.value.decode('utf-8'))

    # Open the JSON file for appending data
    with open(file_path, mode='a', encoding='utf-8') as file:
        # Write the message to the JSON file with timestamp
        json.dump(news_data, file, ensure_ascii=False, indent=4)
        file.write("\n")  # Add a newline for each batch of messages

    print(news_data)
