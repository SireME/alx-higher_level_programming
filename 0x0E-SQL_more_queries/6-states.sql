-- create database with name hbtn_0d_usa

CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;


-- select table just created or already existing
USE hbtn_0d_usa;

-- create table states in above database

CREATE TABLE IF NOT EXISTS states(
	id INT UNIQUE AUTO_INCREMENT NOT NULL,
	name VARCHAR(256),
	PRIMARY KEY(id)
	)
