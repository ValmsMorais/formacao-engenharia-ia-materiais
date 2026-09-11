import os
import psycopg

dsn = os.environ["DATABASE_URL"]

with psycopg.connect(dsn) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT current_database(), current_user")
        print(cur.fetchone())
