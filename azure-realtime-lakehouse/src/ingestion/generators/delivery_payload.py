import uuid
from faker import Faker
from datetime import datetime

data_generator = Faker()
STANDARD_DELIVERY_TIME = 15

def create_delivery_payload():
    expected_time = STANDARD_DELIVERY_TIME
    actual_time = data_generator.random_int(10, 25)
    delivery_status = "ON_TIME" if actual_time <= expected_time else "DELAYED"
    
    return {
        "delivery_id": f"DLV{uuid.uuid4().hex[:8]}",
        "order_id": f"ORD{uuid.uuid4().hex[:8]}",
        "rider_id": f"RID{uuid.uuid4().hex[:6]}",
        "store_id": f"STR{data_generator.random_int(100, 999)}",
        "city": data_generator.city(),
        "expected_delivery_minutes": expected_time,
        "actual_delivery_minutes": actual_time,
        "delivery_status": delivery_status,
        "delivery_time": datetime.utcnow().isoformat(),
        "event_time": datetime.utcnow().isoformat()
    }
