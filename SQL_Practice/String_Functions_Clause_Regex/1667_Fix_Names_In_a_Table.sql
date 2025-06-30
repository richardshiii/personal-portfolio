/* 
1667. Fix Names in a Table
Difficulty: Easy

Table: Users
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.
*/

# Solution
select user_id, 
    -- Use string functions to format the name
    -- Convert the first character to uppercase and the rest to lowercase
    concat(upper(left(name, 1)), lower(substring(name, 2))) as name
from Users
order by user_id ASC; 

/* Test Case
-- Users table
| user_id | name  |
| ------- | ----- |
| 1       | aLice |
| 2       | bOB   |
Output table
| user_id | name  |
| ------- | ----- |
| 1       | Alice |
| 2       | Bob   |
*/
