# Write your MySQL query statement below
with high_sal as(
    select 
        *,
        dense_rank() over(order by salary desc) as sal
    from Employee
)
select max(salary) as SecondHighestSalary
from high_sal
where sal = 2