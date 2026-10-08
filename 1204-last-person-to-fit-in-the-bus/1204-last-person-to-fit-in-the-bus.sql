# Write your MySQL query statement below

with high_weight as(
    select 
        *,
        sum(weight) over(order by turn) as rank_sum
    from queue
)
select person_name
from high_weight
where rank_sum <= 1000
order by turn desc
limit 1