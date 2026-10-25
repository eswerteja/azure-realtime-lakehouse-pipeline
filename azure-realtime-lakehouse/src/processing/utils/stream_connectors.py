def initialize_kafka_stream(topic_name):
    return (
        spark.readStream
        .format("kafka")
        .option("kafka.bootstrap.servers", KAFKA_BOOTSTRAP_SERVERS)
        .option("kafka.security.protocol", "SASL_SSL")
        .option("kafka.sasl.mechanism", "PLAIN")
        .option("kafka.sasl.jaas.config", KAFKA_JAAS_CONFIG)
        .option("kafka.ssl.endpoint.identification.algorithm", "https")
        .option("subscribe", topic_name)
        .option("startingOffsets", "earliest")
        .option("failOnDataLoss", "false")
        .option("maxOffsetsPerTrigger", "50000")
        .load()
    )
