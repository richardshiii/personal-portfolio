/*
1729. Find Followers Count
Difficulty: Easy

Table: Followers
+-------------+------+
| Column Name | Type |
+-------------+------+
| user_id     | int  |
| follower_id | int  |
+-------------+------+
(user_id, follower_id) is the primary key (combination of columns with unique values) for this table.
This table contains the IDs of a user and a follower in a social media app where the follower follows the user.

Write a solution that will, for each user, return the number of followers.

Return the result table ordered by user_id in ascending order.
*/

# Solution
select user_id, count(follower_id) as followers_count
from Followers
group by user_id
order by user_id ASC; 

/* Test Case
-- Followers table
| user_id | follower_id |
| ------- | ----------- |
| 0       | 1           |
| 1       | 0           |
| 2       | 0           |
| 2       | 1           |
Output table
| user_id | followers_count |
| ------- | --------------- |
| 0       | 1               |
| 1       | 1               |
| 2       | 2               |
*/
