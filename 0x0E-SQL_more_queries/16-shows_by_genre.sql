-- List all shows and their linked genres, with NULL for no genres
SELECT tv_shows.title, tv_genres.name
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
LEFT JOIN tv_genres ON tv_genres.id = tv_shows_genres.genre_id
ORDER BY tv_shows.title ASC, tv_genres.name ASC;
