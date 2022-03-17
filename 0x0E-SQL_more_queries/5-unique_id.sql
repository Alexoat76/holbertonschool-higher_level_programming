/*File: 5-unique_id.sql
Author: Alex Orland Arévalo Tribaldos
email: <3915@holbertonschool.com>*/

-- Creates the table unique_id on your MySQL server.
-- for each row, which is never empty when a value isn't given
CREATE TABLE IF NOT EXISTS unique_id(id INT DEFAULT 1, name VARCHAR(256), UNIQUE(id));
