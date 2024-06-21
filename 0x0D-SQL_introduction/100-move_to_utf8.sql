-- This is a script that encodes a database and tables to utf8

-- The commands that does it

USE hbtn_0c_0;
ALTER TABLE first_table
CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
