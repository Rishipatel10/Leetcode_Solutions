# Write your MySQL query statement below
with high_salary as(
    select
        *,
        dense_rank() over(partition by departmentId order by salary desc) as rnk
    from Employee
)
select 
    d.name as Department,
    h.name as Employee,
    h.salary as Salary
from high_salary h
join Department d
on h.departmentId = d.id
where rnk = 1