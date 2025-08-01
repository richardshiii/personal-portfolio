/*
3465.Find Products with Valid Serial Numers
Difficulty: Easy
https://leetcode.com/problems/find-products-with-valid-serial-numbers/description/

Table: products
+--------------+------------+
| Column Name  | Type       |
+--------------+------------+
| product_id   | int        |
| product_name | varchar    |
| description  | varchar    |
+--------------+------------+
(product_id) is the unique key for this table.
Each row in the table represents a product with its unique ID, name, and description.
Write a solution to find all products whose description contains a valid serial number pattern. 
A valid serial number follows these rules:

It starts with the letters SN (case-sensitive).
Followed by exactly 4 digits.
It must have a hyphen (-) followed by exactly 4 digits.
The serial number must be within the description (it may not necessarily start at the beginning).
Return the result table ordered by product_id in ascending order.
*/
# Solution 
select *
from products
-- use regexp_like function to pattern match using regex
-- source string is the description column
-- \\bSN[0-9]{4}-[0-9]{4}\\b is the regex expression
-- 'c' indicates case sensitive matching
where regexp_like (description, '\\bSN[0-9]{4}-[0-9]{4}\\b', 'c')
order by product_id;

/*
Test Case
products = 
| product_id | product_name | description                                          |
| ---------- | ------------ | ---------------------------------------------------- |
| 1          | Widget A     | This is a sample product with SN1234-5678            |
| 2          | Widget B     | A product with serial SN9876-1234 in the description |
| 3          | Widget C     | Product SN1234-56789 is available now                |
| 4          | Widget D     | No serial number here                                |
| 5          | Widget E     | Check out SN4321-8765 in this description            |
Output
| product_id | product_name | description                                          |
| ---------- | ------------ | ---------------------------------------------------- |
| 1          | Widget A     | This is a sample product with SN1234-5678            |
| 2          | Widget B     | A product with serial SN9876-1234 in the description |
| 5          | Widget E     | Check out SN4321-8765 in this description            |
*/