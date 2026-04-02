# Write your MySQL query statement below

SELECT 
    u.name,
    SUM(COALESCE(r.distance, 0)) AS travelled_distance
FROM Users u
LEFT JOIN Rides r 
    ON u.id = r.user_id
GROUP BY u.name,u.id
ORDER BY travelled_distance DESC, u.name ASC;
