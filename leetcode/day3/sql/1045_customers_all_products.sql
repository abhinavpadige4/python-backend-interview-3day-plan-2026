"""
1045. Customers Who Bought All Products
https://leetcode.com/problems/customers-who-bought-all-products/

Table: Customer
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| customer_id | int     |
| product_key | int     |
+-------------+---------+
This table may contain duplicate rows. 
In other words, customer_id is not necessarily unique.
(product_key) is a foreign key (reference column) to Product table.

Table: Product
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| product_key | int     |
+-------------+---------+
product_key is the primary key (column with unique values) for this table.

Write a solution to find the customer IDs that bought all the products in the Product table.
"""

-- Solution 1: Using double NOT EXISTS (relational division)
SELECT DISTINCT customer_id
FROM Customer c1
WHERE NOT EXISTS (
    SELECT 1
    FROM Product p
    WHERE NOT EXISTS (
        SELECT 1
        FROM Customer c2
        WHERE c2.customer_id = c1.customer_id
        AND c2.product_key = p.product_key
    )
);

-- Solution 2: Using GROUP BY and HAVING with counts
SELECT customer_id
FROM Customer
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (SELECT COUNT(*) FROM Product);

-- Solution 3: Using LEFT JOIN and IS NULL
SELECT DISTINCT c1.customer_id
FROM Customer c1
WHERE NOT EXISTS (
    SELECT p.product_key
    FROM Product p
    LEFT JOIN Customer c2 ON p.product_key = c2.product_key AND c2.customer_id = c1.customer_id
    WHERE c2.customer_id IS NULL
);