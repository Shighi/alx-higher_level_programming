-- List all shows without the genre Comedy
SELECT tv_shows.title
FROM tv_shows
WHERE tv_shows.id NOT IN (
    SELECT DISTINCT tv_shows_genres.show_id
    FROM tv_shows_genres
    JOIN tv_genres ON tv_genres.id = tv_shows_genres.genre_id
    WHERE tv_genres.name = 'Comedy'
)
ORDER BY tv_shows.title ASC;
