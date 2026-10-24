import uuid, random
from faker import Faker
from datetime import datetime
data_generator = Faker()
def create_order_payload():
    return {
        "order_id": f"ORD{uuid.uuid4().hex[:8]}",
        "city": data_generator.city(),
        "order_value": round(random.uniform(50, 2000), 2),
        "event_time": datetime.utcnow().isoformat()
    }
