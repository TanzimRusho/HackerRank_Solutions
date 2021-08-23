/*
Practice > SQL > Aggregation > Top Earners
(oracle)
*/
select *
from 
(
    select salary * months, count (*)
    from employee
    group by salary * months
    order by salary * months desc
) 
where rownum = 1;
