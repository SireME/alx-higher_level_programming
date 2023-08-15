-- create table if not exists
-- table should be passed in from the command line
-- NOte: we are not using the `USE` statment
-- because our database is passed in from the CLI

CREATE TABLE IF NOT EXISTS first_table (
	id INT,
	name VARCHAR(256)
)
