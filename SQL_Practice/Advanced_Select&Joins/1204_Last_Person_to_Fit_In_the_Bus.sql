/* 
1204. Last Person to Fit in the Bus
Difficulty: Medium

Table: Queue
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| person_id   | int     |
| person_name | varchar |
| weight      | int     |
| turn        | int     |
+-------------+---------+
person_id column contains unique values.
This table has the information about all people waiting for a bus.
The person_id and turn columns will contain all numbers from 1 to n, where n is the number of rows in the table.
turn determines the order of which the people will board the bus, where turn=1 denotes the first person to board and turn=n denotes the last person to board.
weight is the weight of the person in kilograms.
 
There is a queue of people waiting to board a bus. However, the bus has a weight limit of 1000 kilograms, so there may be some people who cannot board.

Write a solution to find the person_name of the last person that can fit on the bus without exceeding the weight limit. 
The test cases are generated such that the first person does not exceed the weight limit.

Note that only one person can board the bus at any given turn.
*/

# Solution
-- Calculate the cumulative weight of people boarding the bus by turn
with CTE as (
    select person_name, sum(weight) over(order by turn) as total_weight
    from Queue
) 
select person_name
from CTE
-- Select the person whose cumulative weight is 
-- less than or equal to 1000 as the last person to board the bus
where total_weight <= 1000
order by total_weight DESC
limit 1;

/* Test Case
-- Queue table
| person_id | person_name | weight | turn |
| --------- | ----------- | ------ | ---- |
| 5         | Alice       | 250    | 1    |
| 4         | Bob         | 175    | 5    |
| 3         | Alex        | 350    | 2    |
| 6         | John Cena   | 400    | 3    |
| 1         | Winston     | 500    | 6    |
| 2         | Marie       | 200    | 4    |
Output table
| person_name |
| ----------- |
| John Cena   | 
*/

