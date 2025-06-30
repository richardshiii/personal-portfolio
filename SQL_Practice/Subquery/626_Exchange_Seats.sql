/* 
626. Exchange Seats
Difficulty: Medium

Table: Seat
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (unique value) column for this table.
Each row of this table indicates the name and the ID of a student.
The ID sequence always starts from 1 and increments continuously.

Write a solution to swap the seat id of every two consecutive students. 
If the number of students is odd, the id of the last student is not swapped.

Return the result table ordered by id in ascending order.
*/

# Solution
with cte as (
    select id, 
    case when id % 2 = 1  and id + 1 <= (select max(id) from Seat) then id + 1
    when id % 2 = 0 then id - 1
    else id
    end as swapped,
    student 
    from Seat
)
select swapped as id, student
from cte
order by id;

/* Test Case
-- Seat table
| id | student |
| -- | ------- |
| 1  | Abbot   |
| 2  | Doris   |
| 3  | Emerson |
| 4  | Green   |
| 5  | Jeames  |
Output table
| id | student |
| -- | ------- |
| 1  | Doris   |
| 2  | Abbot   |
| 3  | Green   |
| 4  | Emerson |
| 5  | Jeames  |
*/
