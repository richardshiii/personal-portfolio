/*
196. Delete Duplicate Emails
Difficulty: Easy

Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.

For SQL users, please note that you are supposed to write a DELETE statement and not a SELECT one.

For Pandas users, please note that you are supposed to modify Person in place.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. 
The final order of the Person table does not matter.
*/

# Solution
delete p1
from Person p1
join Person p2
-- Join the table with itself to find duplicates
on p1.email = p2.email and p1.id > p2.id;

/* Test Case
-- Person table
| id | email            |
| -- | ---------------- |
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
Output table
| id | email            |
| -- | ---------------- |
| 1  | john@example.com |
| 2  | bob@example.com  |
*/
