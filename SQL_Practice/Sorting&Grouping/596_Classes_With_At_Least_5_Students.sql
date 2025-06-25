/* 
596. Classes With At Least 5 Students
Difficulty: Easy

Table: Courses
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.

Write a solution to find all the classes that have at least five students.

Return the result table in any order.
*/

# Solution
select class
from Courses
group by class
having count(student) >= 5;

/* Test Case
-- Courses table
| student | class    |
| ------- | -------- |
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
Output table
| class |
| ----- |
| Math  |
*/
