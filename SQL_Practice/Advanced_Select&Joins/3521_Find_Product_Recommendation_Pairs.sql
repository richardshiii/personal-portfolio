/*
3521. Find Product Recommendation Pairs
Difficulty: Medium
https://leetcode.com/problems/find-product-recommendation-pairs/description/

Table: ProductPurchases
+-------------+------+
| Column Name | Type | 
+-------------+------+
| user_id     | int  |
| product_id  | int  |
| quantity    | int  |
+-------------+------+
(user_id, product_id) is the unique key for this table.
Each row represents a purchase of a product by a user in a specific quantity.

Table: ProductInfo
+-------------+---------+
| Column Name | Type    | 
+-------------+---------+
| product_id  | int     |
| category    | varchar |
| price       | decimal |
+-------------+---------+
product_id is the primary key for this table.
Each row assigns a category and price to a product.
Amazon wants to implement the Customers who bought this also bought... 
feature based on co-purchase patterns. Write a solution to :

Identify distinct product pairs frequently purchased together by the same customers 
(where product1_id < product2_id)
For each product pair, determine how many customers purchased both products
A product pair is considered for recommendation 
if at least 3 different customers have purchased both products.

Return the result table ordered by customer_count in descending order, 
and in case of a tie, by product1_id in ascending order, and then by product2_id in ascending order.
*/
# Solution 
select 
    pp1.product_id as product1_id, -- select the ID of first product in the pair
    pp2.product_id as product2_id, -- select the ID of second product in the pair
    pi1.category as product1_category, -- category of first product in the pair
    pi2.category as product2_category, -- catefory of second product in the pair
    count(distinct pp1.user_id) as customer_count -- distinct count of customers who bought each product pair
from ProductPurchases pp1
join ProductPurchases pp2
-- use self join to get distinct product pairs purchased by the same customer (product1_id < product2_id)
on pp1.user_id = pp2.user_id and pp1.product_id < pp2.product_id
-- join the productinfo table to get product1's categories for each pair
join ProductInfo pi1 on pp1.product_id = pi1.product_id
-- join the productinfo table to get product2's categories for each pair
join ProductInfo pi2 on pp2.product_id = pi2.product_id
group by pp1.product_id, pp2.product_id, pi1.category, pi2.category
-- only consider for recommendation if at least 3 different customers have purchased the pair
having count(distinct pp1.user_id) >= 3
-- order results by given conditions
order by customer_count desc, product1_id asc, product2_id asc;

/*
Test Case
ProductPurchases = 
| user_id | product_id | quantity |
| ------- | ---------- | -------- |
| 1       | 101        | 2        |
| 1       | 102        | 1        |
| 1       | 103        | 3        |
| 2       | 101        | 1        |
| 2       | 102        | 5        |
| 2       | 104        | 1        |
| 3       | 101        | 2        |
| 3       | 103        | 1        |
| 3       | 105        | 4        |
| 4       | 101        | 1        |
| 4       | 102        | 1        |
| 4       | 103        | 2        |
| 4       | 104        | 3        |
| 5       | 102        | 2        |
| 5       | 104        | 1        |
ProductInfo = 
| product_id | category    | price |
| ---------- | ----------- | ----- |
| 101        | Electronics | 100   |
| 102        | Books       | 20    |
| 103        | Clothing    | 35    |
| 104        | Kitchen     | 50    |
| 105        | Sports      | 75    |
Output
| product1_id | product2_id | product1_category | product2_category | customer_count |
| ----------- | ----------- | ----------------- | ----------------- | -------------- |
| 101         | 102         | Electronics       | Books             | 3              |
| 101         | 103         | Electronics       | Clothing          | 3              |
| 102         | 104         | Books             | Kitchen           | 3              |
*/
