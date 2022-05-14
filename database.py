# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker

# SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
# # SQLALCHEMY_DATABASE_URL = "postgresql://user:password@postgresserver/db"

# engine = create_engine(
#     SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
# )
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

from peewee import *


database = MySQLDatabase(
    'bsale_test',
    user='bsale_test',
    password='bsale_test',
    host='mdb-test.c6vunyturrl6.us-west-1.rds.amazonaws.com',
    port=3306
)

class User(Model):
    username = CharField()
    email = CharField()
    

    def __str__(self):
        return self.username
    class Meta:
        database = database
        table_name = 'users'
    

class Product(Model):
    id = IntegerField()
    name = CharField()
    url_image = CharField()
    price = DoubleField()
    discount = DoubleField()
    category = IntegerField()

    def __str__(self):
        return self.id
    class Meta:
        database = database
        table_name = 'product'
    


class Category(Model):
    id = IntegerField()
    name = CharField()

    def __str__(self):
        return self.id
    class Meta:
        database = database
        table_name = 'category' 

