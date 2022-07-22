from sqlalchemy import Column, String, Boolean,ForeignKey
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP

class User(Base):
    __tablename__ = "users"
    id = Column(String, primary_key=True, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)
    hash = Column(String,nullable=False, unique=True)
    name = Column(String, nullable=False)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True),nullable=False, server_default=text('now()'))
    verified = Column(Boolean, server_default='FALSE', nullable=False)
    active = Column(Boolean, server_default='TRUE', nullable=False)
