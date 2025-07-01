'''
1050. Actors and Directors Who Cooperated At Least 3 Times

Table: ActorDirector
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| actor_id    | int     |
| director_id | int     |
| timestamp   | int     |
+-------------+---------+
timestamp is the primary key (column with unique values) for this table.
 
Write a solution to find all the pairs (actor_id, director_id) where the actor has cooperated with the director at least three times.

Return the result table in any order.
'''

# Solution
import pandas as pd

def actors_and_directors(actor_director: pd.DataFrame) -> pd.DataFrame:
    # Group by actor_id and director_id, counting the number of occurrences 
    group_by = actor_director.groupby(["actor_id", "director_id"]).agg(
        count = ("director_id", "count")
    ).reset_index()
    # Filter the groups where the count is at least 3 
    return group_by[group_by["count"] >= 3][["actor_id", "director_id"]]

'''
Test Case
| actor_id | director_id | timestamp |
| -------- | ----------- | --------- |
| 1        | 1           | 0         |
| 1        | 1           | 1         |
| 1        | 1           | 2         |
| 1        | 2           | 3         |
| 1        | 2           | 4         |
| 2        | 1           | 5         |
| 2        | 1           | 6         |
Output
| actor_id | director_id |
| -------- | ----------- |
| 1        | 1           |
'''