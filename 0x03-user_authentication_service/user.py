#!/usr/bin/env python3
"""_summary_
"""


from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()


class User(Base):
    """_summary_

    Args:
        Base (_type_): _description_
    Usage:
        from user import User

        print(User.__tablename__)

        for column in User.__table__.columns:
            print("{}: {}".format(column, column.type))
    """
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False)
    hashed_password = Column(String(250), nullable=False)
    session_id = Column(String(250), nullable=True)
    reset_token = Column(String(250), nullable=True)
