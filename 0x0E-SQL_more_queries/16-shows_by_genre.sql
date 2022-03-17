/*File: 16-shows_by_genre.sql
Author: Alex Orland Arévalo Tribaldos
email: <3915@holbertonschool.com>*/

-- Lists all shows and genres linked to the show from the
-- database hbtn_0d_tvshows.
-- Records are ordered by ascending show title and genre name.
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_show_genres
ON tv_shows.id = tv_show_genres.show_id
LEFT JOIN tv_genres
ON tv_genres.id = tv_show_genres.genre_id
ORDER BY tv_shows.title, tv_genres.name ASC;
