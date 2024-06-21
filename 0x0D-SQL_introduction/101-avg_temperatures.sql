-- This file orders avg temps of a cities in a database
-- Commands that perform this sql task

SELECT city, AVG(value) AS avg_temp FROM temperatures GROUP BY city ORDER BY -AVG(value);
