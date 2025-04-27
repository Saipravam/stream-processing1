from kafka import KafkaProducer
import json
import os

producer = None

# Kafka config
# KAFKA_BOOTSTRAP_SERVERS = os.getenv("KAFKA_BOOTSTRAP_SERVERS", "kafka:9092")
# KAFKA_TOPIC = os.getenv("KAFKA_TOPIC", "user-events")

# app/kafka_producer.py

USER_CREATED = "USER_CREATED"
USER_FETCHED = "USER_FETCHED"
USER_UPDATED = "USER_UPDATED"
USER_DELETED = "USER_DELETED"

# Create Kafka producer
def init_kafka_producer():
    global producer
    if producer is None:
      producer = KafkaProducer(
        bootstrap_servers='kafka:9092',
        value_serializer=lambda v: json.dumps(v).encode('utf-8')
    )
    return producer

# Define success and error handlers
def on_success(record_metadata):
        print(f"[SUCCESS] Message sent to topic={record_metadata.topic}, partition={record_metadata.partition}, offset={record_metadata.offset}")

def on_error(excp):
        print(f"[ERROR] Failed to send message: {excp}")

def publish_user_created_event(user):
    global producer
    if producer is None:
        producer = init_kafka_producer()
    user_data = {
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
    }
     # Send the message
    future = producer.send('user-events', value=user_data)
    future.add_callback(on_success)
    future.add_errback(on_error)
    producer.flush()

def publish_user_updated_event(user):
    global producer
    if producer is None:
        producer = init_kafka_producer()
    user_data = {
        "event_type": "USER_UPDATED",
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
    }
    future = producer.send('user-events', value=user_data)
    future.add_callback(on_success)
    future.add_errback(on_error)
    producer.flush()

def publish_user_deleted_event(user_id):
    global producer
    if producer is None:
        producer = init_kafka_producer()
    user_data = {
        "event_type": "USER_DELETED",
        "id": user_id,
    }
    future = producer.send('user-events', value=user_data)
    future.add_callback(on_success)
    future.add_errback(on_error)
    producer.flush()

def publish_users_listed_event():
    global producer
    if producer is None:
        producer = init_kafka_producer()
    user_data = {
        "event_type": "USERS_LISTED"
    }
    future = producer.send('user-events', value=user_data)
    future.add_callback(on_success)
    future.add_errback(on_error)
    producer.flush()