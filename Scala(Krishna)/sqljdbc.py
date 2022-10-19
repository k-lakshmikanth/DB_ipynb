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

df = spark.read.jdbc(url=jdbcUrl, table="(select * from [SalesLT].[Product]) a", properties=connectionProperties)

# COMMAND ----------

df.write.jdbc(url=jdbcUrl, table="SalesLT.Product2", mode="overwrite", properties=connectionProperties)

# COMMAND ----------

 spark.conf.set("fs.azure.account.auth.type", "SAS")\
 spark.conf.set("fs.azure.sas.token.provider.type", "com.microsoft.azure.synapse.tokenlibrary.ConfBasedSASProvider")\
 spark.conf.set("spark.storage.synapse.sas", "")
    
 df = spark.read.csv('abfss://<CONTAINER>@<ACCOUNT>.dfs.core.windows.net/<FILE PATH>')

# COMMAND ----------

spark.conf.set("fs.azure.account.auth.type", "SAS")
spark.conf.set("fs.azure.sas.token.provider.type", "com.microsoft.azure.synapse.tokenlibrary.ConfBasedSASProvider")
spark.conf.set("spark.storage.synapse.sas", "sp=r&st=2022-10-13T03:25:05Z&se=2022-10-13T11:25:05Z&spr=https&sv=2021-06-08&sr=c&sig=B951Q7W9hSzmgD%2BJ24PKxY1Oi5jemC0PkowGXxG0J6M%3D")

#spark.read.csv('abfss://data@lkoct1.dfs.core.windows.net/')

# COMMAND ----------

df.write.format('delta').save('https://lkoct1.blob.core.windows.net/data?sp=r&st=2022-10-13T03:29:23Z&se=2022-10-13T11:29:23Z&spr=https&sv=2021-06-08&sr=c&sig=mc5k95OQ1Zx3pCbkjoUpBwxF7hhxNW4Pobq0jR5Ij44%3D')

# COMMAND ----------

json = [i.asDict() for i in df.collect()]

# COMMAND ----------

PUoCrdzKrNEA/hPcvEX1QfWQSYzs2RynH6TADodm7lAlLTkGF2pJZ5EfefooFrukimXxre2gq1vG+ASt+L8doQ==

# COMMAND ----------

df.createOrReplaceTempView('df')

# COMMAND ----------

# MAGIC %sql

# COMMAND ----------



# COMMAND ----------

# MAGIC %scala
# MAGIC val jdbcUsername = "sqladmin"
# MAGIC val jdbcPassword = "Azure$2022"
# MAGIC val jdbcHostname = "lkoct.database.windows.net"
# MAGIC val jdbcDatabase = "sqldb"
# MAGIC val jdbcPort = 1433
# MAGIC val jdbcUrl = "jdbc:sqlserver://{0}:{1};database={2};user={3};password={4}".format(jdbcHostname, jdbcPort, jdbcDatabase, jdbcUsername, jdbcPassword)
# MAGIC val d ="com.microsoft.sqlserver.jdbc.SQLServerDriver"
# MAGIC val connectionProperties = {
# MAGIC   "user" : jdbcUsername;
# MAGIC   "password" : jdbcPassword;
# MAGIC   "driver" : d
# MAGIC }

# COMMAND ----------

# MAGIC %scala
# MAGIC val df = spark.sql("select * from df")
# MAGIC //df.write.jdbc(url=jdbcUrl, table="SalesLT.Product2", mode="overwrite", properties=connectionProperties)

# COMMAND ----------

# MAGIC %scala
# MAGIC val jdbc_dev = "jdbc:sqlserver://lksept2synapse.sql.azuresynapse.net:1433;database=AzureSynapsededicatedSQLpool;user=sqladmin@lksept2synapse;password=Azure$2022;encrypt=true;trustServerCertificate=false;hostNameInCertificate=*.sql.azuresynapse.net;loginTimeout=30;"

# COMMAND ----------

# MAGIC %scala
# MAGIC sc.hadoopConfiguration.set(
# MAGIC   "fs.azure.account.key.lksept2.dfs.core.windows.net",
# MAGIC   "o3jtzn9oF7VjuiYYsmm14ioQAN7eQYtFHu31/iKDLoi/lJFU80RVCB2dgCEVawESFcPBQZKD7FqA+ASt/mWTog==")

# COMMAND ----------

# MAGIC %scala
# MAGIC df.write
# MAGIC   .format("com.databricks.spark.sqldw")
# MAGIC   .option("url", jdbc_dev)
# MAGIC   .option("forwardSparkAzureStorageCredentials", "true")
# MAGIC   .option("dbTable", "product")
# MAGIC   .option("tempDir", "abfss://logs@lksept2.dfs.core.windows.net/tempDirs")
# MAGIC   .save()
