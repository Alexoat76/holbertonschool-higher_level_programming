/*File: 14-my_genres.sql
Author: Alex Orland Arévalo Tribaldos
email: <3915@holbertonschool.com>*/

-- Lists all genres of the show Dexter in the database hbtn_0d_tvshows.
-- Records are ordered by ascending genre name.
SELECT a.name
FROM tv_genres a
INNER JOIN tv_show_genres b
ON a.id = b.genre_id
INNER JOIN tv_shows c
ON c.id = b.show_id
WHERE c.title = 'Dexter'
ORDER BY a.name ASC;
