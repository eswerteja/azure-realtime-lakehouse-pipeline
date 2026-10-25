%run ../config/storage_paths
%run ../utils/layer_writers

from pyspark.sql.functions import window, count, col, sum, when

deliveries_stream = spark.readStream.format("delta").load(f"{ADLS_SILVER_URL}/deliveries")

def process_business_batch(batch_df, batch_id):
    windowed_metrics = batch_df.groupBy(
        window(col("kafka_event_timestamp"), "3 hours").alias("delivery_window"),
        col("city")
    ).agg(
        count("*").alias("total_deliveries"),
        sum(when(col("delivery_status") == "ON_TIME", 1).otherwise(0)).alias("on_time_deliveries"),
        sum(when(col("delivery_status") == "DELAYED", 1).otherwise(0)).alias("delayed_deliveries")
    )
    windowed_metrics.write.format("delta").mode("append").save(f"{ADLS_GOLD_URL}/business_metrics")

(
    deliveries_stream.writeStream
    .foreachBatch(process_business_batch)
    .outputMode("append")
    .option("checkpointLocation", f"{CHECKPOINT_ROOT}/gold_business_metrics")
    .trigger(once=True)
    .start()
)
