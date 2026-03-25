from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker,declarative_base
database_url = "sqlite:///database.db"
engine = create_engine(database_url,connect_args={"check_same_thread":False})
Sessionlocal = sessionmaker(bind=engine)
Base = declarative_base()
