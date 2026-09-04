CREATE TABLE dim_Product(
    product_key SERIAL PRIMARY KEY,
    Product_ID INT UNIQUE NOT NULL,
    Product_Category VARCHAR(100),
    Unit_Cost DECIMAL(10,2),
    Unit_Price DECIMAL(10,2)
);

CREATE TABLE dim_Sales_Rep(
    Sales_rep_key SERIAL PRIMARY KEY,
    Sales_rep_ID INT UNIQUE NOT NULL,
    Sales_Rep VARCHAR(100),
    Region VARCHAR(100)
);

CREATE TABLE dim_date (
    date_key SERIAL PRIMARY KEY,
    full_Date DATE UNIQUE NOT NULL,
    day INT,
    month INT,
    month_name VARCHAR(20),
    quarter INT,
    year INT,
    day_of_week INT,
    day_name VARCHAR(20)
);

CREATE TABLE fact_Sales(
    fact_sales_key SERIAL PRIMARY KEY,
    sales_id INT NOT NULL,
    date_key INT NOT NULL,
    Product_key INT NOT NULL,
    Sales_rep_key INT NOT NULL,
    Sales_Amount DECIMAL(12,2),
    Quantity_Sold INT,
    Discount DECIMAL(5,2),
    FOREIGN KEY (date_key) REFERENCES dim_date(date_key),
    FOREIGN KEY (product_key) REFERENCES dim_product(product_key),
    FOREIGN KEY (Sales_rep_key) REFERENCES dim_sales_rep(sales_rep_key)
);

