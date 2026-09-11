import os
from sqlalchemy import create_engine, text

engine = create_engine(os.environ["DATABASE_URL"])

with engine.connect() as conn:
    print(conn.execute(text("SELECT current_database()")).scalar_one())
