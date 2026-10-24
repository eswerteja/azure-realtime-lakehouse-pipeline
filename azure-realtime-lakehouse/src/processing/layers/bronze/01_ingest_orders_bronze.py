%run ../config/storage_paths
%run ../utils/layer_writers
df = spark.readStream.format("kafka").option("subscribe", "orders").load()
persist_to_layer(df, f"{ADLS_BRONZE_URL}/orders", f"{CHECKPOINT_ROOT}/bronze_orders")
