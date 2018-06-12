import datetime

from sqlalchemy.orm import relationship

from sqlalchemy import Column, Integer, String, DateTime, ForeignKey

from .base import Base


class Post(Base):
    __tablename__ = "post"
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    content = Column(String)
    create_at = Column(DateTime, default=datetime.datetime.now)
    update_at = Column(DateTime, default=datetime.datetime.now)
