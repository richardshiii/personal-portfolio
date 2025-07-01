'''
586. Customer Placing the Largest Number of Orders

Table: Orders
+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key (column with unique values) for this table.
This table contains information about the order ID and the customer ID.

Write a solution to find the customer_number for the customer who has placed the largest number of orders.

The test cases are generated so that exactly one customer will have placed more orders than any other customer.
'''

# Solution
import pandas as pd

def largest_orders(orders: pd.DataFrame) -> pd.DataFrame:
    orders = orders.groupby("customer_number")["order_number"].count().reset_index().sort_values(by = "order_number", ascending = False)

    orders = orders[orders["order_number"] == orders["order_number"].max()]

    orders = orders[["customer_number"]]

    return orders

'''
Test Case
| order_number | customer_number |
| ------------ | --------------- |
| 1            | 1               |
| 2            | 2               |
| 3            | 3               |
| 4            | 3               |
Output
| customer_number |
| --------------- |
| 3               |
'''