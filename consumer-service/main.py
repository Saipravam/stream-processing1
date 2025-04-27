import json
import os
import time
from kafka import KafkaConsumer
from kafka.errors import NoBrokersAvailable

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
        )
        print(" Connected to Kafka successfully!")
        break
    except NoBrokersAvailable:
        print(" Kafka broker not available yet, retrying in 5 seconds...")
        time.sleep(5)

# Start consuming
print(" Starting to consume messages...")

for message in consumer:
    print("=" * 80)
    print(f" Received raw message at offset {message.offset} in partition {message.partition}")
    print(f" Raw message content (bytes): {message.value}")

    try:
        # 1. Decode bytes to string
        message_str = message.value.decode('utf-8')

        # 2. Load JSON string to dict
        message_data = json.loads(message_str)

        print(f" Parsed message: {message_data}")

        # Now safely get event_type
        event_type = message_data.get("event_type")
        print(f" Processing event type: {event_type}")

        #  Manually commit after successful processing
        consumer.commit()
        print(f" Message at offset {message.offset} committed successfully.")

    except Exception as e:
        print(f" Error processing message: {e}")

    print("=" * 80)
