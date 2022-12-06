# Databricks notebook source
!pip install azureml-core

# COMMAND ----------

import azureml.core

print(azureml.core.VERSION)

# COMMAND ----------

from azureml.core import Workspace

ws = Workspace.from_config()

# COMMAND ----------

from azureml.opendatasets import Diabetes

# COMMAND ----------

from azureml import Workspace

ws = Workspace()

# COMMAND ----------

!pip install azure-storage

# COMMAND ----------

from azure.storage.blob import BlockBlobService

# storage account details
azure_storage_account_name = "azureopendatastorage"
azure_storage_sas_token = "sv=2019-02-02&ss=bfqt&srt=sco&sp=rlcup&se=2025-04-14T00:21:16Z&st=2020-04-13T16:21:16Z&spr=https&sig=JgwLYbdGruHxRYTpr5dxfJqobKbhGap8WUtKFadcivQ%3D"

# create a blob service
blob_service = BlockBlobService(
    account_name=azure_storage_account_name,
    sas_token=azure_storage_sas_token,
)

# COMMAND ----------

# container housing CORD-19 data
container_name = "covid19temp"

# download metadata.csv
metadata_filename = 'metadata.csv'
blob_service.get_blob_to_path(
    container_name=container_name,
    blob_name=metadata_filename,
    file_path=metadata_filename
)
