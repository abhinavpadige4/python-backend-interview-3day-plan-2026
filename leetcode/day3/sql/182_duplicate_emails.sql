"""
182. Duplicate Emails
https://leetcode.com/problems/duplicate-emails/

Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.

Write a solution to report all the duplicate emails. 
Note that it's guaranteed that the table contains at least one row.
"""

-- Solution 1: Using GROUP BY and HAVING
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1;

-- Solution 2: Using self-join
SELECT DISTINCT p1.email
FROM Person p1
JOIN Person p2 ON p1.email = p2.email AND p1.id <> p2.id;

-- Solution 3: Using window functions (MySQL 8.0+)
SELECT email
FROM (
    SELECT 
        email,
        COUNT(*) OVER (PARTITION BY email) AS email_count
    FROM Person
) AS counted_emails
WHERE email_count > 1;