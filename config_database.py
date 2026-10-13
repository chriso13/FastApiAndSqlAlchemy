import os

from dotenv import load_dotenv



from sqlalchemy.orm import sessionmaker

from sqlalchemy import create_engine

load_dotenv()

DB_URL = os.getenv("DB_URL")

if not DB_URL:
    raise RuntimeError("DB_URL is not set. Check your .env file.")

engine = create_engine(DB_URL)

Session = sessionmaker(autocommit=False ,autoflush=False, bind=engine)


def get_db():

    db = Session()

    try:
        yield db
    finally:
        db.close()
