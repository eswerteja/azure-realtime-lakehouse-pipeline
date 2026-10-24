import time
from producers.kafka_publisher import publish_event
from generators.order_payload import create_order_payload
def run():
    while True:
        publish_event("orders", create_order_payload())
        time.sleep(2)
if __name__ == "__main__":
    run()
