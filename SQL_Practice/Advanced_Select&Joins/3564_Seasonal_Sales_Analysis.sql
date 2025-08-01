/*
3564. Seasonal Sales Analysis
Difficulty: Medium
https://leetcode.com/problems/seasonal-sales-analysis/description/

Table: sales
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| sale_id       | int     |
| product_id    | int     |
| sale_date     | date    |
| quantity      | int     |
| price         | decimal |
+---------------+---------+
sale_id is the unique identifier for this table.
Each row contains information about a product sale including the product_id, date of sale, quantity sold, and price per unit.

Table: products
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| product_id    | int     |
| product_name  | varchar |
| category      | varchar |
+---------------+---------+
product_id is the unique identifier for this table.
Each row contains information about a product including its name and category.
Write a solution to find the most popular product category for each season. The seasons are defined as:

Winter: December, January, February
Spring: March, April, May
Summer: June, July, August
Fall: September, October, November
The popularity of a category is determined by the total quantity sold in that season. 
If there is a tie, select the category with the highest total revenue (quantity × price).

Return the result table ordered by season in ascending order.
*/
# Solution 
-- create temporary table to extract season, total_quantity, and total_revenue information
with CTE as (
    select 
    -- use case when to categorize months into seasons
    (case 
        when month(s.sale_date) in (12,1,2) then 'Winter'
        when month(s.sale_date) in (3,4,5) then 'Spring'
        when month(s.sale_date) in (6,7,8) then 'Summer'
        else 'Fall'
    end) as season,
    p.category,
    -- calculate total_quantity
    sum(s.quantity) as total_quantity,
    -- calculate total_revenue
    sum(s.quantity * s.price) as total_revenue
    from sales s
    join products p
    on s.product_id = p.product_id
    -- group total quantity and total revenue by product category and season
    group by p.category, season
),
-- create 2nd table to assign rankings to product categories for each season
ranked as (
    select *,
    -- order by total quantity first, if tie, order by total_revenue
    rank() over (partition by season order by total_quantity desc, total_revenue desc) as rnk
    from CTE
)
select season, category, total_quantity, total_revenue
from ranked
-- only show top ranked product category for each season
where rnk = 1
-- order by season ascending
order by season asc;

/*
Test Case
sales = 
| sale_id | product_id | sale_date  | quantity | price |
| ------- | ---------- | ---------- | -------- | ----- |
| 1       | 1          | 2023-01-15 | 5        | 10    |
| 2       | 2          | 2023-01-20 | 4        | 15    |
| 3       | 3          | 2023-03-10 | 3        | 18    |
| 4       | 4          | 2023-04-05 | 1        | 20    |
| 5       | 1          | 2023-05-20 | 2        | 10    |
| 6       | 2          | 2023-06-12 | 4        | 15    |
| 7       | 5          | 2023-06-15 | 5        | 12    |
| 8       | 3          | 2023-07-24 | 2        | 18    |
| 9       | 4          | 2023-08-01 | 5        | 20    |
| 10      | 5          | 2023-09-03 | 3        | 12    |
| 11      | 1          | 2023-09-25 | 6        | 10    |
| 12      | 2          | 2023-11-10 | 4        | 15    |
| 13      | 3          | 2023-12-05 | 6        | 18    |
| 14      | 4          | 2023-12-22 | 3        | 20    |
| 15      | 5          | 2024-02-14 | 2        | 12    |
products = 
| product_id | product_name   | category |
| ---------- | -------------- | -------- |
| 1          | Warm Jacket    | Apparel  |
| 2          | Designer Jeans | Apparel  |
| 3          | Cutting Board  | Kitchen  |
| 4          | Smart Speaker  | Tech     |
| 5          | Yoga Mat       | Fitness  |
Output
| season | category | total_quantity | total_revenue |
| ------ | -------- | -------------- | ------------- |
| Fall   | Apparel  | 10             | 120           |
| Spring | Kitchen  | 3              | 54            |
| Summer | Tech     | 5              | 100           |
| Winter | Apparel  | 9              | 110           |
*/
