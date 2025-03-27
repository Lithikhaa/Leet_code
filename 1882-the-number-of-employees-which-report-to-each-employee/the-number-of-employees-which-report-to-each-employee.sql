select a.employee_id , a.name , count(*) as reports_count , ROUND(avg(b.age),0) as average_age
from employees a join employees b on a.employee_id = b.reports_to
group by a.employee_id , a.name
order by a.employee_id;