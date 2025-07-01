'''
596. Classes With At Least 5 Students

Table: Courses
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| student     | varchar |
| class       | varchar |
+-------------+---------+
(student, class) is the primary key (combination of columns with unique values) for this table.
Each row of this table indicates the name of a student and the class in which they are enrolled.
 
Write a solution to find all the classes that have at least five students.

Return the result table in any order.
'''

# Solution
import pandas as pd

def find_classes(courses: pd.DataFrame) -> pd.DataFrame:
    # Group by 'class' and count the number of unique student in each class
    courses = courses.groupby("class")["student"].count().reset_index()
    # Filter classes with at least 5 students and drop the 'student' column
    filtered_df = courses[courses["student"] >= 5].drop(columns = "student")
    return filtered_df

'''
Test Case
| student | class    |
| ------- | -------- |
| A       | Math     |
| B       | English  |
| C       | Math     |
| D       | Biology  |
| E       | Math     |
| F       | Computer |
| G       | Math     |
| H       | Math     |
| I       | Math     |
Output
| class |
| ----- |
| Math  |
'''