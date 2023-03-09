# https://www.psycopg.org/docs/connection.html
import psycopg2


# Psycopg commits the transaction if no exception occurs within the with block,
# and otherwise it rolls back the transaction.


conn: psycopg2._psycopg.connection = None

with psycopg2.connect(
            host="localhost",
            port=5432,
            database="bank",
            user="postgres",
            password="postgres") as conn:
    with conn.cursor() as cur:
        cur.execute("INSERT INTO transactions...")
        cur.execute("update table accounts set...")
        #...

    # conn.commit()
    # conn.rollback()


conn.close()




