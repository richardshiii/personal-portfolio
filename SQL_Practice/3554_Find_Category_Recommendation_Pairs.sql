/*
3554. Find Category Recommendation Pairs
Difficulty: Hard
https://leetcode.com/problems/find-category-recommendation-pairs/description/

Table: ProductPurchases
+-------------+------+
| Column Name | Type | 
+-------------+------+
| user_id     | int  |
| product_id  | int  |
| quantity    | int  |
+-------------+------+
(user_id, product_id) is the unique identifier for this table. 
Each row represents a purchase of a product by a user in a specific quantity.

Table: ProductInfo
+-------------+---------+
| Column Name | Type    | 
+-------------+---------+
| product_id  | int     |
| category    | varchar |
| price       | decimal |
+-------------+---------+
product_id is the unique identifier for this table.
Each row assigns a category and price to a product.
Amazon wants to understand shopping patterns across product categories. Write a solution to:

Find all category pairs (where category1 < category2)
For each category pair, determine the number of unique customers who purchased products from both categories
A category pair is considered reportable if at least 3 different customers have purchased products from both categories.

Return the result table of reportable category pairs ordered by customer_count in descending order, 
and in case of a tie, by category1 in ascending order lexicographically, and then by category2 in ascending order.
*/
# Solution 
-- connect each product with product category 
with product_category as (
select pp.user_id, pi.category
from ProductPurchases pp
join ProductInfo pi on pp.product_id = pi.product_id
), 
-- use self join to find product category pair each users purchases
-- category pair is defined by category1<category2
category_pairs as (
select pc1.user_id, pc1.category as category1, pc2.category as category2
from product_category pc1
join product_category pc2 on pc1.user_id = pc2.user_id
where pc1.category < pc2.category
)
-- for each category pair, find the number of unique customers that purchased
-- both products from both categories
-- count(distinct user_id) for each category pair
select category1, category2, 
count(distinct user_id) as customer_count
from category_pairs
group by category1, category2
-- category pair is considered reportable if at least 3 different 
-- customers have purchased products from both categories
having customer_count >= 3
order by customer_count desc, category1 asc, category2 asc;

/*
Test Case
ProductPurchases = 
| user_id | product_id | quantity |
| ------- | ---------- | -------- |
| 1       | 101        | 2        |
| 1       | 102        | 1        |
| 1       | 201        | 3        |
| 1       | 301        | 1        |
| 2       | 101        | 1        |
| 2       | 102        | 2        |
| 2       | 103        | 1        |
| 2       | 201        | 5        |
| 3       | 101        | 2        |
| 3       | 103        | 1        |
| 3       | 301        | 4        |
| 3       | 401        | 2        |
| 4       | 101        | 1        |
| 4       | 201        | 3        |
| 4       | 301        | 1        |
| 4       | 401        | 2        |
| 5       | 102        | 2        |
| 5       | 103        | 1        |
| 5       | 201        | 2        |
| 5       | 202        | 3        |
ProductInfo = 
| product_id | category    | price |
| ---------- | ----------- | ----- |
| 101        | Electronics | 100   |
| 102        | Books       | 20    |
| 103        | Books       | 35    |
| 201        | Clothing    | 45    |
| 202        | Clothing    | 60    |
| 301        | Sports      | 75    |
| 401        | Kitchen     | 50    |
Output
| category1   | category2   | customer_count |
| ----------- | ----------- | -------------- |
| Books       | Clothing    | 3              |
| Books       | Electronics | 3              |
| Clothing    | Electronics | 3              |
| Electronics | Sports      | 3              |
*/
