/*
550. Game Play Analysis IV
Difficulty: Medium

Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key (combination of columns with unique values) of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.

Write a solution to report the fraction of players that logged in again on the day after the day they first logged in, 
rounded to 2 decimal places. In other words, you need to determine the number of players who logged in on the day immediately following their initial login, 
and divide it by the number of total players.
*/

# Solution
-- Fraction of players who logged in again the day after their first login
SELECT ROUND(COUNT(DISTINCT player_id) / 
    (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) 
    as fraction 
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
IN 
(
-- Get the first login date for each player
SELECT player_id, MIN(event_date) AS first_login 
FROM ACTIVITY 
GROUP BY player_id 
);

/* Test Case
-- Activity table
| player_id | device_id | event_date | games_played |
| --------- | --------- | ---------- | ------------ |
| 1         | 2         | 2016-03-01 | 5            |
| 1         | 2         | 2016-03-02 | 6            |
| 2         | 3         | 2017-06-25 | 1            |
| 3         | 1         | 2016-03-02 | 0            |
| 3         | 4         | 2018-07-03 | 5            |
Output table
| fraction |
| -------- |
| 0.33     |
*/
