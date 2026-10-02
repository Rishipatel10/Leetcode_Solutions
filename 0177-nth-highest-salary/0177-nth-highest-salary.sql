CREATE FUNCTION getNthHighestSalary(N INT) RETURNS INT
BEGIN
  RETURN (
      # Write your MySQL query statement below.
        with nth_sal as(
            select 
                *,
                dense_rank() over(order by salary desc) as rnk
            from Employee
        )
        select salary as getNthHighestSalary
        from nth_sal
        where rnk = N
        limit 1
  );
END