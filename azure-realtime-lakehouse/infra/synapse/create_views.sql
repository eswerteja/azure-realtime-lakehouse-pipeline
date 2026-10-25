-- Quick Commerce Data Lakehouse - Synapse Views
CREATE DATABASE IF NOT EXISTS quickcom;
GO

USE quickcom;
GO

IF NOT EXISTS (SELECT * FROM sys.symmetric_keys WHERE symmetric_key_id = 101)
    CREATE MASTER KEY ENCRYPTION BY PASSWORD = 'YourVeryStrongPassword@123!';
GO

IF EXISTS (SELECT * FROM sys.database_scoped_credentials WHERE name = 'WorkspaceManagedIdentity')
    DROP DATABASE SCOPED CREDENTIAL WorkspaceManagedIdentity;
GO

CREATE DATABASE SCOPED CREDENTIAL WorkspaceManagedIdentity
WITH IDENTITY = 'Managed Identity';
GO

IF EXISTS (SELECT * FROM sys.external_data_sources WHERE name = 'QuickComDataLake')
    DROP EXTERNAL DATA SOURCE QuickComDataLake;
GO

CREATE EXTERNAL DATA SOURCE QuickComDataLake
WITH (
    LOCATION = 'https://saquickcommercedev.dfs.core.windows.net/quickcom',
    CREDENTIAL = WorkspaceManagedIdentity
);
GO

DROP VIEW IF EXISTS gold_business_metrics;
DROP VIEW IF EXISTS gold_order_status;
DROP VIEW IF EXISTS gold_product_popularity;
DROP VIEW IF EXISTS gold_rider_status;
DROP VIEW IF EXISTS silver_orders;
DROP VIEW IF EXISTS silver_products;
DROP VIEW IF EXISTS silver_riders;
DROP VIEW IF EXISTS silver_deliveries;
GO

CREATE VIEW gold_business_metrics AS
SELECT * FROM OPENROWSET(BULK 'gold/business_metrics/', DATA_SOURCE = 'QuickComDataLake', FORMAT = 'DELTA') AS t;
GO

CREATE VIEW gold_order_status AS
SELECT * FROM OPENROWSET(BULK 'gold/orders_status/', DATA_SOURCE = 'QuickComDataLake', FORMAT = 'DELTA') AS t;
GO

CREATE VIEW gold_product_popularity AS
SELECT * FROM OPENROWSET(BULK 'gold/product_popularity/', DATA_SOURCE = 'QuickComDataLake', FORMAT = 'DELTA') AS t;
GO

CREATE VIEW gold_rider_status AS
SELECT * FROM OPENROWSET(BULK 'gold/rider_status/', DATA_SOURCE = 'QuickComDataLake', FORMAT = 'DELTA') AS t;
GO

CREATE VIEW silver_orders AS
SELECT * FROM OPENROWSET(BULK 'silver/orders/', DATA_SOURCE = 'QuickComDataLake', FORMAT = 'DELTA') AS t;
GO

CREATE VIEW silver_products AS
SELECT * FROM OPENROWSET(BULK 'silver/products/', DATA_SOURCE = 'QuickComDataLake', FORMAT = 'DELTA') AS t;
GO

CREATE VIEW silver_riders AS
SELECT * FROM OPENROWSET(BULK 'silver/riders/', DATA_SOURCE = 'QuickComDataLake', FORMAT = 'DELTA') AS t;
GO

CREATE VIEW silver_deliveries AS
SELECT * FROM OPENROWSET(BULK 'silver/deliveries/', DATA_SOURCE = 'QuickComDataLake', FORMAT = 'DELTA') AS t;
GO
