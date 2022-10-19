# Databricks notebook source
path = r"/dbfs/mnt/lkoct1/data/Google_Finance/NASDAQ_GOOG_ex.xlsx"

# COMMAND ----------

pip install openpyxl 

# COMMAND ----------

import pandas as pd

spark.createDataFrame(pd.read_excel(path)).createOrReplaceTempView('df')
