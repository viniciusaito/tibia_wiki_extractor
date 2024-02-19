from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, Float, String
from tibia_wiki_extractor.database.connector import generate_database_engine

Base = declarative_base()
engine = generate_database_engine()

class Quiver(Base):
    __tablename__ = 'quivers'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    level = Column(Integer)
    vocation = Column(String)
    volume = Column(Integer)
    bonus = Column(String)
    protection = Column(String)
    weight = Column(Float)

Base.metadata.create_all(engine)
