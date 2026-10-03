# Write your MySQL query statement below
select 
    book_id,
    title,
    author,
    genre,
    publication_year,
    total_copies as current_borrowers 
from library_books lb
where total_copies  = (
    select count(*) as cnt
    from borrowing_records br
    where lb.book_id = br.book_id
    and return_date is null
    group by book_id
)
order by current_borrowers desc , title