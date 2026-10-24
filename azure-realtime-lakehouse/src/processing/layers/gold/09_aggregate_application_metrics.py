%run ../config/storage_paths
df = spark.readStream.format("delta").load(f"{ADLS_SILVER_URL}/orders")
def process_batch(batch_df, batch_id):
    batch_df.groupBy("status").count().write.format("delta").mode("overwrite").save(f"{ADLS_GOLD_URL}/orders_status")
df.writeStream.foreachBatch(process_batch).trigger(once=True).start()
