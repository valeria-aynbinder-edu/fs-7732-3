create table customers(
	id serial primary key,
	passport_num bigint not null,
	name varchar(128) not null,
	address varchar(256)
);

create table accounts(
	id serial primary key,
	balance float not null default 0,
	max_limit float not null default 0
);

create table account_owners(
	id serial primary key,
	customer_id int not null,
	account_id int not null,
	foreign key (customer_id) references customers(id),
	foreign key (account_id) references accounts(id)
);

create table transactions(
	id serial primary key,
	transaction_type varchar(16) not null,
	ts timestamp not null,
	initiated_by int not null,
	foreign key (initiated_by) references customers(id) on delete cascade
);

create table transaction_accounts(
	id serial primary key,
	-- states the role of the account in transaction
	-- for example, when transfering (sender / receiver)
	-- for withdraw/deposit, can be null
	account_role varchar(16),
	transaction_id int not null,
	account_id int not null,
	foreign key (transaction_id) references transactions(id) on delete cascade,
	foreign key (account_id) references accounts(id) on delete cascade
);



