from sqlalchemy import create_engine, Column, Table, ForeignKey, MetaData
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import (
    Integer, String, Date, DateTime, Float, Boolean, Text, ARRAY)
from scrapy.utils.project import get_project_settings
from datetime import datetime

Base = declarative_base()

def db_connect():
    """
    Performs database connection using database settings from settings.py.
    Returns sqlalchemy engine instance
    """
    return create_engine(get_project_settings().get("CONNECTION_STRING"))

def create_table(engine):
    Base.metadata.create_all(engine)

# Association Table for Many-to-Many relationship between Quote and Tag
# https://docs.sqlalchemy.org/en/13/orm/basic_relationships.html#many-to-many

class Products(Base):
    __tablename__ = "products"

    id = Column(Integer, primary_key=True)
    crawled_date = Column(DateTime(), default=datetime.now)
    url = Column('url', Text())
    title = Column('title', Text())
    brand = Column('brand', Text())
    item_id = Column('item_id', Integer())
    img = Column('img', Text())
    #size = Column('size', Text())
    price = relationship('Price', backref="products")

class Price(Base):
    __tablename__ = "price"

    id = Column(Integer, primary_key=True)
    crawled_date = Column(DateTime(), default=datetime.now)
    item_id = Column('item_id', Integer(), ForeignKey('products.item_id'))
    price_reg_1 = Column('price_reg_1', Integer())
    price_end_1 = Column('price_end_1', Integer())
    price_reg_2 = Column('price_reg_2', Integer())
    price_end_2 = Column('price_end_2', Integer())
    price_reg_3 = Column('price_reg_3', Integer())
    price_end_3 = Column('price_end_3', Integer())
    price_reg_4 = Column('price_reg_4', Integer())
    price_end_4 = Column('price_end_4', Integer())
    '''size_in_stoke_1 = Column('size_in_stoke_1', Text())
    size_in_stoke_2 = Column('size_in_stoke_2', Text())
    size_in_stoke_3 = Column('size_in_stoke_3', Text())
    size_in_stoke_4 = Column('size_in_stoke_4', Text())'''

