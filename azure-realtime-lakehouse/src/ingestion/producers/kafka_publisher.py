import json
from confluent_kafka import Producer
from config.kafka_settings import KAFKA_CONNECTION_CONFIG

kafka_producer = Producer(KAFKA_CONNECTION_CONFIG)

def on_delivery_confirmation(error, message):
    if error is not None:
        print(f"Delivery failed: {error}")
    else:
        print(f"Published to {message.topic()} | Partition {message.partition()}")

def publish_event(topic_name, event_data, event_key=None):
    kafka_producer.produce(
        topic=topic_name,
        key=str(event_key) if event_key else None,
        value=json.dumps(event_data),
        on_delivery=on_delivery_confirmation
    )
    kafka_producer.poll(0)

def flush_producer():
    kafka_producer.flush()
