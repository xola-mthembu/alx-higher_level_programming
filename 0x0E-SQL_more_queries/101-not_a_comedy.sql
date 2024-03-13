-- 101-not_a_comedy.sql: Lists all shows that are not categorized under Comedy.

SELECT title
FROM tv_shows
WHERE id NOT IN (
  SELECT tv_shows.id
  FROM tv_shows
  JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
  JOIN genres ON tv_show_genres.genre_id = genres.id
  WHERE genres.name = 'Comedy'
)
ORDER BY title ASC;

