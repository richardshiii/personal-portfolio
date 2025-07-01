'''
1873. Calculate Special Bonus

Table: Employees
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| employee_id | int     |
| name        | varchar |
| salary      | int     |
+-------------+---------+
employee_id is the primary key (column with unique values) for this table.
Each row of this table indicates the employee ID, employee name, and salary.
 
Write a solution to calculate the bonus of each employee. 
The bonus of an employee is 100% of their salary if the ID of the employee is an odd number 
and the employee's name does not start with the character 'M'. The bonus of an employee is 0 otherwise.

Return the result table ordered by employee_id.
'''

# Solution
import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    # Since the bonus is 100% of the salary for odd employee IDs and names not starting with 'M', 
    # we can set the salary to 0 for even employee IDs or names starting with 'M'.
    # and change the column name to 'bonus'.
    employees.loc[(employees["employee_id"]%2 == 0) | (employees["name"].str[0] == "M"), "salary"] = 0
    return employees[["employee_id", "salary"]].rename(columns = {"salary":"bonus"}).sort_values(by = "employee_id")

'''
Test Case
| employee_id | name    | salary |
| ----------- | ------- | ------ |
| 2           | Meir    | 3000   |
| 3           | Michael | 3800   |
| 7           | Addilyn | 7400   |
| 8           | Juan    | 6100   |
| 9           | Kannon  | 7700   |
Output
| employee_id | bonus |
| ----------- | ----- |
| 2           | 0     |
| 3           | 0     |
| 7           | 7400  |
| 8           | 0     |
| 9           | 7700  |
'''