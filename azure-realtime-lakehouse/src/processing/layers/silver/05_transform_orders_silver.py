%run ../config/storage_paths
%run ../utils/layer_writers
from pyspark.sql.functions import from_json, col
df = spark.readStream.format("delta").load(f"{ADLS_BRONZE_URL}/orders")
clean_df = df.withColumn("json", from_json(col("value"), "schema")).select("json.*")
persist_to_layer(clean_df, f"{ADLS_SILVER_URL}/orders", f"{CHECKPOINT_ROOT}/silver_orders")
