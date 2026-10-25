import time
from producers.kafka_publisher import publish_event, flush_producer
from config.kafka_settings import EVENT_TOPICS
from generators.order_payload import create_order_payload
from generators.delivery_payload import create_delivery_payload
from generators.product_payload import create_product_payload
from generators.rider_payload import create_rider_payload

def run_event_simulation():
    print("Starting Quick Commerce Event Simulation...")
    while True:
        publish_event(EVENT_TOPICS["order"], create_order_payload(), key="order")
        publish_event(EVENT_TOPICS["delivery"], create_delivery_payload(), key="delivery")
        publish_event(EVENT_TOPICS["product"], create_product_payload(), key="product")
        publish_event(EVENT_TOPICS["rider"], create_rider_payload(), key="rider")
        time.sleep(2)

if __name__ == "__main__":
    try:
        run_event_simulation()
    except KeyboardInterrupt:
        print("\nStopping event simulator...")
        flush_producer()
