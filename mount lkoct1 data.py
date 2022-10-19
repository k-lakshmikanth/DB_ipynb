# Databricks notebook source
configs = {"fs.azure.account.auth.type": "OAuth",
          "fs.azure.account.oauth.provider.type": "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
          "fs.azure.account.oauth2.client.id": "4dea5726-8cd1-4ba6-bb6d-c3b9e13fc96b",
          "fs.azure.account.oauth2.client.secret": "Pys8Q~lipebawMzV-kLGNszhGgLy8ojME-zFLaRn",
          "fs.azure.account.oauth2.client.endpoint": "https://login.microsoftonline.com/f82aa19e-a2ba-4624-98ae-0c68d6c4fa52/oauth2/token"}

# Optionally, you can add <directory-name> to the source URI of your mount point.
dbutils.fs.mount(
  source = "abfss://data@lkoct1.dfs.core.windows.net/",
  mount_point = "/mnt/lkoct1/data",
  extra_configs = configs)
