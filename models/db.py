from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Replace the values within the quotes with your own MySQL server details
db_user = 'root'
db_password = ''
db_host = 'localhost'
db_port = '3306'
db_name = 'chatgpt'

# Create the connection string
SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{db_user}:{db_password}@{db_host}:{db_port}/{db_name}'


engine = create_engine(
    SQLALCHEMY_DATABASE_URL,echo=True,
)



SessionLocal = sessionmaker(autocommit=False, autoflush=True, bind=engine)

Base = declarative_base()
