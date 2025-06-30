/*
180. Consecutive Numbers
Difficulty: Medium

Table: Logs
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
In SQL, id is the primary key for this table.
id is an autoincrement column starting from 1.

Find all numbers that appear at least three times consecutively.

Return the result table in any order.
*/

# Solution
-- create a CTE to find the previous and next number for each row
with cte as 
(
    select num, 
    lead(num) over (order by id) as next_num,
    lag(num) over (order by id) as prev_num
    from Logs
) 
-- filter the CTE to find numbers that are equal to both previous and next number
-- as the consecutive numbers
select distinct num as ConsecutiveNums
from cte
where num = prev_num and num = next_num;

/* Test Case
-- Logs table
| id | num |
| -- | --- |
| 1  | 1   |
| 2  | 1   |
| 3  | 1   |
| 4  | 2   |
| 5  | 1   |
| 6  | 2   |
| 7  | 2   |
Output table
| ConsecutiveNums |
| --------------- |
| 1               | 
*/
