-- This script lists genres and the number of shows for each genre

SELECT genre, COUNT(*) AS number_of_shows
FROM genres
INNER JOIN shows ON genres.id = shows.genre_id
GROUP BY genre
HAVING COUNT(*) > 0
ORDER BY number_of_shows DESC;

