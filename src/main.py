from extract import extract_gas_prices
from transform import transform_data
from load import load_data
import os

# Define function to run the entire pipeline
def run_pipeline():
    # Extract data
    data = extract_gas_prices()
    
    # Transform data
    transformed_data = transform_data(data)
    
    # Load data
    load_data(transformed_data, os.getenv('DATABASE_URL'))

if __name__ == "__main__":
    run_pipeline()


