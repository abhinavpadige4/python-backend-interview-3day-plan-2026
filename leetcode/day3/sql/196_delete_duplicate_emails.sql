"""
196. Delete Duplicate Emails
https://leetcode.com/problems/delete-duplicate-emails/

Table: Person
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key (column with unique values) for this table.

Write a solution to delete all duplicate emails, keeping only one unique email with the smallest id.
"""

-- Solution: Using DELETE with subquery
DELETE FROM Person
WHERE id NOT IN (
    SELECT * FROM (
        SELECT MIN(id)
        FROM Person
        GROUP BY email
    ) AS min_ids
);

-- Alternative solution using self-join (MySQL)
DELETE p1 FROM Person p1
INNER JOIN Person p2 
WHERE p1.email = p2.email 
AND p1.id > p2.id;