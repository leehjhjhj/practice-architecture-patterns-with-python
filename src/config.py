from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager
from decouple import config

user = config('DB_USER')
password = config('DB_PASSWORD')
host = config('DB_HOST')
port = config('DB_PORT')
schema = config('DB_SCHEMA')

def get_mysql_uri():
    return f"mysql+pymysql://{user}:{password}@{host}:{port}/{schema}?charset=utf8mb4"

def get_sqlite_uri():
    return "sqlite:///./sqlite.db"

Base = declarative_base()
DB_URL = get_mysql_uri()
# @contextmanager
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()