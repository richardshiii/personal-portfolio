'''
177. Nth Highest Salary
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
 
Write a solution to find the nth highest distinct salary from the Employee table. 
If there are less than n distinct salaries, return null.
'''

# Solution
import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    # Drop duplicates in the salary column and sort the values in descending order
    employee_no_dupe = employee["salary"].drop_duplicates()
    employee_sorted = employee_no_dupe.sort_values(ascending = False)
    # Check if N is valid
    # If N is greater than the number of distinct salaries or less than or equal to 0, return None
    if N > len(employee_sorted) or N <= 0:
        return pd.DataFrame({"getNthHighestSalary({})".format(N):[None]})
    # Get the N-th highest salary
    # N-1 because of zero-based indexing
    nth = employee_sorted.iloc[N - 1]
    return pd.DataFrame({"getNthHighestSalary({})".format(N): [nth]})

'''
Test Case
| id | salary |
| -- | ------ |
| 1  | 100    |
| 2  | 200    |
| 3  | 300    |
n = 2
Output
| getNthHighestSalary(2) |
| ---------------------- |
| 200                    |
'''