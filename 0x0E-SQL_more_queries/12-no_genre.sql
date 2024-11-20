-- List all shows without a genre linked
SELECT tv_shows.title, tv_shows_genres.genre_id
FROM tv_shows
LEFT JOIN tv_shows_genres ON tv_shows.id = tv_shows_genres.show_id
WHERE tv_shows_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC, tv_shows_genres.genre_id ASC;
