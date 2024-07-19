#!/usr/bin/env python3
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__: str = 'users'

    id: Column = Column(Integer, primary_key=True)
    email: Column = Column(String, non-nullable=True)
    hashed_password: Column = Column(String, non-nullable=True)
    session_id: Column = Column(String, nullable=True)
    reset_token: Column = Column(String, nullable=True)
    
    def __repr__(self) -> str:
        return f'<User(id='{self.id}', email='{self.email}', hashed_password='{self.hashed_password}', session='{self.session}', rest_token='{self.reset_token}>')'
