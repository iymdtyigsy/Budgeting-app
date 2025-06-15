from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import IntegrityError
import bcrypt

engine = create_engine('sqlite:///account.db', echo=True)

Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    password = Column(String(256), nullable=False)

    def hashpassword(password):
        salt = bcrypt.gensalt()
        bytes = password.encode('utf-8')
        return bcrypt.hashpw(bytes, salt)

    def checkpassword(password, hash):
        bytes = password.encode('utf-8')
        return bcrypt.checkpw(bytes, hash)
    
