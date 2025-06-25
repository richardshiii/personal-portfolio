/*
619. Biggest Single Number
Difficulty: Easy

Table: MyNumbers
+-------------+------+
| Column Name | Type |
+-------------+------+
| num         | int  |
+-------------+------+
This table may contain duplicates (In other words, there is no primary key for this table in SQL).
Each row of this table contains an integer.
 
A single number is a number that appeared only once in the MyNumbers table.

Find the largest single number. If there is no single number, report null.
*/

# Solution
with CTE as (
    select num 
    from MyNumbers
    group by num
    having count(num) = 1
)
select max(num) as num
from CTE;

/* Test Case
-- MyNumbers table
| num |
| --- |
| 8   |
| 8   |
| 3   |
| 3   |
| 1   |
| 4   |
| 5   |
| 6   |
Output table
| num |
| --- |
| 6   |
*/