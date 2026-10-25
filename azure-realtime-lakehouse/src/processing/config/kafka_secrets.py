from azure.keyvault.secrets import SecretClient

def get_kafka_connection_details():
    credentials = dbutils.credentials.getServiceCredentialsProvider('cred-quickcommerce-keyvault')
    vault_url = "https://kv-quickcommerce-dev1.vault.azure.net/"
    client = SecretClient(vault_url=vault_url, credential=credentials)
    
    bootstrap_servers = client.get_secret("kafka-bootstrap-servers").value
    api_key = client.get_secret("kafka-api-key").value
    api_secret = client.get_secret("kafka-api-secret").value
    
    jaas_config = (
        "kafkashaded.org.apache.kafka.common.security.plain.PlainLoginModule required "
        f'username="{api_key}" password="{api_secret}";'
    )
    return bootstrap_servers, jaas_config

KAFKA_BOOTSTRAP_SERVERS, KAFKA_JAAS_CONFIG = get_kafka_connection_details()
