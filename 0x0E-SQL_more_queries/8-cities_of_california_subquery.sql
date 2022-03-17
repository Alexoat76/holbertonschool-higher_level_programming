/*File: 8-cities_of_california_subquery.sql
Author: Alex Orland Arévalo Tribaldos
email: <3915@holbertonschool.com>*/

-- Lists all cities of CA in the database hbtn_0d_usa.
-- Results are ordered by ascending cities.id.
SELECT id, name FROM cities WHERE state_id = (SELECT id FROM states WHERE name = '(California') ORDER BY id ASC;
