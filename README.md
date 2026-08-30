# Retail Data Engineering - Week1

## Project Overview

This project impelements asimple ETL(Extract, Transform, Load) pipeline using python and pandas.

The pipeline reads retail sales data from a CSV file, performs data quality checks and transformation, and saves the cleaned data as processed CSV file.

The project also includes configuration mangement, logging, and automated tests using pytest.

---

## Project Structure

```text
Week1/
│
├── config.json
├── requirements.txt
├── README.md
├── .gitignore
│
├── data/
│   ├── raw/
│   │   └── sales_data.csv
│   └── processed/
│       └── sales_clean_data.csv
│
├── logs/
│   └── etl_pipeline.log
│
├── sql/
│
├── src/
│   ├── __init__.py
│   └── pipeline.py
│
└── test/
    └── test_pipeline.py

## Technologies Used

- Python
- Pandas
- Pytest
- Logging
- JSON
- Git
 
 ## ETL Pipeline

 The pipeline consists of three main stages:

 ### 1 Extract

 The pipeline reads the raw CSV file using pandas.
 'data/raw/sales_data.csv'
        ↓
      Extract

### 2 Transform

The transformation stage performs:

- Missing value cheack
- Duplicate removeable
- Data type conversion
- Total cost caculation
- Gross sale calculation
- Discount amount calculation

The following derived columns are created
Total_Cost
Gross_Sales
Discount_Amount

### 3 Load

The transformed data is save as:
data/processed/sales_clean_data.csv

## Configuration

The project uses config.json to store file paths.
```
{
    'input_file': 'data/raw/sales_data.csv'
    'output_file': 'data_clean_data.csv'
    'log_file': 'logs/etl_pipeline.log'
}
```
This keeps file paths separate from the python code

## Logging

The pipeline uses python's built-in logging modules
Logs are written to 
'logs/etl_pipeline.log'

The pipeline records important events such as
- ETL pipeline started
- Extract started
- Extract completed
- Transform started
- Duplicate removal
- Date type conversion
- Data loaded successfully
- pipeline completed successfully
logs are written both to the log file and to the terminal.

## Testing

The project uses pytest for automated testing
The test is suite checks the main ETL pipeline function, including
- Extract
- Transform
- Load
To run tests:
'python -m pytest -v'
Expected result 3 passed

## Installtion
1- create Virtual environmemnt
'python -m venv .venv'

2- Activate the virtual environment
'.venv/Scripts/Activate'

3- Install dependencies
'pip install -r requirements.txt'

## Running the pipeline

from week1 directory
'python src/pipeline.py'

This pipelinewill:
1- Read the raw sales CSV.
2- Check and transform the data.
3- Generate calculated columns.
4- Save the cleaned dataset.
5- Recored the process in the log file.

## Running test

Run:
'python -m pytest -v'
Asuccessful run shoud show:3 passed

## Data Transformation Formulas

Total Cost
'Total_Cost = Quantity_Sold * Unit_Cost'
Gross Sales
'Gross_Sales = Quantity_Sold * Unit_Price'
Discount Amount
'Discount_Amount = Gross_Sales * Discount'

## Scheduling

The ETL Pipeline is scheduled to run automatically one per day using widows Task scheduler.
The scheduled task uses the python interpreter from the project's virtual environment

### Task Configuration

Task Name : Retail ETL Pipeline
Trigger : Daily
Action : Start Program
Python Interpreter : '.venv\Scripts\python.exe'
Script : 'src\pipeline.py'
Working Directory : The project  directory 'C:\Users\zain\Desktop\Retail_Data_Engineering\week1>' 

## Project Goal 

The goal of this project is to demonstrate the fundamentals of building a reliable and maintainable ETL pipeline, including data extraction, transformation, loading, configuration, management, logging, testing, and project organization.



