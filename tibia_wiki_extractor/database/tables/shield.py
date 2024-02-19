from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String
from tibia_wiki_extractor.database.connector import generate_database_engine

Base = declarative_base()
engine = generate_database_engine()

class Shield(Base):
    __tablename__ = 'shields'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)
    vocation = Column(String)
    slots = Column(Integer)
    defense = Column(Integer)
    bonus = Column(String)
    protection = Column(String)
    weight = Column(Float)

Base.metadata.create_all(engine)
