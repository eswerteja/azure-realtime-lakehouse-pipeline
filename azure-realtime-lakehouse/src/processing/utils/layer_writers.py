def persist_to_layer(stream_df, target_path, checkpoint_path):
    stream_df.writeStream.format("delta").outputMode("append").option("checkpointLocation", checkpoint_path).trigger(availableNow=True).start(target_path)
