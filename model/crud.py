### crud.py ###
from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from config import DATABASE_URI

engine = create_engine(DATABASE_URI)

# whenever we wish to interact with the database, we import Session and make a new s to work with
session = sessionmaker(bind=engine)
# s = Session()
# ... 
# s.close()

base = declarative_base()
