-- Create database 

CREATE database IF NOT EXISTS hbtn_0d_2;

-- create user on database
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';

-- set priviledge for user
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
