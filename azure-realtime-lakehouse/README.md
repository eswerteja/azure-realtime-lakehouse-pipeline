# Azure Real-Time Lakehouse Pipeline

End-to-end real-time data pipeline implementing the Medallion Architecture on Azure. Features Confluent Kafka ingestion, Databricks Structured Streaming with Delta Lake, and Azure Synapse Serverless SQL serving. Delivers low-latency operational insights through interactive Power BI dashboards for Quick Commerce analytics.

Tech Stack
- Ingestion: Apache Kafka (Confluent Cloud), Python (Faker)
- Processing: Databricks (PySpark, Structured Streaming)
- Storage: Azure Data Lake Gen2 (Delta Lake)
- Serving: Azure Synapse Analytics (Serverless SQL)
- Visualization: Power BI
- Security: Azure Key Vault, Managed Identities

Project Structure
- src/ingestion/: Python scripts simulating live order/delivery events.
- src/processing/: PySpark notebooks implementing the Medallion Architecture.
- infra/synapse/: SQL scripts creating views over Delta tables.

Key Features
- Real-Time Ingestion: Generates 4 concurrent event streams (Orders, Deliveries, Riders, Products).
- Medallion Architecture: 
  - Bronze: Raw JSON ingestion with Kafka metadata preservation.
  - Silver: Schema enforcement, JSON parsing, and data quality filtering.
  - Gold: Windowed aggregations and stateful tracking for business KPIs using foreachBatch for deterministic output.
- Fault Tolerance: Uses checkpointing and watermarks to handle late-arriving data.
