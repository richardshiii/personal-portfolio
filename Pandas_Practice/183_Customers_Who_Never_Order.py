'''
183. Customers Who Never Order
Data Filtering

Table: Customers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID and name of a customer.
 
Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| customerId  | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
customerId is a foreign key (reference columns) of the ID from the Customers table.
Each row of this table indicates the ID of an order and the ID of the customer who ordered it.
 
Write a solution to find all customers who never order anything.

Return the result table in any order.
'''

# Solution
import pandas as pd

def find_customers(customers: pd.DataFrame, orders: pd.DataFrame) -> pd.DataFrame:
    # Merge the Customers and Orders DataFrames on the customer ID
    merged = pd.merge(customers, orders, how = "left", left_on = "id", right_on = "customerId")
    # Filter the merged DataFrame to find customers who never ordered anything
    merged_na = merged["customerId"].isna()
    return merged[merged_na][["name"]].rename(columns = {"name":"Customers"})

'''
Test Case
| id | name  |
| -- | ----- |
| 1  | Joe   |
| 2  | Henry |
| 3  | Sam   |
| 4  | Max   |

| id | customerId |
| -- | ---------- |
| 1  | 3          |
| 2  | 1          |

Output
| Customers |
| --------- |
| Henry     |
| Max       |
'''