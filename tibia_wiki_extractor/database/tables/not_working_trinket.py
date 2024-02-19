from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String
from tibia_wiki_extractor.database.connector import generate_database_engine

Base = declarative_base()
engine = generate_database_engine()

class Trinket(Base):
    __tablename__ = 'trinkets'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    attributes = Column(String)
    weight = Column(Float)

Base.metadata.create_all(engine)
