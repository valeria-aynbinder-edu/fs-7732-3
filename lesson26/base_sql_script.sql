select * from superstore_data;
--select id, income, teenhome from superstore_data;

select  * 
from superstore_data 
where income > 100000;

select id, education, income, marital_status 
from superstore_data
where income > 10000 and kidhome > 1;

select id, education, income, marital_status 
from superstore_data
where income > 50000 and (kidhome > 1 or teenhome > 1);

select count(*) from superstore_data;

select * from superstore_data where teenhome = 2;

select count(id) from superstore_data;

select count(*) from superstore_data where teenhome = 1;

select * from superstore_data where year_birth between 1970 and 1980;

select max(income) from superstore_data;

select min(income) from superstore_data;

select round(avg(income), 2) as avg_income, 
	avg(mntwines) as avg_wines, 
	avg(mntfruits) as avg_fruits,
	min(income) as min_income
from superstore_data;

select income from superstore_data;

select sum(teenhome) from superstore_data sd ;

select id, teenhome + kidhome as total_children  from superstore_data;

select sum(teenhome + kidhome) from superstore_data;

select id from superstore_data sd ;

select * from superstore_data sd where id=837;
select id from superstore_data sd where id=837;

select id from 
	(select * from superstore_data sd where id=837) as new_table;


select * from superstore_data limit 10;

select * from superstore_data limit 5 offset 5;

select * from superstore_data limit 1 offset 6;

select * from superstore_data order by income ;

select * 
from superstore_data 
where income is not null
order by income desc
limit 1;

select * from superstore_data 
where income = 
	(select max(income) from superstore_data);

select distinct(education) from superstore_data;

select education from superstore_data;

select 
	education ,
	count(id),
	round(avg(income), 0) as average, 
	round(min(income), 0) as minimum, 
	round(max(income), 0) as maximum
from superstore_data
group by education;

select 
	education ,
	marital_status,
	count(id),
	round(avg(income), 0) as average, 
	round(min(income), 0) as minimum, 
	round(max(income), 0) as maximum
from superstore_data
group by education, marital_status
order by education desc, marital_status;



select 
	education ,
	count(id),
	round(avg(income), 0) as average, 
	round(min(income), 0) as minimum, 
	round(max(income), 0) as maximum,
	avg(kidhome)
from superstore_data
where kidhome = 0
group by education;


select 
	education ,
	count(id),
	round(avg(income), 0) as average, 
	round(min(income), 0) as minimum, 
	round(max(income), 0) as maximum,
	avg(kidhome) as avg_kids
from superstore_data
group by education
having avg(kidhome) = 0;

select 
	education ,
	count(id),
	round(avg(income), 0) as average, 
	round(min(income), 0) as minimum, 
	round(max(income), 0) as maximum,
	avg(kidhome)
from superstore_data
where education != 'Basic'
group by education;


select 
	education ,
	count(id),
	round(avg(income), 0) as average, 
	round(min(income), 0) as minimum, 
	round(max(income), 0) as maximum,
	avg(kidhome) as avg_kids
from superstore_data
group by education
having education != 'Basic';


select * from imdb_top
where lower(movie_name) like '%king%';







