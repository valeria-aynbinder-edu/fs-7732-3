import psycopg2


def demo_query():

    with psycopg2.connect(
            host="localhost",
            port=5432,
            database="bank",
            user="postgres",
            password="postgres") as conn:

        # create a cursor
        with conn.cursor() as cur:

            query = """
            select
                c.name as customer_name,
                a.id as account_id,
                a.balance
            from 
                accounts a
            join account_owners ao on
                a.id = ao.account_id
            join customers c on
                c.id = ao.customer_id;
            """

            # execute a statement
            cur.execute(query)
            result = cur.fetchall()
            return result


if __name__ == '__main__':
    res = demo_query()
    print(res)