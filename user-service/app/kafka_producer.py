from kafka import KafkaProducer
import json
import os
import time

KAFKA_BROKER = os.getenv("KAFKA_BROKER", "localhost:9092")

producer = KafkaProducer(
    bootstrap_servers=[KAFKA_BROKER],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_event(topic, event):
    producer.send(topic, value=event)
    producer.flush()