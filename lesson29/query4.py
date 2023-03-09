import psycopg2


def using_fetch_one(cur):
    # The  fetchone() fetches the next row in the result set.
    # It returns a single tuple or None when no more row is available.
    result = ""
    while result is not None:
        result = cur.fetchone()
        print(result)


def using_fetch_many(cur):
    # The  fetchmany(size=cursor.arraysize) fetches the next set of rows specified by the
    # size parameter.
    # The  fetchmany() method returns a list of tuples or an empty list if no more rows available.
    print(cur.arraysize)
    result = cur.fetchmany()
    print(result)


def using_fetch_all(cur):
    pass

def demo_query():
    # connect to the PostgreSQL server
    print('Connecting to the PostgreSQL database...')
    with psycopg2.connect(
            host="localhost",
            port=5432,
            database="bank",
            user="postgres",
            password="postgres") as conn:

        # create a cursor
        with conn.cursor() as cur:

            # execute a statement
            cur.execute('SELECT * FROM customers')

            # result = cur.fetchone()
            # print(result)
            #
            # result = cur.fetchone()
            # print(result)
            #
            # result = cur.fetchone()
            # print(result)
            #
            # result = cur.fetchone()
            # print(result)
            #
            # result = cur.fetchone()
            # print(result)

            #
            # print(cur.rowcount)
            # print(cur.arraysize)
            # # cur.
            # result = cur.fetchmany(2)
            # print(result)

            # using_fetch_one(cur)
            # using_fetch_many(cur)
            # using_fetch_all(cur)

            result = cur.fetchall()
            print(result)

    conn.close()


if __name__ == '__main__':
    demo_query()