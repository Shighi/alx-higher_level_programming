-- List all shows by their rating sum in descending order
SELECT tv_shows.title, SUM(tv_shows_ratings.rating) AS rating
FROM tv_shows
JOIN tv_shows_ratings ON tv_shows.id = tv_shows_ratings.show_id
GROUP BY tv_shows.id, tv_shows.title
ORDER BY rating DESC;
