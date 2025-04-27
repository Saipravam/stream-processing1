from kafka import KafkaProducer
import json

producer = None

# Kafka event types
USER_REGISTERED = "USER_REGISTERED"
USER_CREATED = "USER_CREATED"
USER_FETCHED = "USER_FETCHED"
USER_UPDATED = "USER_UPDATED"
USER_DELETED = "USER_DELETED"

def init_kafka_producer():
    global producer
    if producer is None:
        producer = KafkaProducer(
            bootstrap_servers='kafka:9092',
            value_serializer=lambda v: json.dumps(v).encode('utf-8')
        )
    return producer

def _send_event(payload):
    global producer
    if producer is None:
        producer = init_kafka_producer()
    
    future = producer.send('user-events', value=payload)

    # Callbacks
    def on_success(record_metadata):
        print(f"[SUCCESS] Message sent to topic={record_metadata.topic}, partition={record_metadata.partition}, offset={record_metadata.offset}")

    def on_error(excp):
        print(f"[ERROR] Failed to send message: {excp}")

    future.add_callback(on_success)
    future.add_errback(on_error)

    # Force flush immediately
    producer.flush()

def publish_user_registered_event(user):
    payload = {
           "event_type": USER_REGISTERED,
           "id": user.id,
           "name": user.name,
           "email": user.email,
           "phone": user.phone
    }
    _send_event(payload)

def publish_user_created_event(user):
    payload = {
        "event_type": USER_CREATED,
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone
    }
    _send_event(payload)

def publish_user_updated_event(user):
    payload = {
        "event_type": USER_UPDATED,
        "id": user.id,
        "name": user.name,
        "email": user.email,
        "phone": user.phone,
    }
    _send_event(payload)

def publish_user_deleted_event(user_id):
    payload = {
        "event_type": USER_DELETED,
        "id": user_id,
    }
    _send_event(payload)

def publish_users_listed_event():
    payload = {
        "event_type": USER_FETCHED
    }
    _send_event(payload)
