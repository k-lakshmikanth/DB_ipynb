// Databricks notebook source
package com.sparkbyexamples.spark.dataframe.functions.window

import org.apache.spark.sql.expressions.Window
import org.apache.spark.sql.functions.row_number


import spark.implicits._

val simpleData = Seq(("James", "Sales", 3000),
  ("Michael", "Sales", 4600),
  ("Robert", "Sales", 4100),
  ("Maria", "Finance", 3000),
  ("James", "Sales", 3000),
  ("Scott", "Finance", 3300),
  ("Jen", "Finance", 3900),
  ("Jeff", "Marketing", 3000),
  ("Kumar", "Marketing", 2000),
  ("Saif", "Sales", 4100)
)


// COMMAND ----------

val df = simpleData.toDF("employee_name", "department", "salary")
df.show()

//row_number
val windowSpec  = Window.partitionBy("department").orderBy("salary")
df.withColumn("row_number",row_number.over(windowSpec))
  .show()

