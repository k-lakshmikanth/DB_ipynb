# Databricks notebook source
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "b6040595-d498-4e47-b174-dddd0595a2ae",
          "fs.azure.account.oauth2.client.secret": "yWY8Q~oEGPIoqThbTnp77QoBrpZwLP1C0RnHgckA",
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/5d8baf8c-b2b9-4565-9f80-c22d0cab3623/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://data@lkdec1.dfs.core.windows.net/",
  mount_point = "/mnt/lkdec1/databricks",
  extra_configs = configs)

# COMMAND ----------

# MAGIC %sh
# MAGIC echo "hello world"
