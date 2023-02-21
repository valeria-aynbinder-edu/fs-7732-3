insert into superstore_data 
(id, year_birth)
values
(3335, 'abc');

insert into superstore_data 
values
(3335, 2000);



INSERT INTO public.superstore_data 
(id, year_birth, education, marital_status, income, kidhome, teenhome, dt_customer, recency, mntwines, mntfruits, mntmeatproducts, mntfishproducts, mntsweetproducts, mntgoldprods, numdealspurchases, numwebpurchases, numcatalogpurchases, numstorepurchases, numwebvisitsmonth, response, complain) 
VALUES(0, 0, '', '', 0, 0, 0, '', 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0);





select * from superstore_data sd 
where id=3334;



delete from superstore_data
where id=3334 and year_birth =2020;


select * from superstore_data sd 
where id=3334;

update superstore_data 
set year_birth = 1952
where id=3334;


select * from superstore_data sd 
where income is null;

update superstore_data 
set income = -1
where income is null;

select * from superstore_data sd 
where income is null;

update superstore_data 
set income = null, recency = -1
where income = -1;

update superstore_data 
set education = lower(education); 


