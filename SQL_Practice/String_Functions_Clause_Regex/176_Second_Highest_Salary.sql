/* 
176. Second Highest Salary
Difficulty: Medium

Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

Write a solution to find the second highest distinct salary from the Employee table. 
If there is no second highest salary, return null (return None in Pandas).
*/

# Solution
select max(salary) as SecondHighestSalary
from Employee
where salary < (select max(salary) from Employee);

/* Test Case
-- Employee table
| id | salary |
| -- | ------ |
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
Output table
| SecondHighestSalary |
| ------------------- |
| 200                 |
*/
