/*
1327. List the Products Ordered in a Period
Difficulty: Easy

Table: Products
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| product_id       | int     |
| product_name     | varchar |
| product_category | varchar |
+------------------+---------+
product_id is the primary key (column with unique values) for this table.
This table contains data about the company's products.

Table: Orders
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| order_date    | date    |
| unit          | int     |
+---------------+---------+
This table may have duplicate rows.
product_id is a foreign key (reference column) to the Products table.
unit is the number of products ordered in order_date.

Write a solution to get the names of products that have at least 100 units ordered in February 2020 and their amount.

Return the result table in any order.
*/

# Solution
select p.product_name, sum(o.unit) as unit
from Orders o
join Products p on p.product_id = o.product_id
-- Filter orders in February 2020
where o.order_date between "2020-02-01" and "2020-02-29"
group by p.product_name
-- Filter products with at least 100 units ordered
having sum(o.unit) >= 100;

/* Test Case
-- Products table
| product_id | product_name          | product_category |
| ---------- | --------------------- | ---------------- |
| 1          | Leetcode Solutions    | Book             |
| 2          | Jewels of Stringology | Book             |
| 3          | HP                    | Laptop           |
| 4          | Lenovo                | Laptop           |
| 5          | Leetcode Kit          | T-shirt          |
-- Orders table
| product_id | order_date | unit |
| ---------- | ---------- | ---- |
| 1          | 2020-02-05 | 60   |
| 1          | 2020-02-10 | 70   |
| 2          | 2020-01-18 | 30   |
| 2          | 2020-02-11 | 80   |
| 3          | 2020-02-17 | 2    |
| 3          | 2020-02-24 | 3    |
| 4          | 2020-03-01 | 20   |
| 4          | 2020-03-04 | 30   |
| 4          | 2020-03-04 | 60   |
| 5          | 2020-02-25 | 50   |
| 5          | 2020-02-27 | 50   |
| 5          | 2020-03-01 | 50   |
Output table
| product_name       | unit |
| ------------------ | ---- |
| Leetcode Solutions | 130  |
| Leetcode Kit       | 100  |
*/

