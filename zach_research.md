
# Research into BEA API & Releases/Tables

## Questions for BEA

It is difficult to understand the table structure / hierarchy in the responses from the API (i.e. what is nested below what?). Any advice/guidance for how to deal with that?
Is there a lookup table anywhere for the various 'SeriesCode' values and/or a lookup table for the individual symbols/acronyms within them?
The API responses sometimes differ from the documentation in the BEA API User Guide. Do you have any recommendations for how to deal with that? Are there plans to rectify this?
  - e.g.., with method=getParameterList and datasetName=Name, the API returns five parameters; however the User Guide only lists three. Through experimenting with the API, I have found that two of them are deprecated (i.e., TableID and ShowMillions). Although the API will still accept them, they do not affect the response, and, if you only use the TableID and no TableName, the API will return an error.

## Release - Real Gross Domestic Product (RGDP)

**Note:** I only looked for tables with percent change; however, there should be corresponding tables with raw values for most of the statistics

### Primary Table
  - "TableName": "T10101",
  - "Description": "Table 1.1.1. Percent Change From Preceding Period in Real Gross Domestic Product (A) (Q)"
  - Releases: **Annual (A) and Quarterly (Q)**
  - Contains:
  	- **GDP, Real PCE, Gross Private Domestic Investment, Real PCE: Goods**
  	- Exports, Imports, and their components 
  	- Government Consumption Expenditures and Gross Investment
  	- A number of subcomponents of GDP, PCE, GPDI

### Secondary Table
  - "TableName": "T11701",
  - "Description": "Table 1.17.1. Percent Change From Preceding Period in Real Gross Domestic Product, Real Gross Domestic Income, and Other Major NIPA Aggregates (A) (Q)"
  - Releases: **Annual (A) and Quarterly (Q)**
  - Contains:
    - U.S. Production:
	  - **GDP, GDI, Average of GDP & GDI**
	  - Net domestic product & income
	- Production by labor and capital supplied by U.S. residents:
	  - Gross national product, Gross national income, Net national product
	- Final expenditures by U.S. residents:
	  - Gross domestic purchases, Final sales to domestic purchasers, **Final sales to private domestic purchasers**
	- Purchasing power of income:
	  - Command-basis gross domestic product	
	  - Command-basis net domestic product
	  - Command-basis gross national product
	  - Command-basis net national product
    - After-tax income received by the personal sector - disposable personal income

### Extra Table:  

**Note:** Probably unnecessary - I didn't notice that the final sales statistic we need is also in T11701

  - "TableName": "T10401"
  - "Description": "Table 1.4.1. Percent Change From Preceding Period in Real Gross Domestic Product, Real Gross Domestic Purchases, and Real Final Sales to Domestic Purchasers (A) (Q)"
  - Releases: Annual (A) and Quarterly (Q)
  - Contains:
	- Gross domestic purchases = GDP - exports + imports
	- Final sales to domestic purchases = gross domestic purchases - change in private inventories
	- Addenda:
	  - Final sales of domestic product
	  - **Final sales to private domestic purchasers**
	  - Gross domestic purchases, current dollars
	  - Final sales to domestic purchasers, current dollars
	  - Final sales to private domestic purchasers, current dollars

## Release - Personal Income and Outlays (PIO):

### T20301
  - Table 2.3.1. Percent Change From Preceding Period in Real Personal Consumption Expenditures by Major Type of Product
  - Releases: **Annual (A) and Quarterly (Q)**
  - Contains: **Real PCE, PCE excluding food and energy, Real PCE: Goods**

### Additional Tables
  - "TableName": "T20100",
    - "Description": "Table 2.1. Personal Income and Its Disposition (A) (Q)"
  - "TableName": "T20600",
    - "Description": "Table 2.6. Personal Income and Its Disposition, Monthly (M)"
  - Table 2.8.4. Price Indexes for Personal Consumption Expenditures by Major Type of Product

