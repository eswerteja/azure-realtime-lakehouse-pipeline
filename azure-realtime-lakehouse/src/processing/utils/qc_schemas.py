from pyspark.sql.types import StructType, StructField, StringType, DoubleType, IntegerType

ORDER_EVENT_SCHEMA = StructType([
    StructField("order_id", StringType(), True),
    StructField("user_id", StringType(), True),
    StructField("store_id", StringType(), True),
    StructField("city", StringType(), True),
    StructField("order_status", StringType(), True),
    StructField("order_value", DoubleType(), True),
    StructField("items_count", IntegerType(), True),
    StructField("order_time", StringType(), True),
    StructField("event_time", StringType(), True)
])

DELIVERY_EVENT_SCHEMA = StructType([
    StructField("delivery_id", StringType(), True),
    StructField("order_id", StringType(), True),
    StructField("rider_id", StringType(), True),
    StructField("store_id", StringType(), True),
    StructField("city", StringType(), True),
    StructField("expected_delivery_minutes", IntegerType(), True),
    StructField("actual_delivery_minutes", IntegerType(), True),
    StructField("delivery_status", StringType(), True),
    StructField("delivery_time", StringType(), True),
    StructField("event_time", StringType(), True)
])

PRODUCT_EVENT_SCHEMA = StructType([
    StructField("product_id", StringType(), True),
    StructField("product_name", StringType(), True),
    StructField("category", StringType(), True),
    StructField("order_id", StringType(), True),
    StructField("store_id", StringType(), True),
    StructField("city", StringType(), True),
    StructField("quantity", IntegerType(), True),
    StructField("price", DoubleType(), True),
    StructField("event_time", StringType(), True)
])

RIDER_EVENT_SCHEMA = StructType([
    StructField("rider_id", StringType(), True),
    StructField("city", StringType(), True),
    StructField("rider_status", StringType(), True),
    StructField("current_orders", IntegerType(), True),
    StructField("event_time", StringType(), True)
])
