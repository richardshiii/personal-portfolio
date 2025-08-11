/* 
185. Department Top Three Salaries
Difficulty: Hard

Table: Employee
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| id           | int     |
| name         | varchar |
| salary       | int     |
| departmentId | int     |
+--------------+---------+
id is the primary key (column with unique values) for this table.
departmentId is a foreign key (reference column) of the ID from the Department table.
Each row of this table indicates the ID, name, and salary of an employee. 
It also contains the ID of their department.
 
Table: Department
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table indicates the ID of a department and its name.
 
A company's executives are interested in seeing who earns the most money in each of the company's departments. 
A high earner in a department is an employee who has a salary in the top three unique salaries for that department.

Write a solution to find the employees who are high earners in each of the departments.

Return the result table in any order.
*/

# Solution
select d.name as Department, 
        e.name as Employee, 
        e.salary as Salary
from Employee e
join Department d on e.departmentid = d.id
where (
    -- Count distinct salaries greater than the current employee's salary in the same department
    select count(distinct e2.salary) 
    from Employee e2
    where e2.departmentid = e.departmentid and e2.salary > e.salary
-- Count must be less than 3 to be in the top three salaries
) < 3;

-- alternative solution using dense_rank()
select d.name as Department, e.name as Employee, e.salary as Salary
from
-- create a derived table
-- use dense_rank() to rank employee within each department 
( select *, 
dense_rank() over (partition by departmentId order by salary DESC) as rnk
from Employee) as e
-- join two tables and only include top 3 salaries in each department
join Department d on e.departmentId = d.id
where e.rnk <= 3;

/* Test Case
Employee table = 
| id | name  | salary | departmentId |
| -- | ----- | ------ | ------------ |
| 1  | Joe   | 85000  | 1            |
| 2  | Henry | 80000  | 2            |
| 3  | Sam   | 60000  | 2            |
| 4  | Max   | 90000  | 1            |
| 5  | Janet | 69000  | 1            |
| 6  | Randy | 85000  | 1            |
| 7  | Will  | 70000  | 1            |
Department table = 
| id | name  |
| -- | ----- |
| 1  | IT    |
| 2  | Sales |
Output table
| Department | Employee | Salary |
| ---------- | -------- | ------ |
| IT         | Joe      | 85000  |
| Sales      | Henry    | 80000  |
| Sales      | Sam      | 60000  |
| IT         | Max      | 90000  |
| IT         | Randy    | 85000  |
| IT         | Will     | 70000  |
*/
