/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD */
SELECT avg(rating) FROM ratings
JOIN movies ON ratings.movie_id = movies.id
WHERE year = 2012;
