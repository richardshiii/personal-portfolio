'''
1795. Rearrange Products Table

Table: Products
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_id  | int     |
| store1      | int     |
| store2      | int     |
| store3      | int     |
+-------------+---------+
product_id is the primary key (column with unique values) for this table.
Each row in this table indicates the product's price in 3 different stores: store1, store2, and store3.
If the product is not available in a store, the price will be null in that store's column.

Write a solution to rearrange the Products table so that each row has (product_id, store, price). 
If a product is not available in a store, do not include a row with that product_id and store combination in the result table.

Return the result table in any order.
'''

# Solution
import pandas as pd

def rearrange_products_table(products: pd.DataFrame) -> pd.DataFrame:
    # df.melt(dataframe, id_vars: columns that remain fixed, 
    # value_vars: columns to unpivot, var_name: column name that will hold the original column names, 
    # value_name: column name that will hold the values)
    melted_df = pd.melt(products, id_vars = ["product_id"],
        value_vars = ["store1", "store2", "store3"],
        var_name = "store",
        value_name = "price") 
    
    melted_clean = melted_df.dropna()

'''
Test Case
| product_id | store1 | store2 | store3 |
| ---------- | ------ | ------ | ------ |
| 0          | 95     | 100    | 105    |
| 1          | 70     | null   | 80     |
Output
| product_id | store  | price |
| ---------- | ------ | ----- |
| 0          | store1 | 95    |
| 1          | store1 | 70    |
| 0          | store2 | 100   |
| 0          | store3 | 105   |
| 1          | store3 | 80    |
'''