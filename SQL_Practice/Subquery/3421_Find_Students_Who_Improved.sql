/*
3421. Find Students Who Improved
Difficulty: Medium
https://leetcode.com/problems/find-students-who-improved/description/

Table: Scores
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student_id  | int     |
| subject     | varchar |
| score       | int     |
| exam_date   | varchar |
+-------------+---------+
(student_id, subject, exam_date) is the primary key for this table.
Each row contains information about a student's score in a specific subject on a particular exam date. 
score is between 0 and 100 (inclusive).
Write a solution to find the students who have shown improvement. 
A student is considered to have shown improvement if they meet both of these conditions:

Have taken exams in the same subject on at least two different dates
Their latest score in that subject is higher than their first score
Return the result table ordered by student_id, subject in ascending order.
*/
# Solution 
-- use CTE to retrieve 1st and latest score for each student and each subject
with CTE as(
    select distinct student_id, subject, 
    -- use window function to get the first and latest score for each subject and student
    -- use first_value function to return the first row of a window frame
    -- retrieve the test score for each student and subject and sort by date asc as the 1st time test score
    -- retrieve the test score for each student and subject and sort by date desc as the latest time test score
        first_value(score) over (partition by student_id, subject order by exam_date asc) as first_score,
        first_value(score) over (partition by student_id, subject order by exam_date desc) as latest_score
    from Scores
)
select *
from CTE 
-- a student shows improvement if the latest score in that subject is higher than the 1st score
where first_score < latest_score
order by student_id, subject asc;

/*
Test Case
Scores = 
| student_id | subject | score | exam_date  |
| ---------- | ------- | ----- | ---------- |
| 101        | Math    | 70    | 2023-01-15 |
| 101        | Math    | 85    | 2023-02-15 |
| 101        | Physics | 65    | 2023-01-15 |
| 101        | Physics | 60    | 2023-02-15 |
| 102        | Math    | 80    | 2023-01-15 |
| 102        | Math    | 85    | 2023-02-15 |
| 103        | Math    | 90    | 2023-01-15 |
| 104        | Physics | 75    | 2023-01-15 |
| 104        | Physics | 85    | 2023-02-15 |
Output
| student_id | subject | first_score | latest_score |
| ---------- | ------- | ----------- | ------------ |
| 101        | Math    | 70          | 85           |
| 102        | Math    | 80          | 85           |
| 104        | Physics | 75          | 85           |
*/
