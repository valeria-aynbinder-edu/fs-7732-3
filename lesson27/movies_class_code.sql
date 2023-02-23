create database movies;
drop database movies1;



create table movies (
	id serial primary key,
	movie_name varchar(256) not null,
	release_year smallint not null,
	imdb_rating float
);


INSERT INTO movies
(movie_name, release_year, imdb_rating)
VALUES('The Godfather', 1972, 9.2);

select * from movies;


INSERT INTO movies
(movie_name, release_year)
VALUES('The Shawshank Redemption', 1994);

-- CRUD
update movies set imdb_rating = 9.3;

update movies set imdb_rating =9.2
where id=1;

insert into movies (movie_name, release_year)
values ('The Green Mile', 34.5);

delete from movies
where id=4;

create table directors (
	id serial primary key,
	director_name varchar(256) not null,
	origin_country varchar(128)
);

INSERT INTO directors (director_name, origin_country)
VALUES('Francis Ford Coppola', 'Italy');

INSERT INTO directors (director_name)
VALUES('Frank Darabont');

select * from directors d ;

alter table movies add director_id int;
select * from movies m ;

alter table movies
	add constraint fk_director_id
	foreign key (director_id) references directors(id);

select * from directors d ;

select * from movies m ;

update  movies set director_id =2 where id=1;

alter table movies alter column director_id set not null;

INSERT INTO
directors (director_name, origin_country)
VALUES('Quentin Tarantino', 'Israel');


insert into movies
(movie_name , release_year, director_id)
values ('Pulp fiction', 1994, 3);

insert into movies
(movie_name , release_year, director_id)
values ('Django Unchained', 2012, 3);

select * from
movies cross join directors;

select * from movies
join directors on movies.director_id = directors.id;

--select * from movies
--join directors on movies.director_id > directors.id;

select movie_name, release_year, director_name
from movies m
join directors d on m.director_id = d.id;

select movie_name, release_year, director_name
from movies m
left join directors d on m.director_id = d.id;

select movie_name, release_year, director_name
from movies m
right join directors d on m.director_id = d.id;

select movie_name, release_year, director_name
from movies m
full outer join directors d on m.director_id = d.id;

select * from movies m ;


select director_name, count(*)
from movies m
join directors d on m.director_id = d.id
group by director_id, director_name ;



