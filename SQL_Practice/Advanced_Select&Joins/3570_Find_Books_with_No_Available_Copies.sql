/*
3570. Find Books with No Available Copies
Difficulty: Easy
https://leetcode.com/problems/find-books-with-no-available-copies/description/

Table: library_books
+------------------+---------+
| Column Name      | Type    |
+------------------+---------+
| book_id          | int     |
| title            | varchar |
| author           | varchar |
| genre            | varchar |
| publication_year | int     |
| total_copies     | int     |
+------------------+---------+
book_id is the unique identifier for this table.
Each row contains information about a book in the library, 
including the total number of copies owned by the library.

Table: borrowing_records
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| record_id     | int     |
| book_id       | int     |
| borrower_name | varchar |
| borrow_date   | date    |
| return_date   | date    |
+---------------+---------+
record_id is the unique identifier for this table.
Each row represents a borrowing transaction and return_date is NULL if the book is currently borrowed and hasn't been returned yet.
Write a solution to find all books that are currently borrowed (not returned) and have zero copies available in the library.

A book is considered currently borrowed if there exists a borrowing record with a NULL return_date
Return the result table ordered by current borrowers in descending order, then by book title in ascending order.
*/
# Solution 
-- create CTE to find count of each book title currently borrowed and not returned
-- return_date is NULL
with CTE as (
    select book_id, count(*) as borrowed
    from borrowing_records
    where return_date is NULL
    group by book_id
)
select c.book_id, l.title, l.author, l.genre, l.publication_year, 
l.total_copies as current_borrowers
from CTE c
join library_books l on c.book_id = l.book_id
-- have zero copies available
-- total_copies = count of books currently borrowed but not returned
and l.total_copies = c.borrowed
order by l.total_copies desc, l.title asc;

/*
Test Case
library_books = 
| book_id | title                  | author        | genre     | publication_year | total_copies |
| ------- | ---------------------- | ------------- | --------- | ---------------- | ------------ |
| 1       | The Great Gatsby       | F. Scott      | Fiction   | 1925             | 3            |
| 2       | To Kill a Mockingbird  | Harper Lee    | Fiction   | 1960             | 3            |
| 3       | 1984                   | George Orwell | Dystopian | 1949             | 1            |
| 4       | Pride and Prejudice    | Jane Austen   | Romance   | 1813             | 2            |
| 5       | The Catcher in the Rye | J.D. Salinger | Fiction   | 1951             | 1            |
| 6       | Brave New World        | Aldous Huxley | Dystopian | 1932             | 4            |
borrowing_records = 
| record_id | book_id | borrower_name | borrow_date | return_date |
| --------- | ------- | ------------- | ----------- | ----------- |
| 1         | 1       | Alice Smith   | 2024-01-15  | null        |
| 2         | 1       | Bob Johnson   | 2024-01-20  | null        |
| 3         | 2       | Carol White   | 2024-01-10  | 2024-01-25  |
| 4         | 3       | David Brown   | 2024-02-01  | null        |
| 5         | 4       | Emma Wilson   | 2024-01-05  | null        |
| 6         | 5       | Frank Davis   | 2024-01-18  | 2024-02-10  |
| 7         | 1       | Grace Miller  | 2024-02-05  | null        |
| 8         | 6       | Henry Taylor  | 2024-01-12  | null        |
| 9         | 2       | Ivan Clark    | 2024-02-12  | null        |
| 10        | 2       | Jane Adams    | 2024-02-15  | null        |
Output
| book_id | title            | author        | genre     | publication_year | current_borrowers |
| ------- | ---------------- | ------------- | --------- | ---------------- | ----------------- |
| 1       | The Great Gatsby | F. Scott      | Fiction   | 1925             | 3                 |
| 3       | "1984"           | George Orwell | Dystopian | 1949             | 1                 |
*/
