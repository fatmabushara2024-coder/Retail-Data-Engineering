# OLTP vs OLAP Design

## Overview

This project uses both OLTP and OLAP database designs to support
transactional operations and analytical reporting for a retail sales system.

## OLTP Design

The OLTP schema is designed to store and manage individual sales
transactions efficiently.

The main tables are:

- `products` — stores product information such as category, cost, and price.
- `sales_reps` — stores sales representative information and regions.
- `sales` — stores individual sales transactions.

The `sales` table uses foreign keys to connect each transaction to a
product and a sales representative.

### Why OLTP?

The OLTP design is normalized to reduce data duplication and maintain
data integrity. It is suitable for inserting, updating, and retrieving
individual sales transactions.

## OLAP Design

The OLAP schema is designed for analytical queries and reporting.

The main tables are:

- `dim_product` — product dimension.
- `dim_sales_rep` — sales representative dimension.
- `dim_date` — date dimension.
- `fact_sales` — central fact table containing sales measures.

The `fact_sales` table connects to the dimension tables using foreign keys.

### Why OLAP?

The OLAP design uses a star schema to make analytical queries simpler
and more efficient. It allows sales data to be analyzed by product,
sales representative, region, year, month, quarter, and day.

## OLTP vs OLAP

| Feature | OLTP | OLAP |
|---|---|---|
| Purpose | Transaction processing | Data analysis |
| Structure | Normalized | Star schema |
| Main data | Individual transactions | Historical analytical data |
| Queries | Short and frequent | Complex and analytical |
| Example | Record a sale | Analyze total sales by region |
| Main tables | `products`, `sales_reps`, `sales` | `fact_sales` and dimensions |

## Design Choice

Using both schemas provides a complete data architecture for the
retail project.
The OLTP schema maintains clean and consistent transactional data,
while the OLAP schema transforms this data into a structure optimized
for reporting and business analysis.
This separation allows transactional operations and analytical queries
to be handled independently while maintaining relationships between
the underlying data.

