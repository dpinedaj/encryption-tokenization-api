from sqlalchemy import create_engine, inspect
from sqlalchemy.orm import sessionmaker
from service.core.handlers.key_handler import KeyHandler
from sqlalchemy import Column, Table, MetaData, Integer, String
kh = KeyHandler()
postgres_string = "postgresql+psycopg2://{}:{}@{}:{}/{}".format(
    kh.database_user, kh.database_password,
    kh.database_host, kh.database_port,
    kh.database_db
)

engine = create_engine(postgres_string)
Session = sessionmaker(bind=engine)
session = Session()


def create_if_not_exist(table_name):
    inspector = inspect(engine)
    if not inspector.has_table(table_name):
        metadata = MetaData(engine)
        Table(table_name, metadata,
            Column('id', Integer, primary_key=True, nullable=False, autoincrement=True), 
            Column('value', String),
            Column('token', String))
        metadata.create_all()