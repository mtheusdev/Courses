/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD */
SELECT COUNT(title) FROM movies
JOIN ratings on movies.id = ratings.movie_id
WHERE rating = 10;
