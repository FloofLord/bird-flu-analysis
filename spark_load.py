import os
from awsglue.dynamicframe import DynamicFrame
from pyspark.context import SparkContext
from awsglue.context import GlueContext
from pyspark.context import SparkContext
from pyspark.sql import SparkSession

def main():
    sc = SparkContext.getOrCreate()
    #ls
    # glueContext = GlueContext(sc)
    spark = SparkSession \
            .builder \
            .appName("bird flu etl") \
            .getOrCreate()


    path = "data"
    print(os.listdir(path))
    db_url = "jdbc:postgresql://localhost:5432/postgres"
    
    for file in os.listdir(path):
        full_path =  f"{path}/{file}" # path + "/" + file
        table_name = file.split(".")[0]
        table_name = table_name.replace("-","_")
        
        df = spark.read.csv(full_path, header=True, inferSchema=True)
        #dyf = DynamicFrame.fromDF(df, glueContext, table_name)

        table_name = file.split(".")[0]
        table_name = table_name.replace("-","_")
    
        #dyf = DynamicFrame.fromDF(df, glueContext, table_name)
        
        resp = df.write.format("jdbc") \
                .option("url", db_url) \
                .option("driver", "org.postgresql.Driver") \
                .option("dbtable", table_name) \
                .option("user", "postgres") \
                .option("password", "password") \
                .mode("overwrite") \
                .save()
        
        print(resp)

if __name__ == "__main__":
    main()