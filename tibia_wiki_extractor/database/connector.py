from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker
# Dev lib
import os
import dotenv
dotenv.load_dotenv()

def generate_database_engine():
    url = URL.create(
        drivername= "postgresql+psycopg",
        username= os.getenv("db_user"),
        host= os.getenv("db_host"),
        database= "postgres",
        password= os.getenv("db_pwd"),
        port= "5432"
    )
    return create_engine(url, echo=True)

def generate_database_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()
