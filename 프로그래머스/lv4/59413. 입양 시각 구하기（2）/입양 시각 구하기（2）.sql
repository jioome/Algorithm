SET @HOUR = -1;
select (@HOUR := @HOUR+1) AS HOUR,
    (select count(*)
    from animal_outs
    where hour(datetime) = @hour) as count
from animal_outs
where @HOUR < 23
order by HOUR;