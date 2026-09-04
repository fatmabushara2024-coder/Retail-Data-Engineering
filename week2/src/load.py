import pandas as pd
import psycopg2

conn = psycopg2.connect(
    host='localhost',
    port=5432,
    database='sales_db',
    user='postgres',
    password=12345
)
file_path = 'C:/Users/zain/Desktop/Retail_Data_Engineering/week1/data/processed/sales_clean_data.csv'
df = pd.read_csv(file_path)
print(df.head())

product_df = df[['Product_ID', 'Product_Category', 'Unit_Cost', 'Unit_Price']].drop_duplicates(subset=['Product_ID'])
print('Unique products:', len(product_df))
cur = conn.cursor()

for _, product in product_df.iterrows():
    cur.execute(
    '''
    INSERT INTO product (
        product_id,
        product_category,
        unit_cost,
        unit_price
    )
    VALUES (%s, %s, %s, %s)
    ON CONFLICT (product_id) DO NOTHING
    ''',
        (
                int(product['Product_ID']),
                product['Product_Category'],
                float(product['Unit_Cost']),
                float(product['Unit_Price'])
        )
    )
#conn.commit()
print('All Product Inserted Successfully')

sales_representive_df = df[['Sales_Rep', 'Region']].drop_duplicates()
print('Unique sales rep:', len(sales_representive_df)) 
 
for _, sales_rep in sales_representive_df.iterrows():
    cur.execute(
        '''
        INSERT INTO sales_representive (
            sales_rep,
            region
        )
        SELECT %s, %s
        WHERE NOT EXISTS (
            SELECT 1 FROM sales_representive WHERE sales_rep = %s AND region = %s
        )
        ''',
        (
            sales_rep['Sales_Rep'],
            sales_rep['Region'],
            sales_rep['Sales_Rep'],
            sales_rep['Region']
        )
    )

#conn.commit()
print('All Sales Rep Inserted Successfully')
 
for _, sales in df.iterrows():
    cur.execute(
        '''
        SELECT sales_rep_id FROM sales_representive 
        WHERE sales_rep = %s AND region = %s
        ''',
        (
            sales['Sales_Rep'],
            sales['Region']
        )
    )
    
    result = cur.fetchone()
    if result:
        sales_rep_id = result[0]
        cur.execute(
            '''
            INSERT INTO sales (
                sales_date,
                product_id,
                sales_rep_id,
                sales_amount,
                quantity_sold,
                discount
            )
            VALUES (%s, %s, %s, %s, %s, %s)
            ''',
            (
                sales['Sale_Date'],
                int(sales['Product_ID']), sales_rep_id,
                float(sales['Sales_Amount']),
                int(sales['Quantity_Sold']),
                float(sales['Discount'])
            )
        )
conn.commit()
print('All sale inserted successfully')
