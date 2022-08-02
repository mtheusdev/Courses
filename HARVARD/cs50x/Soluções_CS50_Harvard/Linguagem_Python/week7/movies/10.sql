/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD */
SELECT name from people
JOIN directors ON people.id = directors.person_id
JOIN movies ON directors.movie_id = movies.id
JOIN ratings on movies.id = ratings.movie_id
WHERE rating >= 9;
