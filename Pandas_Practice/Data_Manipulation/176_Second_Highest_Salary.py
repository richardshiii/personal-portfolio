'''
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
'''

# Solution
import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    unique_salary = employee["salary"].drop_duplicates()
    # if there are at least two distinct salaries, get the second highest
    # otherwise, return None
    if len(unique_salary) >= 2:
        second_highest = unique_salary.nlargest(2).iloc[-1] 
    else:
        second_highest = None
    
    if second_highest is None:
        return pd.DataFrame({"SecondHighestSalary": [None]})
    else:
        return pd.DataFrame({"SecondHighestSalary": [second_highest]})
    
'''
Test Case
| id | salary |
| -- | ------ |
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
Output
| SecondHighestSalary |
| ------------------- |
| 200                 |
'''