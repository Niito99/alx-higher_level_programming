-- lists the number of records with same score in a table

-- The command that does that

SELECT score, COUNT(score) AS number FROM second_table GROUP BY score ORDER BY number DESC;
