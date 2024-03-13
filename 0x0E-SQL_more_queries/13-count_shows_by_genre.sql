-- This script lists genres and the number of shows for each genre

SELECT g.genre, COALESCE(COUNT(s.id), 0) AS number_of_shows
FROM genres g
LEFT JOIN shows s ON g.id = s.genre_id
GROUP BY g.genre
ORDER BY number_of_shows DESC;

