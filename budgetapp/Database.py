from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import IntegrityError
import bcrypt

engine = create_engine('sqlite:///account.db', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    hashedpassword = Column(String(256), nullable=False)

    def hashpassword(self, password):
        salt = bcrypt.gensalt()
        bytes = password.encode('utf-8')
        self.hashedpassword = bcrypt.hashpw(bytes, salt)

    def checkpassword(self, password):
        bytes = password.encode('utf-8')
        return bcrypt.checkpw(bytes, self.hashedpassword)
    
Base.metadata.create_all(engine)

def add_user(username, password):
    session = Session()
    try:
        new_user = User(username = username)
        new_user.hashpassword(password)
        session.add(new_user)
        session.commit
        return True, "registered"
    except IntegrityError:
        session.rollback()
        return False, "Username already exist"
    finally:
        session.close()

def auth_user(username, password):
    session = Session()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user and user.checkpassword(password):
            return True, "Login successfully"
        return False, "Wrong username or password"
    finally:
        session.close()

