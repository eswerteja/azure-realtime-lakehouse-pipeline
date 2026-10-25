import os
from dotenv import load_dotenv

load_dotenv()

KAFKA_CONNECTION_CONFIG = {
    "bootstrap.servers": os.getenv("KAFKA_BOOTSTRAP_SERVERS"),
    "security.protocol": "SASL_SSL",
    "sasl.mechanisms": "PLAIN",
    "sasl.username": os.getenv("KAFKA_API_KEY"),
    "sasl.password": os.getenv("KAFKA_API_SECRET"),
    "acks": "all"
}

EVENT_TOPICS = {
    "order": os.getenv("ORDER_EVENT_TOPIC"),
    "delivery": os.getenv("DELIVERY_EVENT_TOPIC"),
    "product": os.getenv("PRODUCT_EVENT_TOPIC"),
    "rider": os.getenv("RIDER_EVENT_TOPIC")
}
