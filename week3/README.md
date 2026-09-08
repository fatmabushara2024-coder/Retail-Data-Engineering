# Week 3 - Big Data and Spark ETL

## Project Overview

This project demonstrates the fundamentals of Big Data processing and distributed computing using Apache Spark.

Alarge online Retail dataset is processed through a scalable Spark ETL pipeline.

The pipeline performs:

- Data extraction from CSV
- Data cleaning and transformation
- Derived column creation
- Parquet output
- Partitioning by country
- Logging
- Performance optimization experiments

---

## Project Structure 

```text
Week3/
├── config/
│   └── config.json
├── src/
│   └── spark_etl.py
├── logs/
│   └── spark_etl.log
├── performance/
│   └── performance_notes.md
├── data/
│   ├── raw/
│   └── processed/
├── README.md
└── requirements.txt

---

## Dataset

The project uses the Online Retail dataset The raw data is stored in:
`data/raw/online_retail.csv`

The dataset contains approximately 1 million retail transaction records.

---

## Prerequisites

- Python 3.13
- Java 17
WSL2 / Ubuntu

---

## Technologies

- Pyspark 4.2.0
- Apache Spark
- Parquet

----

## ETL Pipeline

The ETL pipeline is implemented in:

`src/spark_etl.py

The pipeline contains three main stages.

### 1 Extract

Reads the raw CSV dataset using Spark.

### 2 Transform

The transformation stages:

- Removes rows with missing required values
- Removes duplicate records
- Removes transactions with non-positive quantities
- Removes transactions with non-positive prices
- Create `Total_Amount` column

The calculation is:
 
  `Total_Amount = Quantity * Price`

### Load

The transformed data is written to parquet format.

The output stored in:

`data/processed/retail`

The data is partitioned by:
     `country`

---

## Configuration

Pipeline setting are stored in:

`config/config.json`

The configuration contains:

- Input file
- Output_file
- partition column
- Spark application name

This allow the pipeline configuration to be changed without modifying the main ETL code.

## Logging

The pipeline uses Python logging to record execution information.

log file:

`logs/spark_etl.log`

The log records events such as:

- Extract started/completed
- Transform started/completed
- Load started/completed
- Spark session stopped

---

## Performance Pruning

The output data partitioned by country.

filtering by:

`country = Germany`

allows Spark to use partition pruning.

the physical execution plan confirmed:

`partitionFilters: country = Germany`

---

## caching

Caching was testedto evaluate the benefit of reusing a DataFrame across multiple actions.

The physical plan confirmed cached data through:

`InMemoryTableScan`

---

## Repartitioning

repartitioning was tested using:

`repartition(8, 'StockCode')`

The physical plan confirmed:

`Exchange hashpartitioning(StockCode, 8)

Performance results and detailed observations are documented in:

`Performance/performance_notes.md`

---

## Running the Pipeline 

Activate the WSL virtual environment:

`source .venv-wsl/bin/activate`

Run the ETL pipeline:

`python src/spark_etl.py

A successful execution should complete:

Extract
   |
Transform   
   |
 load

and finish with the Spark session being stopped successfuly.

---

## Output

The processed data is stored as parquet files under:
`data/processed/retail`

with partition based on:

   `Country`

## Performance Result

The main measured optimization result was from repartitioning.

Test                       Execution Time

Without Repartitioning      6 min 43 sec
with Repartitioning         1 min 00 sec

This represents an approximately 85.1% reduction in execution time for the testes workload.

Performance measurements depends on the execution environment and workload.

---

## Learning Objectives

This project demonstrates:

- Big Data processing fundamentals
- Distributed data processing with Spark
- Spark DataFrame
- ETL pipeline
- Parquet storge
- Partitioning
- partition pruning
- Caching
- Repartitioning
- Physical execution plans
- Performance analysis
- Logging
- Configuration management
