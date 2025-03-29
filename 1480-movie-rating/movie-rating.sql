# Write your MySQL query statement below
WITH user_cte AS (
    SELECT u.name 
    FROM Users u
    JOIN MovieRating m ON u.user_id = m.user_id
    GROUP BY u.name
    ORDER BY COUNT(m.user_id) DESC, u.name ASC
    LIMIT 1
),
movie_cte AS (
    SELECT u.title 
    FROM Movies u
    JOIN MovieRating m ON u.movie_id = m.movie_id  
    WHERE m.created_at BETWEEN '2020-02-01' AND '2020-02-29'  
    GROUP BY u.movie_id, u.title
    ORDER BY AVG(m.rating) DESC, u.title ASC
    LIMIT 1
)
SELECT name AS results FROM user_cte
UNION ALL
SELECT title AS results FROM movie_cte;
