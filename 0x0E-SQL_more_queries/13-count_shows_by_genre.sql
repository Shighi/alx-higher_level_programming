-- List all genres with the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(tv_shows_genres.show_id) AS number_of_shows
FROM tv_genres
JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id
GROUP BY tv_genres.id, tv_genres.name
HAVING number_of_shows > 0
ORDER BY number_of_shows DESC;
