/*
1164. Product Price at a Given Date
Difficulty: Medium

Table: Products

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| new_price     | int     |
| change_date   | date    |
+---------------+---------+
(product_id, change_date) is the primary key (combination of columns with unique values) of this table.
Each row of this table indicates that the price of some product was changed to a new price at some date.
Initially, all products have price 10.

Write a solution to find the prices of all products on the date 2019-08-16.

Return the result table in any order.
*/

# Solution
-- select products with their prices changed after 2019-08-16
select product_id, 10 as price
from Products
group by product_id
having min(change_date) > "2019-08-16"
-- union with products that have price changes on or before 2019-08-16
union all
-- select products with their latest price changes on or before 2019-08-16
select product_id, new_price as price
from Products
where (
    product_id, change_date
) in
(
    select product_id, max(change_date)
    from Products
    where change_date <= "2019-08-16"
    group by product_id
);

/* Test Case
-- Products table
| product_id | new_price | change_date |
| ---------- | --------- | ----------- |
| 1          | 20        | 2019-08-14  |
| 2          | 50        | 2019-08-14  |
| 1          | 30        | 2019-08-15  |
| 1          | 35        | 2019-08-16  |
| 2          | 65        | 2019-08-17  |
| 3          | 20        | 2019-08-18  |
Output table
| product_id | price |
| ---------- | ----- |
| 3          | 10    |
| 2          | 50    |
| 1          | 35    |
*/
