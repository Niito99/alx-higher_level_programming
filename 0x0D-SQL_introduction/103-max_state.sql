-- This file contains sql that retrieves temperature of each state
-- The command that does that
SELECT state, MAX(value) AS max_temp FROM temperatures GROUP BY state ORDER BY state ASC;
