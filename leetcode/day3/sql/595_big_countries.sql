"""
595. Big Countries
https://leetcode.com/problems/big-countries/

Table: World
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| name        | varchar |
| continent   | varchar |
| area        | int     |
| population  | int     |
| gdp         | bigint  |
+-------------+---------+
A country is big if:
- it has an area of at least 3,000,000 km2, or
- it has a population of at least 25,000,000.

Write a solution to find the name, population, and area of the big countries.
"""

-- Solution: Using WHERE with OR condition
SELECT name, population, area
FROM World
WHERE area >= 3000000 OR population >= 25000000;

-- Alternative solution using UNION (less efficient but demonstrates concept)
SELECT name, population, area
FROM World
WHERE area >= 3000000
UNION
SELECT name, population, area
FROM World
WHERE population >= 25000000;