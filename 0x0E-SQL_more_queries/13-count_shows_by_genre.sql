-- 13-count_shows_by_genre.sql: Lists all genres from the database 'hbtn_0d_tvshows'
-- and displays the number of shows linked to each genre.

SELECT genres.name AS genre, COALESCE(show_count.count, 0) AS number_of_shows
FROM genres
LEFT JOIN (
  SELECT genre_id, COUNT(show_id) AS count
  FROM tv_show_genres
  GROUP BY genre_id
) AS show_count ON genres.id = show_count.genre_id
ORDER BY number_of_shows DESC;

