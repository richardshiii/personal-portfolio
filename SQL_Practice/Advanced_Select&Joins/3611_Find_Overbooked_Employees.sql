/*
3611. Find Overbooked Employees
Difficulty: Medium
https://leetcode.com/problems/find-overbooked-employees/description/

Table: employees
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| employee_id   | int     |
| employee_name | varchar |
| department    | varchar |
+---------------+---------+
employee_id is the unique identifier for this table.
Each row contains information about an employee and their department.

Table: meetings
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| meeting_id    | int     |
| employee_id   | int     |
| meeting_date  | date    |
| meeting_type  | varchar |
| duration_hours| decimal |
+---------------+---------+
meeting_id is the unique identifier for this table.
Each row represents a meeting attended by an employee. meeting_type can be 'Team', 'Client', or 'Training'.
Write a solution to find employees who are meeting-heavy - 
employees who spend more than 50% of their working time in meetings during any given week.

Assume a standard work week is 40 hours
Calculate total meeting hours per employee per week (Monday to Sunday)
An employee is meeting-heavy if their weekly meeting hours > 20 hours (50% of 40 hours)
Count how many weeks each employee was meeting-heavy
Only include employees who were meeting-heavy for at least 2 weeks
Return the result table ordered by the number of meeting-heavy weeks in descending order, 
then by employee name in ascending order.
*/
# Solution 
-- calculate weekly meeting hours for each employee
-- yearweek() function is used to extract week number from given date
-- 3: mode 3, select Monday as the start of a week instead of Sunday (0)
with weekly_hours as (
select employee_id, yearweek(meeting_date, 3) as meeting_week, sum(duration_hours) as weekly_hours
from meetings
group by employee_id, meeting_week
)
select w.employee_id, e.employee_name, e.department, 
count(w.weekly_hours) as meeting_heavy_weeks
from weekly_hours w
join employees e
on w.employee_id = e.employee_id
-- meeting-heavy week is defined by having > 20 weekly meeting hours
where weekly_hours > 20
group by employee_id, employee_name, department
-- extract employees having >=2 meeting-heavy weeks
having meeting_heavy_weeks > 1
order by meeting_heavy_weeks DESC, employee_name ASC;

/* 
Test Case
employees = 
| employee_id | employee_name | department  |
| ----------- | ------------- | ----------- |
| 1           | Alice Johnson | Engineering |
| 2           | Bob Smith     | Marketing   |
| 3           | Carol Davis   | Sales       |
| 4           | David Wilson  | Engineering |
| 5           | Emma Brown    | HR          |
meetings = 
| meeting_id | employee_id | meeting_date | meeting_type | duration_hours |
| ---------- | ----------- | ------------ | ------------ | -------------- |
| 1          | 1           | 2023-06-05   | Team         | 8              |
| 2          | 1           | 2023-06-06   | Client       | 6              |
| 3          | 1           | 2023-06-07   | Training     | 7              |
| 4          | 1           | 2023-06-12   | Team         | 12             |
| 5          | 1           | 2023-06-13   | Client       | 9              |
| 6          | 2           | 2023-06-05   | Team         | 15             |
| 7          | 2           | 2023-06-06   | Client       | 8              |
| 8          | 2           | 2023-06-12   | Training     | 10             |
| 9          | 3           | 2023-06-05   | Team         | 4              |
| 10         | 3           | 2023-06-06   | Client       | 3              |
| 11         | 4           | 2023-06-05   | Team         | 25             |
| 12         | 4           | 2023-06-19   | Client       | 22             |
| 13         | 5           | 2023-06-05   | Training     | 2              |
Output
| employee_id | employee_name | department  | meeting_heavy_weeks |
| ----------- | ------------- | ----------- | ------------------- |
| 1           | Alice Johnson | Engineering | 2                   |
| 4           | David Wilson  | Engineering | 2                   |
*/
