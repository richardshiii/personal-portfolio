/* 
585. Investment In 2016
Difficulty: Medium

Table: Insurance
+-------------+-------+
| Column Name | Type  |
+-------------+-------+
| pid         | int   |
| tiv_2015    | float |
| tiv_2016    | float |
| lat         | float |
| lon         | float |
+-------------+-------+
pid is the primary key (column with unique values) for this table.
Each row of this table contains information about one policy where:
pid is the policyholder's policy ID.
tiv_2015 is the total investment value in 2015 and tiv_2016 is the total investment value in 2016.
lat is the latitude of the policy holder's city. It's guaranteed that lat is not NULL.
lon is the longitude of the policy holder's city. It's guaranteed that lon is not NULL.

Write a solution to report the sum of all total investment values in 2016 tiv_2016, for all policyholders who:

have the same tiv_2015 value as one or more other policyholders, and
are not located in the same city as any other policyholder (i.e., the (lat, lon) attribute pairs must be unique).
Round tiv_2016 to two decimal places.
*/

# Solution
select round(sum(tiv_2016), 2) as tiv_2016
from Insurance
where (lat, lon) in 
    (
    -- Select unique lat, lon pairs where count is 1 (i.e., unique cities)
    select lat, lon
    from Insurance
    group by lat, lon
    having count(*) = 1
    )
    and
    tiv_2015 in
    (
    -- Select tiv_2015 values that appear more than once
    select tiv_2015
    from Insurance
    group by tiv_2015
    having count(*) > 1
    );
    
/* Test Case
-- Insurance table
| pid | tiv_2015 | tiv_2016 | lat | lon |
| --- | -------- | -------- | --- | --- |
| 1   | 10       | 5        | 10  | 10  |
| 2   | 20       | 20       | 20  | 20  |
| 3   | 10       | 30       | 20  | 20  |
| 4   | 10       | 40       | 40  | 40  |
Output table
| tiv_2016 |
| -------- |
| 45       |
*/


