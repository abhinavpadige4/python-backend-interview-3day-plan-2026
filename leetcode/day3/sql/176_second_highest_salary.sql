"""
176. Second Highest Salary
https://leetcode.com/problems/second-highest-salary/

Table: Employee
+-------------+------+
| Column Name | Type |
+-------------+------+
| id          | int  |
| salary      | int  |
+-------------+------+
id is the primary key (column with unique values) for this table.
Each row of this table contains information about the salary of an employee.

Write a solution to find the second highest salary from the Employee table. 
If there is no second highest salary, return null (return None in Pandas).
"""

-- Solution 1: Using LIMIT and OFFSET
SELECT 
    (SELECT DISTINCT salary 
     FROM Employee 
     ORDER BY salary DESC 
     LIMIT 1 OFFSET 1) AS SecondHighestSalary;

-- Solution 2: Using subquery with MAX
SELECT 
    MAX(salary) AS SecondHighestSalary
FROM Employee
WHERE salary < (SELECT MAX(salary) FROM Employee);

-- Solution 3: Using window functions (MySQL 8.0+)
SELECT 
    CASE 
        WHEN COUNT(*) OVER () >= 2 
        THEN salary 
        ELSE NULL 
    END AS SecondHighestSalary
FROM (
    SELECT DISTINCT salary
    FROM Employee
    ORDER BY salary DESC
    LIMIT 2
) AS top_two_salaries
ORDER BY salary ASC
LIMIT 1;