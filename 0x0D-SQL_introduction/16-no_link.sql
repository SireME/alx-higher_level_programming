-- list all record of table 
-- dont list entries without values

SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC