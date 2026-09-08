import json
import logging
import sys
import os
import subprocess
import time
from pathlib import Path
from pyspark.sql.functions import col
from pyspark.sql import SparkSession

BASE_DIR = Path(__file__).resolve().parent.parent
CONFIG_PATH = BASE_DIR/ 'config'/'config.json'

with open(CONFIG_PATH, "r") as file:
    config = json.load(file)

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
    handlers=[
        logging.FileHandler(
            "logs/spark_etl.log",
            encoding="utf-8"
        ),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

spark = (
    SparkSession.builder
    .appName(config["app_name"])
    .master("local[*]")
    .getOrCreate()
)
print('spark started successfully!')


def extract(spark, input_file):

    logger.info("Starting Extract...")
    
    df = (
        spark.read
        .option("header", True)
        .option("inferSchema", True)
        .csv(input_file)
    )
    logger.info("Extract completed successfully.")
    return df

def transform(df):
    logger.info('Starting Transform')
    
    df_clean = df.dropna(
        subset=['Invoice', 'StockCode', 'Quantity', 'Price']
    )
    
    df_clean = df_clean.dropDuplicates()
    
    df_clean = (
        df_clean.filter(col('Quantity')>0)
        .filter(col('Price')>0)
    )
    
    df_clean = df_clean.withColumn(
        'Total_Amount', col('Quantity') * col('Price')
    )
    
    logger.info('Transform Completed Successfully.')
    return df_clean

def load(df, output_file, partition_column):
    logger.info('start loading')
    (
        df.write
        .mode('overwrite')
        .partitionBy(partition_column)
        .parquet(output_file)
    )
    logger.info('Load completed successfully.')


def main():
    df = extract(spark, config["input_file"])

    logger.info(f"Input partitions: {df.rdd.getNumPartitions()}")

    logger.info("Showing first 5 rows:")
    df.show(5)

    logger.info("Data schema:")
    df.printSchema()

    row_count = df.count()
    logger.info(f"Input row count: {row_count}")
        
    df_clean = transform(df)
    logger.info(f"Transformed row count: {df_clean.count()}")
    logger.info('Showing transformed data:')
    df_clean.show(5)
    
    load(
        df_clean,
        config["output_file"],
        config["partition_column"]
    )
        

if __name__ == "__main__":
    try:
        main()
    finally:
        spark.stop()
        logger.info('spark session stopped')









  
    

    
    