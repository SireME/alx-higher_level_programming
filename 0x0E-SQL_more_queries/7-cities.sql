-- create database hbtn_0d_usa

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;

-- select existent database
USE hbtn_0d_usa;

-- create table if it does not exists
CREATE TABLE IF NOT EXISTS cities(
	id INT UNIQUE AUTO_INCREMENT NOT NULL PRIMARY KEY,
	state_id INT NOT NULL,
	name VARCHAR(256),
	FOREIGN KEY (state_id) REFERENCES states(id)
	)
