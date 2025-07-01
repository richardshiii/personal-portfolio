'''
1148. Article Views I
Data Filtering

Table: Views
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.

Write a solution to find all the authors that viewed at least one of their own articles.

Return the result table sorted by id in ascending order.
'''

# Solution
import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    # Filter the views DataFrame to find rows where the author_id is equal to the viewer_id
    views_own = views[views["author_id"] == views["viewer_id"]]
    # Get the unique author_id 
    own_unique = views_own["author_id"].unique()
    return pd.DataFrame({"id": own_unique}).sort_values(by = "id")

'''
Test Case
| article_id | author_id | viewer_id | view_date  |
| ---------- | --------- | --------- | ---------- |
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
Output
| id |
| -- |
| 4  |
| 7  |
'''

