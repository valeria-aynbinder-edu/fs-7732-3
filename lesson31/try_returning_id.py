import psycopg2

conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bank",
    user="postgres",
    password="postgres")


with conn:
    with conn.cursor() as c:
        c.execute("INSERT INTO ACCOUNTS (balance, max_limit) VALUES (4,5) RETURNING id")
        new_id = c.fetchone()