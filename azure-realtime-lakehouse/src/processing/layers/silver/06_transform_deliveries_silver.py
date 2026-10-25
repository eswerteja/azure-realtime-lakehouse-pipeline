%run ../utils/qc_schemas
%run ../config/storage_paths
%run ../utils/layer_writers

from pyspark.sql.functions import from_json, col, current_timestamp

raw_stream = spark.readStream.format("delta").load(f"{ADLS_BRONZE_URL}/deliveries")

clean_df = (
    raw_stream
    .withColumn("parsed_payload", from_json(col("raw_payload"), DELIVERY_EVENT_SCHEMA))
    .select("parsed_payload.*", "kafka_event_timestamp")
    .filter(col("delivery_id").is_not_null())
    .withColumn("ingestion_timestamp", current_timestamp())
)

persist_to_layer(
    stream_df=clean_df,
    target_path=f"{ADLS_SILVER_URL}/deliveries",
    checkpoint_path=f"{CHECKPOINT_ROOT}/silver_deliveries"
)
