# Databricks notebook source


# COMMAND ----------

import mlflow.sklearn
mlflow.sklearn.autolog()

# COMMAND ----------

labely = 'Close'
path = r"/dbfs/mnt/lkoct1/data/Google_Finance/NASDAQ_GOOG_ex.xlsx"

# COMMAND ----------

import pandas as pd

train_df = pd.read_excel(path)[['Date',labely]]
train_df.head()

# COMMAND ----------

X_date = train_df[['Date']].values
y = train_df[[labely]].values
(X_date.shape,y.shape)

# COMMAND ----------


type(X_date)

# COMMAND ----------

X_date

# COMMAND ----------


from sklearn.linear_model import LinearRegression

reg = LinearRegression()
reg.fit(X_date,y)
predicts = reg.predict(X=X_date.astype('float64'))

# COMMAND ----------

from matplotlib import pyplot as plt

plt.plot(X_date,y)
plt.plot(X_date,predicts,color = 'black')
plt.ylabel(labely)
plt.xlabel('Date')
plt.rcParams["figure.figsize"] = (10,3)
plt.grid(axis='y')
plt.show()
