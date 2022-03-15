/*File: 10-top_score.sql
Author: Alex Orland Arévalo Tribaldos
email: <3915@holbertonschool.com>*/

-- lists all records of the table second_table of the database hbtn_0c_0.
-- Records are ordered by descending score.
SELECT score, name FROM second_table ORDER BY score DESC;
