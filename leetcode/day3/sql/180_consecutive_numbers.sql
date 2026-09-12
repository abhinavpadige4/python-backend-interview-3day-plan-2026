"""
180. Consecutive Numbers
https://leetcode.com/problems/consecutive-numbers/

Table: Logs
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| num         | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.

Write a solution to find all numbers that appear at least three times consecutively.
Return the result table in any order.
"""

-- Solution 1: Using self-joins
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
JOIN Logs l2 ON l1.id = l2.id - 1 AND l1.num = l2.num
JOIN Logs l3 ON l2.id = l3.id - 1 AND l2.num = l3.num;

-- Solution 2: Using window functions (MySQL 8.0+)
SELECT DISTINCT num AS ConsecutiveNums
FROM (
    SELECT 
        num,
        LAG(num, 1) OVER (ORDER BY id) AS prev_num,
        LAG(num, 2) OVER (ORDER BY id) AS prev_prev_num
    FROM Logs
) AS numbered_logs
WHERE num = prev_num AND num = prev_prev_num;

-- Solution 3: Using GROUP BY with HAVING and self-join approach
SELECT DISTINCT l1.num AS ConsecutiveNums
FROM Logs l1
WHERE EXISTS (
    SELECT 1 FROM Logs l2 WHERE l2.id = l1.id + 1 AND l2.num = l1.num
) AND EXISTS (
    SELECT 1 FROM Logs l3 WHERE l3.id = l1.id + 2 AND l3.num = l1.num
);