/*
1965. Employees with missing information
Difficulty: Easy
https://leetcode.com/problems/employees-with-missing-information/

Table: Employees
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the name of the employee whose ID is employee_id.

Table: Salaries
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| salary      | int     |
+-------------+---------+
employee_id is the column with unique values for this table.
Each row of this table indicates the salary of the employee whose ID is employee_id.
 
Write a solution to report the IDs of all the employees with missing information. 
The information of an employee is missing if:

The employee's name is missing, or
The employee's salary is missing.
Return the result table ordered by employee_id in ascending order.
*/
# Solution 
-- use common table expression and outer joins to 
-- implement full outer join of two input tables
with cte as (
    select * 
    from Employees 
        left join Salaries using (employee_id)
    union
    select *
    from Employees
        right join Salaries using (employee_id)
)
select employee_id 
from cte
-- retrieve specific rows based on given condition
where name is null or salary is null
order by employee_id asc;

/*
Test Case
Employees = 
| employee_id | name     |
| ----------- | -------- |
| 2           | Crew     |
| 4           | Haven    |
| 5           | Kristian |
Salaries = 
| employee_id | salary |
| ----------- | ------ |
| 5           | 76071  |
| 1           | 22517  |
| 4           | 63539  |
Output
| employee_id |
| ----------- |
| 1           |
| 2           |
*/
