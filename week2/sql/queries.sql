-- Q1 Total Sales
SELECT SUM(sales_amount) AS total_sales FROM fact_sales;

--Total Sales = 5019265.23 

-- Q2 Total Quantity Sold
SELECT SUM(quantity_sold) AS total_quantity_sold FROM fact_sales;

-- Total Quantity Sold = 25355

-- Q3 Average Amount Sales
SELECT AVG(sales_amount) AS average_sales_amount FROM fact_sales;

-- Average Amount Sales = 5019.2652300000000000 

-- Q4  Highest Sales Transaction
SELECT MAX(sales_amount) AS highest_sales FROM fact_sales;

-- Highest Sales Transaction =  9989.04

-- Q5  Lowest Sales Transaction
SELECT MIN(sales_amount) AS lowest_sales FROM fact_sales;

-- Lowest Sales Transaction = 100.12

-- Q6 Total of Sales Transaction
SELECT COUNT(*) AS total_transaction FROM fact_sales;

-- Total of Sales Transaction = 1000

-- Q7 Total Sales by Product Category
SELECT p.product_category, SUM(f.sales_amount) AS total_sales 
FROM fact_sales f JOIN dim_product p 
ON f.product_key = p.product_key 
GROUP BY p.product_category ORDER BY total_sales DESC;

-- product_category | total_sales
------------------+-------------
# Furniture        |  1566190.36
 #Clothing         |  1202034.72
 #Electronics      |  1131692.14
 #Food             |  1119348.01
 #(4 rows)

 -- Q8  Count the number of sales transaction for each product
 SELECT p.product_category, COUNT(*) AS number_of_transactions 
 FROM fact_sales f JOIN dim_product p
ON f.product_key = p.product_key
GROUP BY P.product_category ORDER BY number_of_transactions DESC;

-- Q9 Total sales by Sale Representive
SELECT r.sales_rep, SUM(f.sales_amount) AS total_sales
FROM fact_sales f JOIN dim_sales_rep r 
ON f.sales_rep_key = r.sales_rep_key 
GROUP BY  r.sales_rep ORDER BY total_sales DESC;

-- Q10 Total Sales by Region
SELECT r.region, SUM(f.sales_amount) AS total_sales 
FROM fact_sales f JOIN dim_sales_rep r
ON f.sales_rep_key = r.sales_rep_key
GROUP BY r.region ORDER BY total_sales DESC;

-- Q11 Total Sales by Year
SELECT d.year, SUM(f.sales_amount) AS total_sales
FROM fact_sales f JOIN dim_date d
ON f.date_key = d.date_key
GROUP BY d.year ORDER BY d.year; 

-- Q12 Total Sales by Month
SELECT d.year, d.month, d.month_name, SUM(f.sales_amount) AS total_sales
FROM fact_sales f JOIN dim_date d
ON f.date_key = d.date_key
GROUP BY d.year, d.month, d.month_name ORDER BY d.year, d.month;

-- Q13 Average Sales by Product Category
SELECT p.product_category, AVG(f.sales_amount) AS averge_sales
From fact_sales f JOIN dim_product p
ON f.product_key = p.product_key
GROUP BY p.product_category ORDER BY averge_sales DESC;

-- Q14 Total Quantity Sold by Product category
SELECT p.product_category, SUM(f.quantity_sold) AS total_quantity_sold
FROM fact_sales f JOIN dim_product p
ON f.product_key = p.product_key
GROUP BY p.product_category ORDER BY total_quantity_sold DESC;

--Q15 Total Sales by Sales Representive and Region
SELECT r.region, r.sales_rep, SUM(f.sales_amount) AS total_sales
FROM fact_sales f JOIN dim_sales_rep r 
ON f.sales_rep_key = r.sales_rep_key
GROUP BY r.region, r.sales_rep ORDER BY r.region, total_sales DESC;  

-- Q16 Number Transaction  by Sales representive
SELECT r.sales_rep, COUNT(*) AS number_of_transactions
FROM fact_sales f JOIN dim_sales_rep r 
ON f.sales_rep_key = r.sales_rep_key
GROUP BY r.sales_rep ORDER BY number_of_transactions DESC;

-- Total Sales by Quarter
SELECT d.year, d.quarter, SUM(f.sales_amount) AS total_sales
FROM fact_sales f JOIN dim_date d
ON f.date_key = d.date_key
GROUP BY d.year, d.quarter ORDER BY d.year, d.quarter;

-- Q18 Total Sales by Day of Week
SELECT d.day_name, SUM(f.sales_amount) AS total_sales
FROM fact_sales f JOIN dim_date d
ON f.date_key = d.date_key
GROUP BY d.day_name ORDER BY total_sales DESC;

-- Q19 Average Sales by Region
SELECT r.region, AVG(f.sales_amount) AS average_sales
FROM fact_sales f JOIN dim_sales_rep r
ON f.sales_rep_key = r.sales_rep_key
GROUP BY r.region ORDER BY average_sales DESC;

-- Q20 Top 5 Product by Total Sales
SELECT p.product_id, p.product_category, SUM(f.sales_amount) AS total_sales
FROM fact_sales f JOIN dim_product p
ON f.product_key = p.product_key
GROUP BY p.product_id, p.product_category ORDER BY total_sales DESC LIMIT 5;
