/*File: 0-privileges.sql
Author: Alex Orland Arévalo Tribaldos
email: <3915@holbertonschool.com>*/

-- script | lists all privileges of the MySQL users user_0d_1 and user_0d_2 on your server
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
