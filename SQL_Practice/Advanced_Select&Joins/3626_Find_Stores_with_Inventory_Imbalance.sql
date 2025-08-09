/*
3626. Find Stores with Inventory Imbalance
Difficulty: Medium
https://leetcode.com/problems/find-stores-with-inventory-imbalance/description/

Table: stores
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| store_id    | int     |
| store_name  | varchar |
| location    | varchar |
+-------------+---------+
store_id is the unique identifier for this table.
Each row contains information about a store and its location.

Table: inventory
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| inventory_id| int     |
| store_id    | int     |
| product_name| varchar |
| quantity    | int     |
| price       | decimal |
+-------------+---------+
inventory_id is the unique identifier for this table.
Each row represents the inventory of a specific product at a specific store.
Write a solution to find stores that have inventory imbalance - 
stores where the most expensive product has lower stock than the cheapest product.

For each store, identify the most expensive product (highest price) and its quantity
For each store, identify the cheapest product (lowest price) and its quantity
A store has inventory imbalance if the most expensive product's quantity is less than the cheapest product's quantity
Calculate the imbalance ratio as (cheapest_quantity / most_expensive_quantity)
Round the imbalance ratio to 2 decimal places
Only include stores that have at least 3 different products
Return the result table ordered by imbalance ratio in descending order, then by store name in ascending order.
*/
# Solution 
-- find qualified stores
-- only include stores that has at least 3 different products
-- find the max and min price of products for each store
with qualified_store as (
select s.store_id, s.store_name, s.location,
    max(i.price) as max_price, 
    min(i.price) as min_price
from stores s 
join inventory i on s.store_id = i.store_id
group by s.store_id, s.store_name, s.location
having count(distinct i.product_name) > 2
),
-- find the most expensive and cheapest product for each qualified store
expensive_cheap_products as (
    select i.store_id, q.store_name, q.location, i.quantity,
    i.product_name, i.price
    from inventory i
    join qualified_store q on i.store_id = q.store_id
-- filter only the most expensive and cheapest product in each store
    and (i.price = q.max_price or i.price = q.min_price)
)
-- calculate the imbalance ratio as cheapest quantity / most expensive quantity
-- use self join to find qualifying stores
-- sort results according to requirements
select e.store_id, e.store_name, e.location, e2.product_name as most_exp_product,
e.product_name as cheapest_product, 
round(e.quantity / e2.quantity, 2) as imbalance_ratio
from expensive_cheap_products e
-- use self join 
-- use e.price < e2.price to pair the cheapest product from the first copy(e) 
-- with the most expensive product from the second copy (e2)
-- check if the cheap product's quantity is greater then expensive product's
join expensive_cheap_products e2
on e.store_id = e2.store_id
and e.price < e2.price and e.quantity > e2.quantity
order by imbalance_ratio DESC, store_name ASC;

/*
Test Case
stores = 
| store_id | store_name    | location    |
| -------- | ------------- | ----------- |
| 1        | Downtown Tech | New York    |
| 2        | Suburb Mall   | Chicago     |
| 3        | City Center   | Los Angeles |
| 4        | Corner Shop   | Miami       |
| 5        | Plaza Store   | Seattle     |
inventory = 
| inventory_id | store_id | product_name | quantity | price  |
| ------------ | -------- | ------------ | -------- | ------ |
| 1            | 1        | Laptop       | 5        | 999.99 |
| 2            | 1        | Mouse        | 50       | 19.99  |
| 3            | 1        | Keyboard     | 25       | 79.99  |
| 4            | 1        | Monitor      | 15       | 299.99 |
| 5            | 2        | Phone        | 3        | 699.99 |
| 6            | 2        | Charger      | 100      | 25.99  |
| 7            | 2        | Case         | 75       | 15.99  |
| 8            | 2        | Headphones   | 20       | 149.99 |
| 9            | 3        | Tablet       | 2        | 499.99 |
| 10           | 3        | Stylus       | 80       | 29.99  |
| 11           | 3        | Cover        | 60       | 39.99  |
| 12           | 4        | Watch        | 10       | 299.99 |
| 13           | 4        | Band         | 25       | 49.99  |
| 14           | 5        | Camera       | 8        | 599.99 |
| 15           | 5        | Lens         | 12       | 199.99 |
Output
| store_id | store_name    | location    | most_exp_product | cheapest_product | imbalance_ratio |
| -------- | ------------- | ----------- | ---------------- | ---------------- | --------------- |
| 3        | City Center   | Los Angeles | Tablet           | Stylus           | 40              |
| 2        | Suburb Mall   | Chicago     | Phone            | Case             | 25              |
| 1        | Downtown Tech | New York    | Laptop           | Mouse            | 10              |
*/
