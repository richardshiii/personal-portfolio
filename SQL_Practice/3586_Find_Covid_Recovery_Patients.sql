/*
3586. Find COVID Recovery Patients
Difficulty: Medium
https://leetcode.com/problems/find-covid-recovery-patients/description/

Table: patients
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| patient_id  | int     |
| patient_name| varchar |
| age         | int     |
+-------------+---------+
patient_id is the unique identifier for this table.
Each row contains information about a patient.

Table: covid_tests
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| test_id     | int     |
| patient_id  | int     |
| test_date   | date    |
| result      | varchar |
+-------------+---------+
test_id is the unique identifier for this table.
Each row represents a COVID test result. The result can be Positive, Negative, or Inconclusive.
Write a solution to find patients who have recovered from COVID - patients who tested positive but later tested negative.

A patient is considered recovered if they have at least one Positive test followed by at least one Negative test on a later date
Calculate the recovery time in days as the difference between the first positive test and the first negative test after that positive test
Only include patients who have both positive and negative test results
Return the result table ordered by recovery_time in ascending order, then by patient_name in ascending order.
*/
# Solution 
-- find the first positive test date for each patient
with first_positive as (
    select patient_id, min(test_date) as first_positive_date
    from covid_tests
    where result = 'Positive'
    group by patient_id
),
-- find the first negative test date for each patient
-- 1st negative date must be later than the 1st positive date
first_negative as (
select c.patient_id, fp.first_positive_date, min(c.test_date) as first_negative_date
    from covid_tests c
    join first_positive fp
    on c.patient_id = fp.patient_id
    and c.result = "Negative"
    -- ensure negative test date is later then positive test date for each patient
    and c.test_date > fp.first_positive_date
    group by patient_id
)
-- calculate the recovery time 
-- 1st_negative_date - 1st_positive_date after positive test
select fr.patient_id, p.patient_name, p.age, 
datediff(fr.first_negative_date, fr.first_positive_date) as recovery_time
from first_negative fr
join patients p
on fr.patient_id = p.patient_id
order by recovery_time asc, patient_name asc;

/*
Test Case
patients = 
| patient_id | patient_name | age |
| ---------- | ------------ | --- |
| 1          | Alice Smith  | 28  |
| 2          | Bob Johnson  | 35  |
| 3          | Carol Davis  | 42  |
| 4          | David Wilson | 31  |
| 5          | Emma Brown   | 29  |
covid_tests = 
| test_id | patient_id | test_date  | result       |
| ------- | ---------- | ---------- | ------------ |
| 1       | 1          | 2023-01-15 | Positive     |
| 2       | 1          | 2023-01-25 | Negative     |
| 3       | 2          | 2023-02-01 | Positive     |
| 4       | 2          | 2023-02-05 | Inconclusive |
| 5       | 2          | 2023-02-12 | Negative     |
| 6       | 3          | 2023-01-20 | Negative     |
| 7       | 3          | 2023-02-10 | Positive     |
| 8       | 3          | 2023-02-20 | Negative     |
| 9       | 4          | 2023-01-10 | Positive     |
| 10      | 4          | 2023-01-18 | Positive     |
| 11      | 5          | 2023-02-15 | Negative     |
| 12      | 5          | 2023-02-20 | Negative     |
Output
| patient_id | patient_name | age | recovery_time |
| ---------- | ------------ | --- | ------------- |
| 1          | Alice Smith  | 28  | 10            |
| 3          | Carol Davis  | 42  | 10            |
| 2          | Bob Johnson  | 35  | 11            |
*/

