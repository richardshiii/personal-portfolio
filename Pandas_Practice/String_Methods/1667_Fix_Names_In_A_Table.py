'''
1667. Fix Names In A Table

Table: Users
+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| user_id        | int     |
| name           | varchar |
+----------------+---------+
user_id is the primary key (column with unique values) for this table.
This table contains the ID and the name of the user. The name consists of only lowercase and uppercase characters.

Write a solution to fix the names so that only the first character is uppercase and the rest are lowercase.

Return the result table ordered by user_id.
'''

# Solution
import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    # use str.capitalize() to convert the 1st character to uppercase and the rest to lowercase
    users["name"] = users["name"].str.capitalize()
    return users.sort_values(by = "user_id")

'''
Test Case
| user_id | name  |
| ------- | ----- |
| 1       | aLice |
| 2       | bOB   |
Output
| user_id | name  |
| ------- | ----- |
| 1       | Alice |
| 2       | Bob   |
'''
