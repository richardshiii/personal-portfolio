'''
1527. Patients With A Condition

Table: Patients

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| patient_id   | int     |
| patient_name | varchar |
| conditions   | varchar |
+--------------+---------+
patient_id is the primary key (column with unique values) for this table.
'conditions' contains 0 or more code separated by spaces. 
This table contains information of the patients in the hospital.

Write a solution to find the patient_id, patient_name, and conditions of the patients who have Type I Diabetes. 
Type I Diabetes always starts with DIAB1 prefix.

Return the result table in any order.
'''

# Solution
import pandas as pd

def find_patients(patients: pd.DataFrame) -> pd.DataFrame:
    diabetes = patients[patients["conditions"].str.contains(r"(^|\s)DIAB1\d*($|\s)")]
    return diabetes

'''
Test Case
| patient_id | patient_name | conditions   |
| ---------- | ------------ | ------------ |
| 1          | Daniel       | YFEV COUGH   |
| 2          | Alice        |              |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
| 5          | Alain        | DIAB201      |
Output
| patient_id | patient_name | conditions   |
| ---------- | ------------ | ------------ |
| 3          | Bob          | DIAB100 MYOP |
| 4          | George       | ACNE DIAB100 |
'''