from sqlalchemy import Column, String, Boolean,ForeignKey
from .database import Base
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.orm import relationship


class Comment(Base):
    __tablename__ = "comments"
    id = Column(String,primary_key=True, nullable=False, unique=True)
    comment = Column(String,nullable=False,unique=False)
    hash = Column(String,nullable=False, unique=True)
    post_id =  Column(String, ForeignKey("posts.hash", ondelete="CASCADE"), nullable=False)
    user_id = Column(String,ForeignKey("users.hash", ondelete="CASCADE"), nullable=False)
    post = relationship("Post")
    user = relationship("User")

class Like(Base):
    __tablename__ = "likes"
    id = Column(String,primary_key=True, nullable=False, unique=True)
    hash = Column(String,nullable=False, unique=True)
    post_id =  Column(String, ForeignKey("posts.hash", ondelete="CASCADE"), nullable=False)
    user_id = Column(String,ForeignKey("users.hash", ondelete="CASCADE"), nullable=False)
    post = relationship("Post")
    user = relationship("User")

class Post(Base):
    __tablename__ = "posts"
    id = Column(String,primary_key=True, nullable=False, unique=True)
    user_id = Column(String, ForeignKey("users.hash", ondelete="CASCADE"), nullable=False)
    content = Column(String,nullable=True, unique=False)
    hash = Column(String,nullable=False, unique=True)
    created_at = Column(TIMESTAMP(timezone=True),
                        nullable=False, server_default=text('now()'))
    published = Column(Boolean, server_default='TRUE', nullable=False)
    user = relationship("User")


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
