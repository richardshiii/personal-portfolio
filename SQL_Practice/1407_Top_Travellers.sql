/*
1407. Top Travellers
Difficulty: Easy
https://leetcode.com/problems/top-travellers/description/

Table: Users
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the column with unique values for this table.
name is the name of the user.
 
Table: Rides
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| user_id       | int     |
| distance      | int     |
+---------------+---------+
id is the column with unique values for this table.
user_id is the id of the user who traveled the distance "distance".
 
Write a solution to report the distance traveled by each user.

Return the result table ordered by travelled_distance in descending order, 
if two or more users traveled the same distance, order them by their name in ascending order.
*/
# Solution
select 
    u.name,
    -- calculate the total distance travelled by each traveller
    -- if no info in the distance column, replace with 0
    ifnull(sum(r.distance), 0) as travelled_distance
from Users u
-- match each traveller using their user_id
left join Rides r on u.id = r.user_id
group by u.id
-- sort results by distance in desc order
-- if tie, sort alphabetically;
order by travelled_distance desc, name asc;

/*
Test Case
Users = 
| id | name     |
| -- | -------- |
| 1  | Alice    |
| 2  | Bob      |
| 3  | Alex     |
| 4  | Donald   |
| 7  | Lee      |
| 13 | Jonathan |
| 19 | Elvis    |
Rides = 
| id | user_id | distance |
| -- | ------- | -------- |
| 1  | 1       | 120      |
| 2  | 2       | 317      |
| 3  | 3       | 222      |
| 4  | 7       | 100      |
| 5  | 13      | 312      |
| 6  | 19      | 50       |
| 7  | 7       | 120      |
| 8  | 19      | 400      |
| 9  | 7       | 230      |
Output
| name     | travelled_distance |
| -------- | ------------------ |
| Elvis    | 450                |
| Lee      | 450                |
| Bob      | 317                |
| Jonathan | 312                |
| Alex     | 222                |
| Alice    | 120                |
| Donald   | 0                  |
*/