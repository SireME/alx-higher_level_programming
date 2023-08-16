-- list all records of table
-- Records should be ordered by score
-- The database name will be passed as
-- an argument of the mysql command

SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
