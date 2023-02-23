select movies.name, directors.name from movies 
join directors on movies.director_id = directors.id;



select m."name" , m."year" , d.* 
from movies m left outer join directors d 
on m.director_id = d.id;


select  d.* ,m."name" , m."year" 
from directors d right join movies m 
on m.director_id = d.id;

select  d.* ,m."name" , m."year" 
from directors d full outer join movies m 
on m.director_id = d.id;


