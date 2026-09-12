"""
607. Sales Person
https://leetcode.com/problems/sales-person/

Table: SalesPerson
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| sales_id        | int     |
| name            | varchar |
| salary          | int     |
| commission_rate | int     |
| hire_date       | date    |
+-----------------+---------+
sales_id is the primary key (column with unique values) for this table.

Table: Company
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+
com_id is the primary key (column with unique values) for this table.

Table: Orders
+------------+---------+
| Column Name| Type    |
+------------+---------+
| order_id   | int     |
| date       | date    |
| com_id     | int     |
| sales_id   | int     |
| amount     | int     |
+------------+---------+

Write a solution to find the names of all the salespersons who did not have 
any orders related to the company with the name "RED".
"""

-- Solution 1: Using NOT IN with subquery
SELECT name
FROM SalesPerson
WHERE sales_id NOT IN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
);

-- Solution 2: Using LEFT JOIN and IS NULL
SELECT sp.name
FROM SalesPerson sp
LEFT JOIN (
    SELECT o.sales_id
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE c.name = 'RED'
) AS red_orders ON sp.sales_id = red_orders.sales_id
WHERE red_orders.sales_id IS NULL;

-- Solution 3: Using NOT EXISTS
SELECT sp.name
FROM SalesPerson sp
WHERE NOT EXISTS (
    SELECT 1
    FROM Orders o
    JOIN Company c ON o.com_id = c.com_id
    WHERE o.sales_id = sp.sales_id AND c.name = 'RED'
);