import json
from confluent_kafka import Producer
from config.kafka_settings import KAFKA_CONNECTION_CONFIG
kafka_producer = Producer(KAFKA_CONNECTION_CONFIG)
def publish_event(topic_name, event_data):
    kafka_producer.produce(topic=topic_name, value=json.dumps(event_data))
    kafka_producer.poll(0)
