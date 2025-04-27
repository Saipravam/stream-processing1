import json
import os
import time
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

# KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
# KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "user-events")

KAFKA_BROKER = "kafka:9092"
TOPIC_NAME = "user-events"

# Retry loop to wait for Kafka
while True:
    try:
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=KAFKA_BROKER,
            group_id="my-consumer-group",
            auto_offset_reset="earliest",
            enable_auto_commit=False,
            group_id='my-consumer-group'
        )
        print("Connected to Kafka successfully!")
        break
    except NoBrokersAvailable:
        print("Kafka broker not available yet, retrying in 5 seconds...")
        time.sleep(5)

# Now you can start consuming messages
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")