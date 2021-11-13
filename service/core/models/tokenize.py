from typing import List, Tuple, Union, Any
from sqlalchemy import Column, Integer, String
from service.core.handlers.db_session import create_if_not_exist, session
from sqlalchemy.ext.declarative import declarative_base, declared_attr
from sqlalchemy.orm.exc import NoResultFound
from pydantic import BaseModel
from service.core.libs.constants import Constants as cts

Base = declarative_base()


class DynamicName(object):
    @declared_attr
    def __tablename__(cls):
        return cls.__name__.lower()


def Tokenize(table_name: str):
    create_if_not_exist(table_name)

    class TokenizeTable(DynamicName, Base):
        __tablename__ = table_name
        __table_args__ = {'extend_existing': True}
        id = Column(Integer, primary_key=True, autoincrement=True)
        value = Column(String)
        token = Column(String)
    
        @classmethod
        def lookup_value(cls, key_name: str, value: str) -> Tuple[str, str]:
            assert key_name in cts.TOKENIZE_KEYS.value\
                , f"Key_name: {key_name} is not allowed, options: {cts.TOKENIZE_KEYS.value}"
            query = """
                SELECT value, token
                FROM %s
                WHERE %s = '%s'
            """ % (cls.__tablename__, key_name, value)

            try:
                return session.execute(query).fetchone()
            except NoResultFound:
                return ()


    return TokenizeTable


class TokenizeInput(BaseModel):
    value: Any
    table_name: str

class TokenizeOutput(BaseModel):
    value: Any