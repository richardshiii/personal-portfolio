/*
3601. Find Drivers with Improved Fuel Efficiency
Difficulty: Medium
https://leetcode.com/problems/find-drivers-with-improved-fuel-efficiency/description/

Table: drivers
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| driver_id   | int     |
| driver_name | varchar |
+-------------+---------+
driver_id is the unique identifier for this table.
Each row contains information about a driver.

Table: trips
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| trip_id       | int     |
| driver_id     | int     |
| trip_date     | date    |
| distance_km   | decimal |
| fuel_consumed | decimal |
+---------------+---------+
trip_id is the unique identifier for this table.
Each row represents a trip made by a driver, including the distance traveled and fuel consumed for that trip.
Write a solution to find drivers whose fuel efficiency has improved by comparing their 
average fuel efficiency in the first half of the year with the second half of the year.

Calculate fuel efficiency as distance_km / fuel_consumed for each trip
First half: January to June, Second half: July to December
Only include drivers who have trips in both halves of the year
Calculate the efficiency improvement as (second_half_avg - first_half_avg)
Round all results to 2 decimal places
Return the result table ordered by efficiency improvement in descending order, 
then by driver name in ascending order.
*/
# Solution 
-- calculate the fuel efficiency for each driver in each half of the year
with efficiency as (
select driver_id, 
-- use case when to categorize the 1st half and 2nd half of the year
avg(case when month(trip_date) between 1 and 6 then distance_km/fuel_consumed end) as first_half_avg,
avg(case when month(trip_date) between 7 and 12 then distance_km/fuel_consumed end) as second_half_avg
from trips
group by driver_id
)
select d.driver_id, d.driver_name, 
-- round fuel efficiency numbers to 2 decimal places
round(e.first_half_avg, 2) as first_half_avg, 
round(e.second_half_avg, 2) as second_half_avg, 
round(e.second_half_avg - e.first_half_avg, 2) as efficiency_improvement
from drivers d
left join efficiency e
on d.driver_id = e.driver_id
-- include only drivers with trips in both 1st and 2nd half of a year
where e.first_half_avg is not null
and e.second_half_avg is not null
-- include only drivers with improvement in fuel efficiency
and e.second_half_avg - e.first_half_avg > 0
order by efficiency_improvement DESC, driver_name ASC;

/*
Test Case
drivers = 
| driver_id | driver_name   |
| --------- | ------------- |
| 1         | Alice Johnson |
| 2         | Bob Smith     |
| 3         | Carol Davis   |
| 4         | David Wilson  |
| 5         | Emma Brown    |
trips = 
| trip_id | driver_id | trip_date  | distance_km | fuel_consumed |
| ------- | --------- | ---------- | ----------- | ------------- |
| 1       | 1         | 2023-02-15 | 120.5       | 10.2          |
| 2       | 1         | 2023-03-20 | 200         | 16.5          |
| 3       | 1         | 2023-08-10 | 150         | 11            |
| 4       | 1         | 2023-09-25 | 180         | 12.5          |
| 5       | 2         | 2023-01-10 | 100         | 9             |
| 6       | 2         | 2023-04-15 | 250         | 22            |
| 7       | 2         | 2023-10-05 | 200         | 15            |
| 8       | 3         | 2023-03-12 | 80          | 8.5           |
| 9       | 3         | 2023-05-18 | 90          | 9.2           |
| 10      | 4         | 2023-07-22 | 160         | 12.8          |
| 11      | 4         | 2023-11-30 | 140         | 11            |
| 12      | 5         | 2023-02-28 | 110         | 11.5          |
Output
| driver_id | driver_name   | first_half_avg | second_half_avg | efficiency_improvement |
| --------- | ------------- | -------------- | --------------- | ---------------------- |
| 2         | Bob Smith     | 11.24          | 13.33           | 2.1                    |
| 1         | Alice Johnson | 11.97          | 14.02           | 2.05                   |
*/
