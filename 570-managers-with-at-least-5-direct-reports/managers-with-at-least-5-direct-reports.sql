# Write your MySQL query statement below

select e.name from Employee e
join Employee e1 on e.id = e1.managerId
group by e1.managerId
having count(e1.managerId) >= 5;