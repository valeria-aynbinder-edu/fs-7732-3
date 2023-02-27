explain select * from jan j where tail_num like '%48%';

create index tail_idx on jan (tail_num);


explain select * from jan j where day_of_month =
15 and day_of_week =3;
create index day_idx on jan (day_of_month);

create index d_idx on jan (day_of_month, day_of_week);

drop index day_idx;
--Seq Scan on jan j  (cost=0.00..17526.83 rows=275006 width=91)
--Index Scan using day_idx on jan j  (cost=0.42..10259.03 rows=275006 width=91)explain select * from jan j where day_of_month =


explain select * from jan j where day_of_month =15;
--Gather  (cost=1000.00..16132.86 rows=20346 width=91)
--  ->  Parallel Seq Scan on jan j  (cost=0.00..13098.26 rows=8478 width=91)


select count(*) from jan;

select * from jan j where distance <200
order by tail_num ;


explain analyze select * from jan j where day_of_month =15;
--Gather  (cost=1000.00..16132.86 rows=20346 width=91) (actual time=1.866..84.029 rows=19669 loops=1)
--  Workers Planned: 2
--  Workers Launched: 2
--  ->  Parallel Seq Scan on jan j  (cost=0.00..13098.26 rows=8478 width=91) (actual time=44.505..69.673 rows=6556 loops=3)
--        Filter: (day_of_month = 15)
--        Rows Removed by Filter: 195892
--Planning Time: 0.157 ms
--Execution Time: 85.280 ms

create index day_idx on jan (day_of_month);




explain analyze select * from jan j where distance >1000
and day_of_month = 15;

create index both_day_and_dist on jan (day_of_month, distance);



