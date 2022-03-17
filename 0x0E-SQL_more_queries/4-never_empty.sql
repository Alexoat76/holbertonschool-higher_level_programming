/*File: 4-never_empty.sql
Author: Alex Orland Arévalo Tribaldos
email: <3915@holbertonschool.com>*/

-- Creates the table id_not_null on your MySQL server.
-- column that is never empty when given a NULL value
CREATE TABLE IF NOT EXISTS id_not_null(id INT DEFAULT 1, name VARCHAR(256) NOT NULL);
