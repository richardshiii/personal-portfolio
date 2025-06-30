/*
1731. The Number of Employees Which Report to Each Employee
Difficulty: Easy

Table: Employees
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| reports_to  | int      |
| age         | int      |
+-------------+----------+
employee_id is the column with unique values for this table.
This table contains information about the employees and the id of the manager they report to. 
Some employees do not report to anyone (reports_to is null). 

For this problem, we will consider a manager an employee who has at least 1 other employee reporting to them.

Write a solution to report the ids and the names of all managers, the number of employees who report directly to them, 
and the average age of the reports rounded to the nearest integer.

Return the result table ordered by employee_id.
*/

# Solution
select e1.employee_id, e1.name, 
    count(e2.employee_id) as reports_count, 
    round(avg(e2.age)) as average_age
from Employees e1
join Employees e2
on e1.employee_id = e2.reports_to -- self join to get employees reporting to the manager
group by e1.employee_id, e1.name
order by e1.employee_id;

/* Test Case
-- Employees table
| employee_id | name    | reports_to | age |
| ----------- | ------- | ---------- | --- |
| 1           | Michael | null       | 45  |
| 2           | Alice   | 1          | 38  |
| 3           | Bob     | 1          | 42  |
| 4           | Charlie | 2          | 34  |
| 5           | David   | 2          | 40  |
| 6           | Eve     | 3          | 37  |
| 7           | Frank   | null       | 50  |
| 8           | Grace   | null       | 48  |
Output table
| employee_id | name    | reports_count | average_age |
| ----------- | ------- | ------------- | ----------- |
| 1           | Michael | 2             | 40          |
| 2           | Alice   | 2             | 37          |
| 3           | Bob     | 1             | 37          |
*/
