import os
import requests
import pandas as pd
from dotenv import load_dotenv
load_dotenv()

def extract_gas_prices(state = 'WA') -> pd.DataFrame:

    """
    Extracts gas price data from the EIA API for a given state.

    Parameters:
    state (str): The two-letter abbreviation of the state to extract data for. Default is 'WA'.

    Returns:
    pd.DataFrame: A DataFrame containing the extracted gas price data.
    """
    url = "https://api.collectapi.com/gasPrice/stateUsaPrice"
    api_key = os.getenv('COLLECTAPI_KEY')
    if not api_key:
        raise Exception("API key not found. Please set the COLLECTAPI_KEY environment variable.")
    
    headers = {
        'content-type': 'application/json',
        'authorization': f"apikey {api_key}"
    }
    params = {
        'state': state
    }

    try:
        print("Extracting gas prices...")
        response = requests.get(url, headers=headers, params=params)
        
        #Raise an exception for HTTP errors
        response.raise_for_status()
        data = response.json()

        # drilling down to the results
        results_dict = data.get('result', {})
        cities_data = results_dict.get('cities', [])

        prices_df =  pd.DataFrame(cities_data)
        return prices_df
    
    except requests.exceptions.RequestException as e:
        print(f"Failed to fetch gas prices: {e}")
        return pd.DataFrame()

testdf = extract_gas_prices()
print(testdf.head())