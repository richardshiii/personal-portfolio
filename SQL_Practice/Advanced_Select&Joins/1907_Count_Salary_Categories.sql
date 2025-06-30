/*
1907. Count Salary Categories
Difficulty: Meduim

Table: Accounts
+-------------+------+
| Column Name | Type |
+-------------+------+
| account_id  | int  |
| income      | int  |
+-------------+------+
account_id is the primary key (column with unique values) for this table.
Each row contains information about the monthly income for one bank account.

Write a solution to calculate the number of bank accounts for each salary category. The salary categories are:

"Low Salary": All the salaries strictly less than $20000.
"Average Salary": All the salaries in the inclusive range [$20000, $50000].
"High Salary": All the salaries strictly greater than $50000.
The result table must contain all three categories. If there are no accounts in a category, return 0.

Return the result table in any order.
*/

# Solution
select "Low Salary" as category,
    count(income) as accounts_count
from Accounts
where income < 20000
union all -- use union all to combine results from different categories
select "Average Salary" as category,
    count(income) as accounts_count
from Accounts
where income between 20000 and 50000
union all -- use union all to combine results from different categories
select "High Salary" as category,
    count(income) as accounts_count
from Accounts
where income > 50000; 

/* Test Case
-- Accounts table
| account_id | income |
| ---------- | ------ |
| 3          | 108939 |
| 2          | 12747  |
| 8          | 87709  |
| 6          | 91796  |
Output table
| category       | accounts_count |
| -------------- | -------------- |
| Low Salary     | 1              |
| Average Salary | 0              |
| High Salary    | 3              |
*/
