from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql://{settings.DATABASE_USERNAME}:{settings.DATABASE_PASSWORD}@{settings.DATABASE_HOSTNAME}:{settings.DATABASE_PORT}/{settings.DATABASE_NAME}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# while True:
#     try:
#         # Connect to your postgres DB
#         conn = psycopg2.connect(
#             dbname="fastapi", user="namnguyen")
#         # Open a cursor to perform database operations
#         cur = conn.cursor()
#         print("Connect to DB successlly")
#         break
#     except Exception as error:
#         print("Connect to DB failed")
#         print(error)
#         time.sleep(3)
