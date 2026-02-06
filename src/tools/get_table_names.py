from typing import Any
from fastmcp import FastMCP
from src.client import BeaNipaClient

def register_table_name_tools(mcp: FastMCP, client: BeaNipaClient):
    """Register TableName reference/lookup tools"""

    @mcp.tool()
    async def get_table_names() -> Any:
        """
        Get a list of all available NIPA tables.

        Use this when you want to get a list of all available NIPA tables and 
        their associated descriptions and TableName values, which are needed 
        for other API calls.

        Returns:
            The "Results" portion of the raw API response data as a JSON string 
            containing NIPA table information
        """
        try:
            # build the params dictionary
            params = {
                "method": "GetParameterList",
                "datasetName": "NIPA"
            }
            
            # make API call
            response = await client.get(params=params)
            
            # extract, then return the "Results" portion of the raw API response
            results = response["BEAAPI"]["Results"]
            return results

        except Exception as e:
            return f"Error fetching NIPA table information: {str(e)}"

