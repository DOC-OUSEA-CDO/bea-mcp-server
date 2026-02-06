from typing import Any
from fastmcp import FastMCP
from src.client import BeaNipaClient

def register_parameter_lookup_tools(mcp: FastMCP, client: BeaNipaClient):
    """Register parameter options/values reference/lookup tools"""

    @mcp.tool()
    async def get_valid_parameter_values_filtered(tableName: str, targetParameter: str) -> Any:
        """
        Get a list of all valid parameter values for the target parameter given 
        a particularly tableName value.

        Use this when you want to get a list of all available options for the 
        'Year' and 'Frequency' parameters once you have identified a target
        table and have its corresponding 'TableName' value. Use the results to
        help form the subsequent API calls to retrieve the raw table data.
        
        NOTES FOR BELLA:
            I THOUGHT THIS WOULD WORK BUT I THEN REALIZED THE 
            GetParameterValuesFiltered METHOD IS NOT IMPLEMENTED FOR THE 
            NIPA TABLES
            
            I THINK WE WILL HAVE TO USE THE GetParameterValues METHOD AS A FALL
            BACK OPTION AND, UNFORTUNATELY, HAVE TO SEARCH THROUGH THE LIST OF
            RESULTS FOR THE VALUES THAT CORRESPOND TO THE GIVEN TableName. 
            I HAVEN'T CODED/IMPLEMENTED THIS YET.

        Returns:
            The "Results" portion of the raw API response data as a JSON string 
            containing valid parameter values for the target parameter.
        """
        try:
            # build the params dictionary
            params = {
                "method": "getParameterValuesFiltered",
                "datasetName": "NIPA",
                "tableName": tableName,
                "targetParameter": targetParameter
            }
            
            # make API call
            response = await client.get(params=params)
            
            # extract, then return the "Results" portion of the raw API response
            results = response["BEAAPI"]["Results"]
            return results

        except Exception as e:
            return f"Error fetching valid parameter values: {str(e)}"

