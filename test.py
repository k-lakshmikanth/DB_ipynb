# Databricks notebook source
url="https://docs.google.com/spreadsheets/d/e/2PACX-1vStEDoehbRz6WNCrvGZrPbDizzqPyS0oY0bQt35GKL2hUu2vrVAtWpJR86DLg0QB5Omdt01RRgDyKdG/pub?gid=0&single=true&output=csv"
import pandas as pd
spark.createDataFrame(pd.read_csv(url)[-33:]).createOrReplaceTempView('data')
def create_table():
    spark.sql("""
    create table sbin as
    select * from data""")
    print('Table SBIN created sucessfully')

# COMMAND ----------

try:
    create_table()
except:
    spark.sql('drop table sbin')
    create_table()

# COMMAND ----------

# MAGIC %sql
# MAGIC select TO_DATE(CAST(UNIX_TIMESTAMP(date, 'dd/MM/yyyy hh:mm:ss') AS TIMESTAMP))
# MAGIC ,open,high,low,close,volume from sbin order by date
