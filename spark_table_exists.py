# Databricks notebook source
jdbcUsername = "sqladmin"
jdbcPassword = "Azure$2022"
jdbcHostname = "lkoct.database.windows.net"
jdbcDatabase = "sqldb"
jdbcPort = 1433
jdbcUrl = "jdbc:sqlserver://{0}:{1};database={2};user={3};password={4}".format(jdbcHostname, jdbcPort, jdbcDatabase, jdbcUsername, jdbcPassword)

connectionProperties = {
  "user" : jdbcUsername,
  "password" : jdbcPassword,
  "driver" : "com.microsoft.sqlserver.jdbc.SQLServerDriver"
}

# COMMAND ----------

df = spark.read.jdbc(url=jdbcUrl, table="dbo.orders", properties=connectionProperties)

# COMMAND ----------

df.createOrReplaceTempView('df')

# COMMAND ----------

# MAGIC %sql
# MAGIC create table orders as
# MAGIC select * from df

# COMMAND ----------

if spark._jsparkSession.catalog().tableExists('sales'):
    print("Continue with the remaining code execution")
else:
    spark.sql("select * from sales")
    #raise Exception("table not found")

# COMMAND ----------

try:
    if spark._jsparkSession.catalog().tableExists('sales'):
        print("Continue with the remaining code execution")
    else:
        spark.sql("select * from sales")
        #raise Exception("table not found")
except Exception as ex :
    print(ex)
print("hello")
