'''
178. Rank Scores
Difficulty: Medium

Table: Scores
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| score       | decimal |
+-------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the score of a game. Score is a floating point value with two decimal places.
 
Write a solution to find the rank of the scores. The ranking should be calculated according to the following rules:

The scores should be ranked from the highest to the lowest.
If there is a tie between two scores, both should have the same ranking.
After a tie, the next ranking number should be the next consecutive integer value. 
In other words, there should be no holes between ranks.
Return the result table ordered by score in descending order.
'''

# Solution
import pandas as pd

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Rank the scores in descending order
    # Use dense ranking to avoid gaps in the ranking sequence
    scores["rank"] = scores["score"].rank(method = "dense", ascending = False)
    scores_sorted = scores.sort_values(by = "score", ascending = False)
    return scores_sorted[["score", "rank"]]

'''
Test Case
| id | score |
| -- | ----- |
| 1  | 3.5   |
| 2  | 3.65  |
| 3  | 4     |
| 4  | 3.85  |
| 5  | 4     |
| 6  | 3.65  |
Output
| score | rank |
| ----- | ---- |
| 4     | 1    |
| 4     | 1    |
| 3.85  | 2    |
| 3.65  | 3    |
| 3.65  | 3    |
| 3.5   | 4    |
'''