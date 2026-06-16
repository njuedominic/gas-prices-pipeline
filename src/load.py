# Load the data to Postgresql 

import os
from sqlalchemy import create_engine
from dotenv import load_dotenv
load_dotenv()

### Define function to load the data

def load_data(data, db_url):
    print("Loading data into the database")

    # Get the database url from environmental variables
    db_url = os.getenv('DATABASE_URL')

    #Create the Databse connection 
    engine = create_engine(db_url)


    #Load the data into the database

    data.to_sql('gas_prices', con=engine, if_exists='replace', index=False)

    print("Data loaded successfully to the database.")