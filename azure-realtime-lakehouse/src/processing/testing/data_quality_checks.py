%run ../config/storage_paths

def validate_layer(layer_name, path):
    try:
        df = spark.read.format("delta").load(path)
        count = df.count()
        print(f"{layer_name}: {count} rows found.")
    except Exception as e:
        print(f"Error reading {layer_name}: {e}")

validate_layer("Bronze Orders", f"{ADLS_BRONZE_URL}/orders/")
validate_layer("Silver Orders", f"{ADLS_SILVER_URL}/orders/")
validate_layer("Gold Order Status", f"{ADLS_GOLD_URL}/orders_status/")
