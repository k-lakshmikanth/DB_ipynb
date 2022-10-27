# Databricks notebook source
df = spark.read.csv('dbfs:/FileStore/first_dt1.csv',inferSchema=True,header=True)
df.display()

# COMMAND ----------

df.write.format("parquet").saveAsTable('parquet_table')

# COMMAND ----------

spark.table('parquet_table').display()

# COMMAND ----------

from delta.tables import DeltaTable

deltatable = DeltaTable.convertToDelta(spark,"parquet.`dbfs:/user/hive/warehouse/parquet_table`")


