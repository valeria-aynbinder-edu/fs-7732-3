-- we want to transfer 1000000 
-- from Angelina's account to Brad's account



begin;

INSERT INTO transactions 
	(transaction_type, ts, initiated_by) 
values
	('transfer', '09-01-2023 10:00:00', 2);


INSERT INTO transaction_accounts 
	(account_role, transaction_id, account_id) 
values
	('sender', currval(pg_get_serial_sequence('transactions','id')), 2);

INSERT INTO transaction_accounts 
	(account_role, transaction_id, account_id) 
values
	('receiver', currval(pg_get_serial_sequence('transactions','id')), 1);

select * from transactions t ;

-- error
--update accounts set balance = balance - 1000000 where account_id=2;

update accounts set balance = balance - 1000000 where id=2;
update accounts set balance = balance + 1000000 where id=1;

select * from accounts a ;

commit;

rollback;




select * from accounts a join account_owners ao 
on a.id =ao.account_id join customers c 
on c.id=ao.account_id;


begin;


INSERT INTO transactions 
	(transaction_type, ts, initiated_by) 
values
	('transfer', now(), 2);


INSERT INTO transaction_accounts 
	(account_role, transaction_id, account_id) 
values
	('sender', currval(pg_get_serial_sequence('transactions','id')), 2);

INSERT INTO transaction_accounts 
	(account_role, transaction_id, account_id) 
values
	('receiver', currval(pg_get_serial_sequence('transactions','id')), 1);


update accounts set balance = balance - 1000000 where id=1;
update accounts set balance = balance + 1000000 where id=2

commit;
end;
--rollback ;






select
	"name", ao.*
from
	transactions t
join transaction_accounts ta 
on
	t.id = ta.transaction_id
join account_owners ao 
on
	ao.account_id = ta.account_id
join customers c 
on
	c.id = ao.customer_id
where
	t.id = 12;


























