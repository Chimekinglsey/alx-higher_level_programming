-- Write a script that creates the database hbtn_0d_2 and the user user_0d_2.
-- user_0d_2 should have only SELECT privilege in the database hbtn_0d_2
-- The user_0d_2 password should be set to user_0d_2_pwd
-- If the database hbtn_0d_2 already exists, your script should not fail
-- If the user user_0d_2 already exists, your script should not fail
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
-- creating user
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
-- removing every privilege for user_0d_2
GRANT USAGE ON *.* TO 'user_0d_2'@'localhost';
-- granting select privileges for user
GRANT SELECT ON `hbtn_0d_2` TO 'user_0d_2'@'localhost';
