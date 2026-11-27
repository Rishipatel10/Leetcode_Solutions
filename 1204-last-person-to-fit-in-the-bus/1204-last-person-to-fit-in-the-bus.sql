# Write your MySQL query statement below
with last_fit as(
    select
        *,
        sum(weight) over(order by turn) as total_sum
    from Queue
)

select
    person_name
from last_fit
where total_sum <= 1000
order by turn desc
limit 1