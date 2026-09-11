import os
import psycopg

dsn = os.environ["PSYCOPG_DSN"]

with psycopg.connect(dsn) as conn:
    with conn.cursor() as cur:
        cur.execute("SELECT current_database(), current_user")
        print(cur.fetchone())
