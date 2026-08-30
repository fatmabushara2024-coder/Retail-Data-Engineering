import pandas as pd
import logging
import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

CONFIG_FILE = BASE_DIR / 'config.json'
with open(CONFIG_FILE, 'r') as file:
    config = json.load(file)
    
input_file = BASE_DIR / config['input_file']
output_file = BASE_DIR / config['output_file']
log_file = BASE_DIR / config['log_file']  


log_file.parent.mkdir(parents=True, exist_ok=True)

logging.basicConfig(
    level = logging.INFO,
    format = '%(asctime)s - %(levelname)s - %(message)s',
    handlers=[logging.FileHandler('log_file'), logging.StreamHandler()
              ]
    )
logger = logging.getLogger(__name__)



class CsvETLPipeline:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.df = None
        
    def extract(self):
        try:
            logger.info('Extract started')
            self.df = pd.read_csv(self.input_file)
            logger.info('extract complete successfully. Rows: %s, columns: %s',
                        len(self.df),
                        len(self.df.columns)
                        )
        except FileNotFoundError:
            logger.error(f'Error: file not found: {self.input_file}')
            raise
            
        except Exception as e:
            logger.exception(f'Error during extraction: {e}')
            raise
            
            
    def transform(self):
        try:
            
            logger.info('Transform started')
        
            Missing_values = self.df.isnull().sum()
            logger.info('Missing value cheacked')
        
            befor = len(self.df)
            self.df = self.df.drop_duplicates()
            after = len(self.df)
            logger.info(f'Duplicates removed: {befor - after}')
        
            self.df['Product_ID'] = self.df['Product_ID'].astype(int)
            self.df['Sale_Date'] = pd.to_datetime(self.df['Sale_Date'])
            self.df['Sales_Rep'] = self.df['Sales_Rep'].astype(str)
            self.df['Region'] = self.df['Region'].astype(str)
            self.df['Sales_Amount'] = self.df['Sales_Amount'].astype(float)
            self.df['Quantity_Sold'] = self.df['Quantity_Sold'].astype(int)
            self.df['Product_Category'] = self.df['Product_Category'].astype(str)
            self.df['Unit_Cost'] = self.df['Unit_Cost'].astype(float)
            self.df['Unit_Price'] = self.df['Unit_Price'].astype(float)
            self.df['Discount'] = self.df['Discount'].astype(float)
        
            self.df['Total_Cost'] = (self.df['Quantity_Sold'] * self.df['Unit_Cost'])
            self.df['Gross_Sales'] = (self.df['Quantity_Sold'] * self.df['Unit_Price'])
            self.df['Discount_Amount'] = (self.df['Gross_Sales'] * self.df['Discount'])
        
            #print('\nTransformed data:')
            #print(self.df.head())
            #print('\nColumns:')
            #print(self.df.columns.tolist())
            
            logger.info('Data types converted successfully')
            logger.info('Derved columns created')        
            logger.info('Transform complete sucecessfully')
            
        
        except Exception as e:
            print(f'Error during Transformation: {e}')  
            raise  
        
    def load(self):
        try:
           logger.info('load started')
        
           output_path = Path(self.output_file)
           output_path.parent.mkdir(parents=True, exist_ok=True)
        
           self.df.to_csv(output_path, index=False)
        
           logger.info(f'Data loaded successfully to: {output_path}')
        
        except Exception as e:
            logger.exception(f'Error during loading: {e}')
       

    
    def run(self):
        try:
            logger.info('ETL Pipeline started')
            
            self.extract()
            self.transform()
            self.load()
            logger.info('ETL Pipeline completed successfully.')
            
        except Exception as e:
            logger.exception(f'ETL Pipeline failed: {e}')
            
if __name__ == '__main__':
    pipeline = CsvETLPipeline(input_file, output_file)
    pipeline.run()          
#pipeline = CsvETLPipeline('week1/data/raw/sales_data.csv')
#pipeline.run()            