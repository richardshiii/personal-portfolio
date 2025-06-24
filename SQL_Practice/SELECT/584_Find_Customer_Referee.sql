/*
584. Find Customer Referee
Difficulty: Easy

Table: Customer
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| referee_id  | int     |
+-------------+---------+
In SQL, id is the primary key column for this table.
Each row of this table indicates the id of a customer, their name, and the id of the customer who referred them.
 

Find the names of the customer that are not referred by the customer with id = 2.

Return the result table in any order.
*/

# Solution:
SELECT name
FROM Customer
WHERE referee_id IS NULL OR referee_id != 2;
-- The query selects the names of customers who are either not referred by anyone (referee_id IS NULL) 
-- or not referred by the customer with id = 2 (referee_id != 2)

/*Test Case
-- Customer table
| id | name | referee_id |
| -- | ---- | ---------- |
| 1  | Will | null       |
| 2  | Jane | null       |
| 3  | Alex | 2          |
| 4  | Bill | null       |
| 5  | Zack | 1          |
| 6  | Mark | 2          |

Output table
| name |
| ---- |
| Will |
| Jane |
| Bill |
| Zack |
*/