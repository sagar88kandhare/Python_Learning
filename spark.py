from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("ETL Pipeline").getOrCreate()

data_df = spark.read.csv("path", header = True, inferSchema = True)

transformed_df = data_df.filter(data_df.age > 18).groupBy("City").agg({"Salary" : "sum"})

transformed_df.write.format("delta").save("/mnt/delta/transformed_data")