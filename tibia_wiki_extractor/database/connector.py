from sqlalchemy import create_engine
from sqlalchemy.engine import URL
# Dev lib
import os
import dotenv

dotenv.load_dotenv()

url = URL.create(
    drivername= "postgresql+psycopg",
    username= os.getenv("db_user"),
    host= os.getenv("db_host"),
    database= "tibiawiki_extractor",
    password= os.getenv("db_pwd"),
    port= "5432"
)

engine = create_engine(url)
