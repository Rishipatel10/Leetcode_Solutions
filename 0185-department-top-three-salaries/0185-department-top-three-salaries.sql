# Write your MySQL query statement below
with top_sal as(
    select 
        *,
        dense_rank() over(partition by departmentId order by salary desc) as rnk
    from Employee
)
select
    d.name as Department,
    t.name as Employee,
    t.salary
from top_sal t
join Department d
on t.departmentId = d.id
where rnk <= 3