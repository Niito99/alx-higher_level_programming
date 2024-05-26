-- This file orders the top 3 cities from a temp database

-- Sql command that does it

SELECT city, AVG(value) AS avg_temp FROM temperatures WHERE month BETWEEN "7" AND "8" GROUP BY city ORDER BY -AVG(value) LIMIT 3;
