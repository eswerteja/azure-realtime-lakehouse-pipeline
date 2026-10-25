from faker import Faker
from datetime import datetime

data_generator = Faker()
PRODUCT_CATALOG = ["Milk 1L", "Bread", "Eggs", "Fruits", "Vegetables"]

def create_product_payload():
    selected_product = data_generator.random_element(PRODUCT_CATALOG)
    
    return {
        "product_id": f"PRD{data_generator.random_int(1000, 9999)}",
        "product_name": selected_product,
        "category": "Grocery",
        "order_id": f"ORD{data_generator.random_int(100000, 999999)}",
        "store_id": f"STR{data_generator.random_int(100, 999)}",
        "city": data_generator.city(),
        "quantity": data_generator.random_int(1, 5),
        "price": round(data_generator.random_number(digits=2), 2),
        "event_time": datetime.utcnow().isoformat()
    }
