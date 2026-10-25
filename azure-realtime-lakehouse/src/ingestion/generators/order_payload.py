import uuid
import random
from faker import Faker
from datetime import datetime

data_generator = Faker()
ORDER_STATUS_FLOW = ["PLACED", "CONFIRMED", "PACKED", "OUT_FOR_DELIVERY", "DELIVERED"]

def create_order_payload():
    return {
        "order_id": f"ORD{uuid.uuid4().hex[:8]}",
        "user_id": f"USR{uuid.uuid4().hex[:6]}",
        "store_id": f"STR{data_generator.random_int(100, 999)}",
        "city": data_generator.city(),
        "order_status": data_generator.random_element(ORDER_STATUS_FLOW),
        "order_value": round(random.uniform(50, 2000), 2),
        "items_count": data_generator.random_int(1, 10),
        "order_time": datetime.utcnow().isoformat(),
        "event_time": datetime.utcnow().isoformat()
    }
