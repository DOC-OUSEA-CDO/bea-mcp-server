import asyncio
import os
from dotenv import load_dotenv
from client import BeaNipaClient

load_dotenv()

async def get_GDP_percent_change_annual_and_quarterly(client: BeaNipaClient, year: str):
    """
    Retrieves the percent change in relevant GDP statistics relative to the 
    last year and quarter for the given year.
    
    Args:
        year (str): The desired year of data.
    
    Returns:
        gdp_perc_change (dict): Contains the percent change in relevant GDP 
        statistics relative to the last year and quarter for a given year.
    """
    try:
        # build the params dictionary
        params = {
            "userID": f"{os.getenv('API_KEY')}",
            "method": "getData",
            "datasetName": "NIPA",
            "tableName": "T10101",
            "frequency": "A,Q",
            "year": year
        }
        
        response = await client.get(params=params)
        return response
    except Exception as e:
        return e


async def main():
    async with BeaNipaClient() as client:
        GDP_data = await get_GDP_percent_change_annual_and_quarterly(client, "2024")
        return GDP_data


if __name__ == "__main__":
    print(asyncio.run(main()))