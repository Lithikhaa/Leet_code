# Write your MySQL query statement below

select * from Cinema
WHERE mod(id,2) = 1 and description !=  'boring'
ORDER BY rating DESC;