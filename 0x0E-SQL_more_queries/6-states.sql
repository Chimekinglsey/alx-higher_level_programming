-- script that creates the database hbtn_0d_usa
-- id INT auto generated
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states(id INT AUTO_INCREMENT PRIMARY KEY
UNIQUE NOT NULL, name VARCHAR(256) NOT NULL);
