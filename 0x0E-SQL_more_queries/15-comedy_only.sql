-- List all Comedy shows
SELECT tv_shows.title
FROM tv_shows
JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
JOIN tv_genres ON tv_genres.id = tv_shows_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY tv_shows.title ASC;
