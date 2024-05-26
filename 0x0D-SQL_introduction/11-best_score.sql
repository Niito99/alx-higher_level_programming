-- This file contains sql that list all records in  the second_table of a database

-- This is the command that does that

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY -score;
