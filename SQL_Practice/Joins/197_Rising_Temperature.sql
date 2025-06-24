/*
197. Rising Temperature
Difficulty: Easy

Table: Weather
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the column with unique values for this table.
There are no different rows with the same recordDate.
This table contains information about the temperature on a certain day.
 
Write a solution to find all dates' id with higher temperatures compared to its previous dates (yesterday).

Return the result table in any order.
*/

# Solution
SELECT w1.id
FROM Weather w1 -- w1 represents the current day and w2 represents the previous day
JOIN Weather w2 -- Join the Weather table with itself
ON datediff(w1.recordDate, w2.recordDate) = 1 -- Ensure that w1 is the day after w2
WHERE w1.temperature > w2.temperature; -- Compare the temperatures of the two days

/* Test Case
-- Weather table
| id | recordDate | temperature |
| -- | ---------- | ----------- |
| 1  | 2015-01-01 | 10          |
| 2  | 2015-01-02 | 25          |
| 3  | 2015-01-03 | 20          |
| 4  | 2015-01-04 | 30          |

Output table
| id |
| -- |
| 2  |
| 4  |
*/

