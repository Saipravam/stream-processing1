from kafka import KafkaProducer
from kafka.errors import NoBrokersAvailable
import time

def create_producer_with_retry(max_retries=10, delay=5, bootstrap_servers=["kafka:9092"]):
    """Create Kafka Producer with retry mechanism."""
    for attempt in range(1, max_retries + 1):
        try:
            print(f"[Kafka Producer] Attempt {attempt} to connect to Kafka at {bootstrap_servers}")
            producer = KafkaProducer(bootstrap_servers=bootstrap_servers)
            print("[Kafka Producer] Connected successfully!")
            return producer
        except NoBrokersAvailable as e:
            print(f"[Kafka Producer] Attempt {attempt} failed: NoBrokersAvailable. Retrying in {delay} seconds...")
            time.sleep(delay)
        except Exception as e:
            print(f"[Kafka Producer] Attempt {attempt} failed with unexpected error: {e}. Retrying in {delay} seconds...")
            time.sleep(delay)

    raise Exception(f"[Kafka Producer] Could not connect to Kafka after {max_retries} retries!")

