# Week 2 - SQL Database Design and Analytics

## Overview

Week 2 focuses on designing a retail sales database using both OLTP
and OLAP approaches, loading data into PostgreSQL, and writing
analytical SQL queries.

## Objectives

- Design an OLTP database schema for retail sales transactions.
- Design an OLAP star schema for analytical reporting.
- Load processed sales data into PostgreSQL.
- Create dimension and fact tables.
- Write SQL queries for sales analysis.
- Create an Entity Relationship Diagram (ERD).
- Compare OLTP and OLAP database designs.

## Project Structure

```text
Week2/
├── SQL/
│   ├── OLTB_schema.sql
│   ├── OLAP_schema.sql
│   └── queries.sql
├── erd/
│   └── retail_erd.png
├── docs/
│   └── oltp_vs_olap.md
├── src/
│   └── load.py
├── README.md
└── requirements.txt

## Technologies

- Python
- PostgresSQL
- SQL
- pandas
- psycopg2-binary

## Database Design

### OLTP

The OLTP schema contains:
- product
- sales_representive
- sales
It is designed for transactional data storge and maintaining data integrity through primary and forign keys.

### OLAP

The OLAP schema uses star schema consisting of:
- dim_product
- dim_sales_rep
- dim_date
- fact_sales
The structure support analytical queries and reporting

## Data Loading

Processed sales data from week1 was loaded into PostgreSQL.
The database contains:
- 100 products
- 20 sales representives
- 340 dates
- 1000 sales transactions
- 1000 fact records

## SQL Quries

Acollection of 20 SQL queries was created to demonstrate different analytical techniques including:
- Aggregations
- Grouping
- Sorting
- Averages
- Minimum and Maximum values
- Sales analysis by product category
- Sales analysis by sales representive
- Time based analysis
- Top salling product

## ERD

The RED illustrates the relationship between the OLTP tables
- product  -> sales
- sales_representive -> sales
The diagram is avalible in:
`erd/sales_erd.png`

## OLTP cs OLAP

A detailed comparision of the OLTP and OLAP designs is available
`Docs/oltp_vs_olap.md`

## Python Data Loading

The src/load.py script uses pandas to read the processed CSV file and psycopg2-binary to load the data into PostgreSQL.
