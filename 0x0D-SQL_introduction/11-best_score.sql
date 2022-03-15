/*File: 11-best_score.sql
Author: Alex Orland Arévalo Tribaldos
email: <3915@holbertonschool.com>*/

-- Lists all records in the table second_table with a score >= 10. od the db.
-- Records are ordered by descending score.

SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
