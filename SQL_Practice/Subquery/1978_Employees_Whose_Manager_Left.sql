/* 
1978. Employees Whose Manager Left the Company
Difficulty: Easy

Table: Employees
+-------------+----------+
| Column Name | Type     |
+-------------+----------+
| employee_id | int      |
| name        | varchar  |
| manager_id  | int      |
| salary      | int      |
+-------------+----------+
In SQL, employee_id is the primary key for this table.
This table contains information about the employees, their salary, and the ID of their manager. Some employees do not have a manager (manager_id is null). 

Find the IDs of the employees whose salary is strictly less than $30000 and whose manager left the company. When a manager leaves the company, their information is deleted from the Employees table, but the reports still have their manager_id set to the manager that left.

Return the result table ordered by employee_id.
*/

# Solution
select employee_id 
from Employees
-- Check if salary is less than $30000
where salary < 30000 and 
    -- Ensure the employee has a manager
      manager_id is not null and 
    -- Check if the manager is still in the company
    manager_id not in ( 
        select employee_id
        from Employees
    )
order by employee_id;

/* Test Case
-- Employees table
| employee_id | name      | manager_id | salary |
| ----------- | --------- | ---------- | ------ |
| 3           | Mila      | 9          | 60301  |
| 12          | Antonella | null       | 31000  |
| 13          | Emery     | null       | 67084  |
| 1           | Kalel     | 11         | 21241  |
| 9           | Mikaela   | null       | 50937  |
| 11          | Joziah    | 6          | 28485  |
Output table
| employee_id |
| ----------- |
| 11          |
*/
