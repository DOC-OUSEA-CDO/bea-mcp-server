# BEA Server Design

## Tools

### Retrieve TableNames
Create a tool (i.e., get_table_names() that returns a list of all available NIPA tables. BEA breaks the tables up into sections by their topic area (e.g., domestic product and income, personal income and outlays); however, there is no way to grab a list of TableNames 
for just one or two of these sections; you have to grab them all at once. I've been brainstorming a couple potential solutions for this. I believe the first number in each TableName corresponds to the section number/topic area, and we should be able to embed this 
knowledge into the server; either through a Class, the server instructions, a skill.md file, or maybe all of the above.

### Get a List of Valid Parameter Values for the Given Table
Different tables accept different ranges of values for the two remaining parameters: Frequency and Year. As such, the server may need to double check that the parameter values indicated/supplied by the user, or those that it arrives at itself, are valid for the given 
table. To provide the server with this knowledge, we will need to create two tools, get_available_frequencies() and get_available_years() that return a list of valid parameter values for each respective parameter given the TableName.

### Retrieve Table Data
Once the server decides on all three parameter values, it has everything it needs to retrieve the data. Create a tool, get_table_data() that issues the appropriate API call, cleans/wrangles the json response, and returns it to the server.

## Control Flow
1. The server should always start by attempting to identify the appropriate table to retrieve data from. This will most likely entail calling the get_table_names() tool.
2. Once it has identified the target table and its associated TableName, the server should try to determine the appropriate values for the remaining parameters: Frequency and Year
  1. **Note:** since we are only focusing on the NIPA tables for now, we don't have to worry about other parameters in the API like GeoFips or Industry codes.
  2. To ensure it doesn't use invalid parameter values, the server should most likely call the get_available_frequencies() and/or get_available_years() tools.
3. Now that the server has all three parameter values, it can retrieve the data by calling the get_table_data() tool.  
