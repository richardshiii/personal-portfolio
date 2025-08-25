/*
3657. Find Loyal Customers
Difficulty: Medium
https://leetcode.com/problems/find-loyal-customers/description/

Table: customer_transactions
+------------------+---------+
| Column Name      | Type    | 
+------------------+---------+
| transaction_id   | int     |
| customer_id      | int     |
| transaction_date | date    |
| amount           | decimal |
| transaction_type | varchar |
+------------------+---------+
transaction_id is the unique identifier for this table.
transaction_type can be either 'purchase' or 'refund'.
Write a solution to find loyal customers. A customer is considered loyal if they meet ALL the following criteria:

Made at least 3 purchase transactions.
Have been active for at least 30 days.
Their refund rate is less than 20% .
Return the result table ordered by customer_id in ascending order.
*/
# Solution 
select customer_id
from customer_transactions
group by customer_id
-- find custoemers who are active for at least 30 days
having datediff(max(transaction_date), min(transaction_date)) >= 30
-- find customers who made at least 3 purchase transactions
-- COUNT() counts all NON-NULL values, so else NULL instead of 0
and count(case when transaction_type = "purchase" then 1 else NULL end) >= 3
-- find customers whose refund rate is less than 20%
and count(case when transaction_type = "refund" then 1 else NULL end) 
/ count(case when transaction_type = "purchase" then 1 else NULL end) <= 0.2
order by customer_id asc;

/* Test Case
custoemr_transactions = 
| transaction_id | customer_id | transaction_date | amount | transaction_type |
| -------------- | ----------- | ---------------- | ------ | ---------------- |
| 1              | 101         | 2024-01-05       | 150    | purchase         |
| 2              | 101         | 2024-01-15       | 200    | purchase         |
| 3              | 101         | 2024-02-10       | 180    | purchase         |
| 4              | 101         | 2024-02-20       | 250    | purchase         |
| 5              | 102         | 2024-01-10       | 100    | purchase         |
| 6              | 102         | 2024-01-12       | 120    | purchase         |
| 7              | 102         | 2024-01-15       | 80     | refund           |
| 8              | 102         | 2024-01-18       | 90     | refund           |
| 9              | 102         | 2024-02-15       | 130    | purchase         |
| 10             | 103         | 2024-01-01       | 500    | purchase         |
| 11             | 103         | 2024-01-02       | 450    | purchase         |
| 12             | 103         | 2024-01-03       | 400    | purchase         |
| 13             | 104         | 2024-01-01       | 200    | purchase         |
| 14             | 104         | 2024-02-01       | 250    | purchase         |
| 15             | 104         | 2024-02-15       | 300    | purchase         |
| 16             | 104         | 2024-03-01       | 350    | purchase         |
| 17             | 104         | 2024-03-10       | 280    | purchase         |
| 18             | 104         | 2024-03-15       | 100    | refund           |
Output table = 
| customer_id |
| ----------- |
| 101         |
| 104         |
*/



