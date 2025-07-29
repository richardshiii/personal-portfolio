/*
3436. Find Valid Emails
Difficulty: Easy
https://leetcode.com/problems/find-valid-emails/

Table: Users
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| user_id         | int     |
| email           | varchar |
+-----------------+---------+
(user_id) is the unique key for this table.
Each row contains a user's unique ID and email address.
Write a solution to find all the valid email addresses. 
A valid email address meets the following criteria:

It contains exactly one @ symbol.
It ends with .com.
The part before the @ symbol contains only alphanumeric characters and underscores.
The part after the @ symbol and before .com contains a domain name that contains only letters.
Return the result table ordered by user_id in ascending order.
*/
# Solution 
SELECT user_id, email
FROM Users
-- regex expression
-- ^ start of a string
-- [a-zA-Z0-9_] character set of alphanumeric values and underscore
-- +@ matches one preceeding character of @
-- [a-zA-Z] character set of only letters
-- \.com$ matches .com characters and end of string
WHERE email REGEXP '^[a-zA-Z0-9_]+@[a-zA-Z]+\.com$'
ORDER BY user_id asc;

/* 
Test Case
Users = 
| user_id | email               |
| ------- | ------------------- |
| 1       | alice@example.com   |
| 2       | bob_at_example.com  |
| 3       | charlie@example.net |
| 4       | david@domain.com    |
| 5       | eve@invalid         |
Output
| user_id | email             |
| ------- | ----------------- |
| 1       | alice@example.com |
| 4       | david@domain.com  |
*/
