INSERT INTO 
	customers (passport_num, "name", address) 
values
	(123456789, 'Brad Pitt', 'California');

INSERT INTO 
	customers (passport_num, "name", address) 
values
	(101010101, 'Angelina Jolie', 'California');


INSERT INTO 
	accounts (max_limit) 
values
	(10000000);

INSERT INTO 
	accounts (balance, max_limit) 
values
	(5000000, 10000000);


INSERT INTO account_owners (customer_id, account_id) 
VALUES(2, 2);

