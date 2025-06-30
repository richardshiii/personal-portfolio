/* 
602. Friend Requests II: Who has the most friends?
Difficulty: Medium

Table: RequestAccepted
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| requester_id   | int     |
| accepter_id    | int     |
| accept_date    | date    |
+----------------+---------+
(requester_id, accepter_id) is the primary key (combination of columns with unique values) for this table.
This table contains the ID of the user who sent the request, the ID of the user who received the request, 
and the date when the request was accepted.

Write a solution to find the people who have the most friends and the most friends number.

The test cases are generated so that only one person has the most friends.
*/

#Solution
with cte as (
    -- select requester_id and accepter_id from RequestAccepted
    -- union them to get all unique ids of users who have sent or accepted requests
    (select requester_id as id
    from RequestAccepted)
    union all
    (select accepter_id as id
    from RequestAccepted)
    )
-- count the number of friends for each user & output the highest count
select id, count(id) as num
from cte
group by id
order by count(id) DESC
limit 1;

/* Test Case
-- RequestAccepted table
| requester_id | accepter_id | accept_date |
| ------------ | ----------- | ----------- |
| 1            | 2           | 2016/06/03  |
| 1            | 3           | 2016/06/08  |
| 2            | 3           | 2016/06/08  |
| 3            | 4           | 2016/06/09  |
Output table
| id | num |
| -- | --- |
| 3  | 3   |
*/

