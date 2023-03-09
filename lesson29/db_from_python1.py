import psycopg2

# connection string
# conn = psycopg2.connect("host=localhost port=5432 dbname=bank user=postgres password=postgres")
# print(conn)
# conn.close()
# print(conn)

# as params
conn = psycopg2.connect(
    host="localhost",
    port=5432,
    database="bank",
    user="postgres",
    password="postgres")
print(conn)
print(conn.closed)
conn.close()
print(conn)
print(conn.closed)

