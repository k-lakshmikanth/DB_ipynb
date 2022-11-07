# Databricks notebook source
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "801ab191-c59e-4262-88d6-caed53f91738",
          "fs.azure.account.oauth2.client.secret": "FmO8Q~X26i16-nnR.vtOYYF68n58eYqFQ6aCgdyc",
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/4a125cb1-7277-47ca-bfbf-baad0b21be72/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://databricks@lknov1.dfs.core.windows.net/",
  mount_point = "/mnt/lknov1/databricks",
  extra_configs = configs)
