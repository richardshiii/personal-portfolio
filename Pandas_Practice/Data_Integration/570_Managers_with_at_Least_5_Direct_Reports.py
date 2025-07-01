'''
570. Managers with at least 5 direct reports

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
'''

# Solution
import pandas as pd

def find_managers(employee: pd.DataFrame) -> pd.DataFrame:
    # The .query('id >= 5') filters groups where the count of 
    # direct reports (rows per managerId) is at least 5.
    manager = employee.groupby('managerId', as_index = False).count().query('id >= 5')
    return employee[employee["id"].isin(manager["managerId"])][["name"]]

'''
Test Case
| id  | name  | department | managerId |
| --- | ----- | ---------- | --------- |
| 101 | John  | A          | null      |
| 102 | Dan   | A          | 101       |
| 103 | James | A          | 101       |
| 104 | Amy   | A          | 101       |
| 105 | Anne  | A          | 101       |
| 106 | Ron   | B          | 101       |
Output
| name |
| ---- |
| John |
'''