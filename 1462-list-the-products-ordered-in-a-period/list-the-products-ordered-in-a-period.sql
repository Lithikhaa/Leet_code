# Write your MySQL query statement below



with modu as (select p.product_name as product_name, o.unit as unit,p.product_id as product_id,
month(order_date) as month, year(order_date) as year from Products p
inner join Orders o on p.product_id = o.product_id
where month(order_date) = 2
and year(order_date) = 2020)

-- select product_name,sum(unit) from modu

select product_name,sum(unit) as unit from modu
group by product_name
having unit >= 100



