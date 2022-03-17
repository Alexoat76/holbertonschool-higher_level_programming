/*File: 2-create_read_user.sql
Author: Alex Orland Arévalo Tribaldos
email: <3915@holbertonschool.com>*/

-- Creates the database hbtn_0d_2 and the user user_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;

-- Creates a user with SELECT privileges only
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
FLUSH PRIVILEGES;
