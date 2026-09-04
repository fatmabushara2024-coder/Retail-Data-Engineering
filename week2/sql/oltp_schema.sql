CREATE TABLE Product(
    Product_ID INT PRIMARY KEY,
    Product_Category VARCHAR(100),
    Unit_Cost DECIMAL(10,2),
    Unit_Price DECIMAL(10,2)
);

CREATE TABLE Sales_Representive(
    Sales_rep_ID SERIAL PRIMARY KEY,
    Sales_Rep VARCHAR(100),
    Region VARCHAR(100)
);

CREATE TABLE Sales(
    Sales_ID SERIAL PRIMARY KEY,
    Sales_Date DATE,
    Product_ID  INT NOT NULL,
    Sales_rep_ID INT NOT NULL,
    Sales_Amount DECIMAL(10,2),
    Quantity_Sold INT,
    Discount DECIMAL(5,2),
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID),
    FOREIGN KEY (Sales_rep_ID) REFERENCES Sales_Representive(Sales_rep_ID)
);
