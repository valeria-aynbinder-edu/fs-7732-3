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

select min(income), max(income), avg(income), stddev(income)
from superstore_data;