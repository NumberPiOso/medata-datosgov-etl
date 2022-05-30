import os

from sqlalchemy import create_engine

user = os.getenv("POSTGRES_USER")
password = os.getenv("POSTGRES_PASS")
host = os.getenv("POSTGRES_HOST")
db = os.getenv("POSTGRES_DB")
port = os.getenv("POSTGRES_PORT")
engine = create_engine(
    f"postgresql+psycopg2://{user}:{password}@{host}:{port}/{db}"
)
