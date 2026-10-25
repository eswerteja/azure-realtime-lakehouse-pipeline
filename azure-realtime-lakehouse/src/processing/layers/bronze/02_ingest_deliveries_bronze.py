%run ../config/kafka_secrets
%run ../config/storage_paths
%run ../utils/stream_connectors
%run ../utils/layer_writers

TOPIC_NAME = "quick_commerce_delivery_events"

raw_stream = initialize_kafka_stream(TOPIC_NAME)

bronze_df = raw_stream.selectExpr(
    "CAST(key AS STRING) AS kafka_key",
    "CAST(value AS STRING) AS raw_payload",
    "topic",
    "partition",
    "offset",
    "timestamp AS kafka_event_timestamp",
    "current_timestamp() AS ingestion_timestamp"
)

persist_to_layer(
    stream_df=bronze_df,
    target_path=f"{ADLS_BRONZE_URL}/deliveries",
    checkpoint_path=f"{CHECKPOINT_ROOT}/bronze_deliveries"
)
