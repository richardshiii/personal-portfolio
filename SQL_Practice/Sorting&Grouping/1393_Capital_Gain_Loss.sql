/*
1393. Capital Gain/Loss
Difficulty: Medium
https://leetcode.com/problems/capital-gainloss/description/

Table: Stocks
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| stock_name    | varchar |
| operation     | enum    |
| operation_day | int     |
| price         | int     |
+---------------+---------+
(stock_name, operation_day) is the primary key (combination of columns with unique values) for this table.
The operation column is an ENUM (category) of type ('Sell', 'Buy')
Each row of this table indicates that the stock which has stock_name had an operation on the day operation_day with the price.
It is guaranteed that each 'Sell' operation for a stock has a corresponding 'Buy' operation in a previous day. 
It is also guaranteed that each 'Buy' operation for a stock has a corresponding 'Sell' operation in an upcoming day.
 
Write a solution to report the Capital gain/loss for each stock.

The Capital gain/loss of a stock is the total gain or loss after buying and selling the stock one or many times.

Return the result table in any order.
*/
# Solution
select stock_name, 
-- use case when to identify capital gain and loss
-- sum up capital change by stock 
    sum(case 
        when operation = "Buy" then -price
        when operation = "Sell" then price 
    end) as capital_gain_loss
from Stocks
group by stock_name;

/*
Test Case
Stocks = 
| stock_name   | operation | operation_day | price |
| ------------ | --------- | ------------- | ----- |
| Leetcode     | Buy       | 1             | 1000  |
| Corona Masks | Buy       | 2             | 10    |
| Leetcode     | Sell      | 5             | 9000  |
| Handbags     | Buy       | 17            | 30000 |
| Corona Masks | Sell      | 3             | 1010  |
| Corona Masks | Buy       | 4             | 1000  |
| Corona Masks | Sell      | 5             | 500   |
| Corona Masks | Buy       | 6             | 1000  |
| Handbags     | Sell      | 29            | 7000  |
| Corona Masks | Sell      | 10            | 10000 |
Output
| stock_name   | capital_gain_loss |
| ------------ | ----------------- |
| Leetcode     | 8000              |
| Corona Masks | 9500              |
| Handbags     | -23000            |
*/