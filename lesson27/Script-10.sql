-- id
-- name
-- year

-- genre
-- avg_rating
-- duration
-- production_name
-- language
-- peg_rating
-- description
-- poster_url


create table movies (
	id serial primary key,
	name varchar(256) not null,
	year smallint not null check (year > 1900),
	genre varchar(64) not null,
	avg_rating float check (avg_rating between 0 and 10),
	language varchar(64) default 'EN'
		
);

INSERT INTO 
	public.movies ("name", "year", genre, avg_rating, "language") 
VALUES('Avatar', 10, 'comedy', 7.8, 'EN'::character varying);


-- actors
-- director
-- awards
-- studios




CREATE TABLE directors (
	id serial primary key,
	name varchar(256) not null,
	birth_date date

);

drop table movies;


create table movies (
	id serial primary key,
	name varchar(256) not null,
	year smallint not null check (year > 1900),
	genre varchar(64) not null,
	avg_rating float check (avg_rating between 0 and 10),
	language varchar(64) default 'EN',
	director_id int not null,
	
	CONSTRAINT fk_director
	FOREIGN KEY(director_id) REFERENCES directors(id) 


);

INSERT INTO public.directors 
("name", birth_date) 
VALUES('James Cameron', '1967-12-12');

INSERT INTO public.directors 
("name", birth_date) 
VALUES('Quentin Tarantino', '1947-10-12');


INSERT INTO 
	public.movies 
	("name", "year", genre, avg_rating, "language", director_id) 
VALUES('Avatar', 2000, 'comedy', 7.8, 'EN'::character varying, 1);

INSERT INTO 
	public.movies 
	("name", "year", genre, avg_rating, "language", director_id) 
VALUES('Titanic', 1996, 'comedy', 8.5, 'EN'::character varying, 1);

INSERT INTO 
	public.movies 
	("name", "year", genre, avg_rating, "language", director_id) 
VALUES('Pulp fuction', 1993, 'comedy', 9.2, 'EN'::character varying, 2);

INSERT INTO 
	public.movies 
	("name", "year", genre, avg_rating, "language", director_id) 
VALUES('Star wars', 1987, 'action', 9.2, 'EN'::character varying, null);


UPDATE public.directors 
SET id=2
WHERE id=1;





