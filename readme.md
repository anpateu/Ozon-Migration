# Ozon API Product Migrator
This code is used to migrate products from one Ozon account to another by utilizing the Ozon API. The products are first loaded from a CSV file and an Excel file, and then the API is used to create the products in the new Ozon account.

## Prerequisites
To run this code, the following files are required:

- **CSV file** containing product information (including SKU ID, name, and price)
- **Excel file** containing information on how to match the products from the CSV file with the products in the new Ozon account

## How it Works
The code uses the pandas library to read the data from the CSV and Excel files, and then performs some operations on the data to clean and prepare it for use with the API. This includes renaming columns, dropping duplicates, and using regular expressions to split the data into two groups based on whether or not the product codes contain a dot ("**.**").

The code then uses the `merge()` function from pandas to merge the data from the CSV and Excel files, creating two DataFrame objects containing the data for the products that will be migrated to the new Ozon account.

Once the data is prepared, the OzonAPI class is used to create the products in the new Ozon account. The `create_products()` method is called with a list of products to create, and the code uses a loop to split the list of products into smaller slices of **1000** items each to avoid exceeding the API's maximum request size.
