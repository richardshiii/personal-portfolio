'''
2356. Number of Unique Subjects Taught by Each Teacher

Table: Teacher
+-------------+------+
| Column Name | Type |
+-------------+------+
| teacher_id  | int  |
| subject_id  | int  |
| dept_id     | int  |
+-------------+------+
(subject_id, dept_id) is the primary key (combinations of columns with unique values) of this table.
Each row in this table indicates that the teacher with teacher_id teaches the subject subject_id in the department dept_id.
 
Write a solution to calculate the number of unique subjects each teacher teaches in the university.

Return the result table in any order.
'''

# Solution
import pandas as pd

def count_unique_subjects(teacher: pd.DataFrame) -> pd.DataFrame:
    # Group by teacher_id and count the number of unique subject_id for each teacher 
    # nunique() counts the number of distinct values in 'subject_id' for each 'teacher_id'
    teacher = teacher.groupby("teacher_id")["subject_id"].nunique().reset_index()

    teacher = teacher.rename(columns = {"subject_id": "cnt"})
    return teacher

'''
Test Case
| teacher_id | subject_id | dept_id |
| ---------- | ---------- | ------- |
| 1          | 2          | 3       |
| 1          | 2          | 4       |
| 1          | 3          | 3       |
| 2          | 1          | 1       |
| 2          | 2          | 1       |
| 2          | 3          | 1       |
| 2          | 4          | 1       |
Output
| teacher_id | cnt |
| ---------- | --- |
| 1          | 2   |
| 2          | 4   |
'''