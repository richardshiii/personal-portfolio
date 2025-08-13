/*
3482. Analyze Organization Hierarchy
Difficulty: Hard
https://leetcode.com/problems/analyze-organization-hierarchy/description/

Table: Employees
+----------------+---------+
| Column Name    | Type    | 
+----------------+---------+
| employee_id    | int     |
| employee_name  | varchar |
| manager_id     | int     |
| salary         | int     |
| department     | varchar |
+----------------+----------+
employee_id is the unique key for this table.
Each row contains information about an employee, including their ID, name, their manager's ID, salary, and department.
manager_id is null for the top-level manager (CEO).
Write a solution to analyze the organizational hierarchy and answer the following:

Hierarchy Levels: For each employee, determine their level in the organization (CEO is level 1, employees reporting directly to the CEO are level 2, and so on).
Team Size: For each employee who is a manager, count the total number of employees under them (direct and indirect reports).
Salary Budget: For each manager, calculate the total salary budget they control (sum of salaries of all employees under them, including indirect reports, plus their own salary).
Return the result table ordered by the result ordered by level in ascending order, then by budget in descending order, and finally by employee_name in ascending order.
*/
# Solution 
/* 
Recursive CTE
- great for hierarchical data like organizational chart
- anchor member: non-recursive query that selects the base rows -> root of hierarchy
- recursive member: references the CTE itself and joins it with the original table. 
It finds the next set of rows based on the results from the previous step. 
This process repeats until the query returns no more new rows.
- Union All: joins the anchor and recursive parts in each iteration
*/
with recursive leadership as(
    select manager_id ,employee_id ,employee_name ,salary,1 as level
    from Employees 
    where manager_id is null
    union all
    select e.manager_id ,e.employee_id ,e.employee_name ,e.salary,level+1 level
    from Employees e
    join leadership l
    on e.manager_id =l.employee_id 
),
subordinate as(
    select employee_id ,salary ,manager_id 
    from Employees 
    union all
    select e.employee_id ,e.salary ,s.manager_id 
    from Employees e
    join subordinate s
    on s.employee_id=e.manager_id 
)
,
final as(
    select l.employee_id,l.employee_name,level,
    count(s.employee_id)team_size ,
    ifnull(sum(s.salary),0)+l.salary budget 
    from leadership l
    left join subordinate s
    on s.manager_id=l.employee_id
    group by 1,2,3,l.salary
)
select * from final
order by 3, 5 desc,2

/*
Test Case
| employee_id | employee_name | manager_id | salary | department  |
| ----------- | ------------- | ---------- | ------ | ----------- |
| 1           | Alice         | null       | 12000  | Executive   |
| 2           | Bob           | 1          | 10000  | Sales       |
| 3           | Charlie       | 1          | 10000  | Engineering |
| 4           | David         | 2          | 7500   | Sales       |
| 5           | Eva           | 2          | 7500   | Sales       |
| 6           | Frank         | 3          | 9000   | Engineering |
| 7           | Grace         | 3          | 8500   | Engineering |
| 8           | Hank          | 4          | 6000   | Sales       |
| 9           | Ivy           | 6          | 7000   | Engineering |
| 10          | Judy          | 6          | 7000   | Engineering |
Output
| employee_id | employee_name | level | team_size | budget |
| ----------- | ------------- | ----- | --------- | ------ |
| 1           | Alice         | 1     | 9         | 84500  |
| 3           | Charlie       | 2     | 4         | 41500  |
| 2           | Bob           | 2     | 3         | 31000  |
| 6           | Frank         | 3     | 2         | 23000  |
| 4           | David         | 3     | 1         | 13500  |
| 7           | Grace         | 3     | 0         | 8500   |
| 5           | Eva           | 3     | 0         | 7500   |
| 9           | Ivy           | 4     | 0         | 7000   |
| 10          | Judy          | 4     | 0         | 7000   |
| 8           | Hank          | 4     | 0         | 6000   |
*/

