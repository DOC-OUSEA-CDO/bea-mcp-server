import asyncio
import logging

from fastmcp import FastMCP
from client import BeaNipaClient
from tools.get_table_names import register_table_name_tools
from tools.get_valid_parameters import register_parameter_lookup_tools

logger = logging.getLogger(__name__)

# Create FastMCP instance with detailed instructions
mcp = FastMCP(
    name="BeaNipaServer",
    instructions="""
    This server provides comprehensive access to National Income and Product 
    Account (NIPA) data through the apps.bea.gov API.

    ## Key Parameters:

    ### Table:
    - **Divide the tables to topic and create functions to retrieve names based on that** 
    - **If unsure of topic, use get_table_names() to get a complete list of all available NIPA tables**

    ### Release Frequency:
    - **M:** Monthly
    - **Q:** Quarterly
    - **A:** Annual
    - **Use get_available_frequencies() to get a list of valid frequencies for the given table.**
    - **Use multiple frequency values in a comma-separated list to retrieve data from multiple releases in one API call**

    ### Data Formatting (ShowMillions flag):
    - **"N":** Return raw, unscaled values (e.g., 1234567 - meaning $1,234,567)
    - **"Y":** Return data values scaled to millions and formats
    - **Default value is 'N'**
    - **Can be used when requesting percent tables; however, it will have no impact on the data values**
    
    ### Year:
    - **"X" or "ALL":** Return data for all available years 
    - **Use get_available_years() to get a list of valid years for the given table.**

    Always provide clear, actionable insights based on the economic data retrieved.
    """,
)


def main():
    """Main entry point"""
    logging.basicConfig(level=logging.INFO)
    logger.info("Starting USA Spending MCP Server")

    # Run the asynchronous main function
    asyncio.run(async_main())


async def async_main():
    """Async entry point"""
    # Initialize HTTP client
    async with BeaNipaClient() as client:
        # Register tools
        logger.info("Registering tools")
        register_table_name_tools(mcp, client)
        register_parameter_lookup_tools(mcp, client)

        logger.info("Running BEA NIPA MCP Server")
        await mcp.run_async()


if __name__ == "__main__":
    main()