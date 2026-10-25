from faker import Faker
from datetime import datetime

data_generator = Faker()
RIDER_STATUS_OPTIONS = ["AVAILABLE", "BUSY", "OFFLINE"]

def create_rider_payload():
    return {
        "rider_id": f"RID{data_generator.random_int(1000, 9999)}",
        "city": data_generator.city(),
        "rider_status": data_generator.random_element(RIDER_STATUS_OPTIONS),
        "current_orders": data_generator.random_int(0, 3),
        "event_time": datetime.utcnow().isoformat()
    }
