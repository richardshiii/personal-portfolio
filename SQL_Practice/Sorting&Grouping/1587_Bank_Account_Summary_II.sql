/*
1587. Bank Account Summary II
Difficulty: Easy
https://leetcode.com/problems/bank-account-summary-ii/description/

Table: Users
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| account      | int     |
| name         | varchar |
+--------------+---------+
account is the primary key (column with unique values) for this table.
Each row of this table contains the account number of each user in the bank.
There will be no two users having the same name in the table.
 
Table: Transactions
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trans_id      | int     |
| account       | int     |
| amount        | int     |
| transacted_on | date    |
+---------------+---------+
trans_id is the primary key (column with unique values) for this table.
Each row of this table contains all changes made to all accounts.
amount is positive if the user received money and negative if they transferred money.
All accounts start with a balance of 0.

Write a solution to report the name and balance of users with a balance higher than 10000. 
The balance of an account is equal to the sum of the amounts of all transactions involving that account.

Return the result table in any order.
*/
# solution
select u.name, 
    sum(t.amount) as balance
from Users u
-- us right join since we want to match every transaction with each account
right join Transactions t on u.account = t.account
-- create groups by account
group by t.account
-- filter account group based on given condition 
having sum(t.amount) > 10000;

/*
Test Case
Users = 
| account | name    |
| ------- | ------- |
| 900001  | Alice   |
| 900002  | Bob     |
| 900003  | Charlie |
Transactions = 
| trans_id | account | amount | transacted_on |
| -------- | ------- | ------ | ------------- |
| 1        | 900001  | 7000   | 2020-08-01    |
| 2        | 900001  | 7000   | 2020-09-01    |
| 3        | 900001  | -3000  | 2020-09-02    |
| 4        | 900002  | 1000   | 2020-09-12    |
| 5        | 900003  | 6000   | 2020-08-07    |
| 6        | 900003  | 6000   | 2020-09-07    |
| 7        | 900003  | -4000  | 2020-09-11    |
Output
| NAME  | BALANCE |
| ----- | ------- |
| Alice | 11000   |
*/
