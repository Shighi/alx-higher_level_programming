-- List all genres by their rating sum in descending order
SELECT tv_genres.name, SUM(tv_shows_ratings.rating) AS rating
FROM tv_genres
JOIN tv_shows_genres ON tv_genres.id = tv_shows_genres.genre_id
JOIN tv_shows_ratings ON tv_shows_genres.show_id = tv_shows_ratings.show_id
GROUP BY tv_genres.id, tv_genres.name
ORDER BY rating DESC;
