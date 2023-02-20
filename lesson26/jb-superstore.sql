select * from superstore_data;
select year_birth from superstore_data;
select id, year_birth from superstore_data;
select * from superstore_data where year_birth < 1980;
select count(*) from superstore_data;

select 
	* 
from 
	superstore_data 
where
	year_birth > 1980 and response = 1;

select * from superstore_data 
where mntmeatproducts >= 1000 or mntfishproducts >=1000;

select 
	id, mntmeatproducts,mntfishproducts  
from 
	superstore_data 
where 
	mntmeatproducts + mntfishproducts >= 1000;

select 
	id, mntmeatproducts,mntfishproducts,  
	mntmeatproducts + mntfishproducts as all_products
from 
	superstore_data 
where 
	mntmeatproducts + mntfishproducts >= 1000;

select
	count(id) - count(mntfruits)
from
	superstore_data;

select * from superstore_data
where income is null;

select count(income) from superstore_data;

select max(income) from superstore_data;

select
	min(income),
	max(income),
	avg(income),
	stddev(income)
from
	superstore_data;


-- usage of limit/offset

select
	*
from
	superstore_data
where
	kidhome = 0
order by income 
limit 10
offset 0;


select
	*
from
	superstore_data
where
	kidhome = 0 and income is not null
order by
	income desc
limit 10
offset 0;

select education from superstore_data sd ;
select distinct education from superstore_data sd ;

select distinct education, teenhome from superstore_data;


select
	education,
	count(id) as total_customers,
	max(kidhome) as max_kids,
	max(teenhome) as max_teens,
	max(income) as max_income,
	round(avg(income)) as avg_income
from
	superstore_data
group by
	education
order by avg_income;



select kidhome, count(id)
from superstore_data
group by kidhome;


select marital_status, kidhome, count(id)
from superstore_data
group by kidhome, marital_status
order by marital_status desc, kidhome asc;

-- where / having

select year_birth, round(avg(income)) as avg_income
from superstore_data
where year_birth > 1980
group by year_birth 
having round(avg(income)) > 30000
order by avg_income desc
limit 3
offset 2;

select kidhome+teenhome as total_kids
from superstore_data sd;

select lower(marital_status) from superstore_data sd ;

select lower(marital_status) || ' ' || education 
from superstore_data sd ;

select extract (year from now());

select *, extract (year from now()) - year_birth as age
from superstore_data;











select extract(year from now());











