from sqlalchemy.ext.declarative import declarative_base

from sqlalchemy import create_engine

eng = create_engine('postgresql://test:hello@localhost/myblog0')
Base = declarative_base()
Base.metadata.bind = eng
