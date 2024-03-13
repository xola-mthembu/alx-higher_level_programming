-- 100-not_my_genres.sql: Lists all genres not linked to the show Dexter.

SELECT genres.name
FROM genres
LEFT JOIN (SELECT tv_show_genres.genre_id
           FROM tv_shows
           JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
           WHERE tv_shows.title = 'Dexter') AS dexter_genres
ON genres.id = dexter_genres.genre_id
WHERE dexter_genres.genre_id IS NULL
ORDER BY genres.name ASC;

