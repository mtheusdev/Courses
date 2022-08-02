/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD */
SELECT movies.title, ratings.rating FROM movies
JOIN ratings ON ratings.movie_id = movies.id
WHERE year = 2010
ORDER BY 2 DESC, 1;
