%run ../config/storage_paths
%run ../utils/layer_writers

from pyspark.sql.functions import count, col, max, first

orders_stream = spark.readStream.format("delta").load(f"{ADLS_SILVER_URL}/orders")

def process_orders_batch(batch_df, batch_id):
    latest_status_df = batch_df.groupBy("order_id").agg(
        max("ingestion_timestamp").alias("last_seen"),
        first("order_status").alias("current_status")
    )
    aggregated_df = latest_status_df.groupBy("current_status").agg(count("*").alias("order_count"))
    aggregated_df.write.format("delta").mode("overwrite").save(f"{ADLS_GOLD_URL}/orders_status")

(
    orders_stream.writeStream
    .foreachBatch(process_orders_batch)
    .outputMode("complete")
    .option("checkpointLocation", f"{CHECKPOINT_ROOT}/gold_orders_status")
    .trigger(once=True)
    .start()
)
