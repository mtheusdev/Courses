/* Matheus Henrique dos Santos, https://github.com/mtheusdev  UDESC CCT CS50X - HARVARD */
SELECT movies.title from people
JOIN stars ON people.id = stars.person_id
JOIN movies ON stars.movie_id = movies.id
JOIN ratings on movies.id = ratings.movie_id
WHERE people.name = "Chadwick Boseman"
ORDER BY rating DESC
LIMIT 5;
