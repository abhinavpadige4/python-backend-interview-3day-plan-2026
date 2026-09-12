"""
626. Exchange Seats
https://leetcode.com/problems/exchange-seats/

Table: Seat
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| student     | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.

Write a solution to swap the seat id of every two consecutive students. 
If the number of students is odd, the id of the last student is not swapped.
"""

-- Solution 1: Using CASE and arithmetic
SELECT 
    CASE
        WHEN id % 2 = 1 AND id != (SELECT COUNT(*) FROM Seat) THEN id + 1
        WHEN id % 2 = 0 THEN id - 1
        ELSE id
    END AS id,
    student
FROM Seat
ORDER BY id;

-- Solution 2: Using LEAD and LAG window functions (MySQL 8.0+)
SELECT 
    COALESCE(
        LAG(id) OVER (ORDER BY id),
        LEAD(id) OVER (ORDER BY id),
        id
    ) AS id,
    student
FROM Seat
ORDER BY id;

-- Solution 3: Using UNION approach
SELECT 
    CASE 
        WHEN id % 2 = 1 THEN id + 1
        ELSE id - 1
    END AS id,
    student
FROM Seat
WHERE id % 2 = 1 AND id < (SELECT COUNT(*) FROM Seat)
UNION ALL
SELECT 
    CASE 
        WHEN id % 2 = 0 THEN id - 1
        ELSE id + 1
    END AS id,
    student
FROM Seat
WHERE id % 2 = 0 AND id > 1
UNION ALL
SELECT id, student
FROM Seat
WHERE id = (SELECT COUNT(*) FROM Seat) AND id % 2 = 1
ORDER BY id;