/*
601. Human Traffic of Stadium
Difficulty: Hard
https://leetcode.com/problems/human-traffic-of-stadium/description/

Table: Stadium
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| visit_date    | date    |
| people        | int     |
+---------------+---------+
visit_date is the column with unique values for this table.
Each row of this table contains the visit date and visit id to the stadium with the number of people during the visit.
As the id increases, the date increases as well.
 
Write a solution to display the records with three or more rows with consecutive id's, 
and the number of people is greater than or equal to 100 for each.

Return the result table ordered by visit_date in ascending order.
*/
# Solution
SELECT 
    DISTINCT a.*
FROM 
-- use 3 aliases and self join to find ids that meet requirement
    stadium AS a, stadium AS b, stadium AS c
WHERE
-- having >= 100 people 
     a.people >= 100 AND b.people >= 100 AND c.people >= 100
AND(
-- identify consecutive id requirement by calculating the difference
-- between ids
       (a.id - b.id = 1 AND b.id - c.id = 1)
    OR (c.id - b.id = 1 AND b.id - a.id = 1)
    OR (b.id - a.id = 1 AND a.id - c.id = 1)
    )
-- order by date of visit in ascending order
ORDER BY visit_date

/*
Test Case
Stadium = 
| id | visit_date | people |
| -- | ---------- | ------ |
| 1  | 2017-01-01 | 10     |
| 2  | 2017-01-02 | 109    |
| 3  | 2017-01-03 | 150    |
| 4  | 2017-01-04 | 99     |
| 5  | 2017-01-05 | 145    |
| 6  | 2017-01-06 | 1455   |
| 7  | 2017-01-07 | 199    |
| 8  | 2017-01-09 | 188    |
Output
| id | visit_date | people |
| -- | ---------- | ------ |
| 5  | 2017-01-05 | 145    |
| 6  | 2017-01-06 | 1455   |
| 7  | 2017-01-07 | 199    |
| 8  | 2017-01-09 | 188    |
*/
