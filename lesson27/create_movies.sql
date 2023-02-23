CREATE TABLE public.directors (
	id serial primary key,
	name varchar(256) not null

);

CREATE TABLE public.movies (
	id serial primary key,
	name varchar(256) not null,
	year int not null,
	director_id int not null,
	CONSTRAINT fk_director
      FOREIGN KEY(director_id)
	  REFERENCES directors(id)

);


insert into directors(name) values ('Frank Darabont');
insert into directors(name) values ('Francis Ford Coppola');
insert into directors(name) values ('Steven Spielberg');
insert into directors(name) values ('Quentin Tarantino');


INSERT INTO movies ("id", "name", "year", director_id) VALUES(1, 'The Godfather', 1972, 2);
INSERT INTO movies ("id", "name", "year", director_id) VALUES(2, 'The Shawshank Redemption', 1994, 1);
insert into movies (id, name, year, director_id) values (3, 'The Green Mile', 1999, 1);
insert into movies (id, name, year, director_id) values (4, 'The Mist', 2007, 1);
insert into movies (id, name, year, director_id) values (5, 'Dracula', 1992, 2);
insert into movies (id, name, year, director_id) values (6, 'Gardens of stone', 1987, 2);
insert into movies (id, name, year, director_id) values (7, 'Pulp fiction', 1994, 4);