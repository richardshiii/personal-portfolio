/* 
570. Managers with At Least 5 Direct Reports
Difficulty: Medium

Table: Employee
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| department  | varchar |
| managerId   | int     |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the name of an employee, their department, and the id of their manager.
If managerId is null, then the employee does not have a manager.
No employee will be the manager of themself.
 
Write a solution to find managers with at least five direct reports.

Return the result table in any order.
*/

# Solution
select e1.name
from Employee e1
join Employee e2 -- Join the Employee table to itself to find managers and their direct reports
on e1.id = e2.managerID -- Match the manager's id with the direct report's managerId
where e1.managerID is null -- Ensure we are only considering managers
group by e2.managerID
having count(e2.managerID) >= 5; 

/* Test Case
-- Employee table
| id  | name  | department | managerId |
| --- | ----- | ---------- | --------- |
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       | 
Output table
| name |
| ---- |
| John |
*/