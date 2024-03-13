-- 103-rating_genres.sql: Lists all genres by their total ratings, sorted by the rating.

SELECT genres.name, SUM(tv_show_ratings.rating) AS rating_sum
FROM genres
JOIN tv_show_genres ON genres.id = tv_show_genres.genre_id
JOIN tv_shows ON tv_shows.id = tv_show_genres.show_id
JOIN tv_show_ratings ON tv_shows.id = tv_show_ratings.show_id
GROUP BY genres.name
ORDER BY rating_sum DESC, genres.name ASC;

