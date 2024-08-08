# Write your MySQL query statement below
select e.name,s.bonus from Employee e
left join Bonus s on  e.empId = s.empId
where s.bonus < 1000 or s.bonus is Null;

