CREATE VIEW gold_business_metrics AS
SELECT * FROM OPENROWSET(BULK 'gold/business_metrics/', DATA_SOURCE = 'QuickComDataLake', FORMAT = 'DELTA') AS t;
