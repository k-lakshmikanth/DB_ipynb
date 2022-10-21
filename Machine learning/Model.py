# Databricks notebook source
# MAGIC %md
# MAGIC # This is a model of SBIN stocks

# COMMAND ----------

url="https://raw.githubusercontent.com/k-lakshmikanth/Machine_Learning_Models/main/SBIN/Data/data.csv"
import pandas as pd
train_df = pd.read_csv(url)
train_df

# COMMAND ----------

train_df.info()

# COMMAND ----------

date = train_df.drop('Close',axis=1)
close = train_df[['Close']].values
(date.shape,close.shape)

# COMMAND ----------

date['Date'] = pd.to_numeric(pd.to_datetime(train_df['Date']))

# COMMAND ----------

date = date.values

# COMMAND ----------

type(date)

# COMMAND ----------

from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(date,close)
predicts = reg.predict(X=date)

# COMMAND ----------

reg.score(date,close)*100

# COMMAND ----------

# Graph from YTD
from matplotlib import pyplot as plt

plt.plot(train_df['Date'],close,color = 'red')
plt.plot(train_df['Date'],predicts,color = 'black')
plt.ylabel('Close')
plt.xlabel('Date')
plt.legend(['Real','Prediction'])
plt.rcParams["figure.figsize"] = (40,3)
plt.grid(axis='y')
plt.xticks(rotation=90)
plt.show()

# COMMAND ----------

pred_url = "https://raw.githubusercontent.com/k-lakshmikanth/Machine_Learning_Models/main/SBIN/Data/Predict_data.csv"

pred = pd.read_csv(pred_url).to_dict()

for i in pred.keys():
    pred[i] = pred[i][0]
pred

# COMMAND ----------

import numpy as np

a= np.array([[(np.array(pred['date']+'T15:30:00.000000000').astype('datetime64')).astype('float64'),pred['open'],pred['high'],pred['low'],pred['volume']]])

# COMMAND ----------

a

# COMMAND ----------

# predicted close on date 2022-10-21 03:30pm
reg.predict(a)

# COMMAND ----------

# actual close on date 2022-10-21 03:30pm as per source(Google)
561.65
