import sys
from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJECT_ROOT))

from src.pipeline import CsvETLPipeline


def create_test_csv(tmp_path):

    data = {
        "Product_ID": [1, 2, 2],
        "Sale_Date": ["2025-01-01", "2025-01-02", "2025-01-02"],
        "Sales_Rep": ["Ahmed", "Sara", "Sara"],
        "Region": ["North", "South", "South"],
        "Sales_Amount": [100, 200, 200],
        "Quantity_Sold": [2, 4, 4],
        "Product_Category": ["Laptop", "Phone", "Phone"],
        "Unit_Cost": [30, 50, 50],
        "Unit_Price": [50, 70, 70],
        "Discount": [0.1, 0.05, 0.05]
    }

    df = pd.DataFrame(data)

    input_file = tmp_path / "sales.csv"
    df.to_csv(input_file, index=False)

    return input_file


def test_extract(tmp_path):

    input_file = create_test_csv(tmp_path)

    pipeline = CsvETLPipeline(
        input_file,
        tmp_path / "output.csv"
    )

    pipeline.extract()

    assert pipeline.df is not None
    assert len(pipeline.df) == 3


def test_transform(tmp_path):

    input_file = create_test_csv(tmp_path)

    pipeline = CsvETLPipeline(
        input_file,
        tmp_path / "output.csv"
    )

    pipeline.extract()
    pipeline.transform()

    # Duplicate row should be removed
    assert len(pipeline.df) == 2

    # Derived columns should exist
    assert "Total_Cost" in pipeline.df.columns
    assert "Gross_Sales" in pipeline.df.columns
    assert "Discount_Amount" in pipeline.df.columns


def test_load(tmp_path):

    input_file = create_test_csv(tmp_path)
    output_file = tmp_path / "processed.csv"

    pipeline = CsvETLPipeline(
        input_file,
        output_file
    )

    pipeline.extract()
    pipeline.transform()
    pipeline.load()

    assert output_file.exists()

    loaded_df = pd.read_csv(output_file)

    assert len(loaded_df) == 2



