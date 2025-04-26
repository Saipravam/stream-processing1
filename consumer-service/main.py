from kafka import KafkaConsumer
import time

TOPIC_NAME = "user-events"
BOOTSTRAP_SERVERS = "kafka:9092"
GROUP_ID = "user-group"

consumer = None

while consumer is None:
    try:
        print("Trying to connect to Kafka...")
        consumer = KafkaConsumer(
            TOPIC_NAME,
            bootstrap_servers=BOOTSTRAP_SERVERS,
            auto_offset_reset="earliest",
            group_id=GROUP_ID,
        )
        print("Connected to Kafka successfully!")
    except Exception as e:
        print(f"Kafka connection failed: {e}")
        print("Retrying in 5 seconds...")
        time.sleep(5)

# Now consumer is ready, listen forever
for message in consumer:
    print(f"Received message: {message.value.decode('utf-8')}")
