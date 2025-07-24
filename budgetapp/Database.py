from sqlalchemy import Column, Integer, String, ForeignKey, Sequence, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import IntegrityError
import bcrypt

engine = create_engine('sqlite:///account.db', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    hashedpassword = Column(String(256), nullable=False)

    """budget = relationship("Budget", back_populates="user")
    catergory = relationship("Catergory", back_populates="user")
    goal = relationship("Goal", back_populates="user")"""

    def hashpassword(self, password):
        salt = bcrypt.gensalt()
        bytes = password.encode()
        self.hashedpassword = bcrypt.hashpw(bytes, salt).decode()

    def checkpassword(self, password):
        bytes = password.encode()
        return bcrypt.checkpw(bytes, self.hashedpassword.encode())

"""class Budget(Base):
    __tablename__ = 'budget'

    id = Column(Integer, Sequence('budget_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    budget_name = Column(String, unique=True, nullable=False)
    budget_amount = Column(Integer, nullable=False)

    user = relationship("User", back_populates="budget")
    catergory = relationship("Catergory", back_populates="budget")
    goal = relationship("Goal", back_populates="budget")

class Catergory(Base):
    __tablename__ = 'catergory'

    id = Column(Integer, Sequence('catergory_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    budget_id = Column(Integer, ForeignKey('budget.id'))
    catergory_name = Column(String, unique=True, nullable=False)
    catergory_amount = Column(Integer, nullable=False)

    user = relationship("User", back_populates="catergory")
    budget = relationship("Budget", back_populates="catergory")
    goal = relationship("Goal", back_populates="catergory")


class Goal(Base):
    __tablename__ = 'goal'

    id = Column(Integer, Sequence('catergory_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    budget_id = Column(Integer, ForeignKey('budget.id'))
    catergory_id = Column(Integer, ForeignKey('catergory.id'))
    goal_name = Column(String, unique=True, nullable=False)
    goal_amount = Column(Integer, nullable=False)

    user = relationship("User", back_populates="goal")
    budget = relationship("Budget", back_populates="goal")
    catergory = relationship("Catergory", back_populates="goal")"""

Base.metadata.create_all(engine)

def add_user(username, password):
    session = Session()
    try:
        new_user = User(username=username)
        new_user.hashpassword(password)
        session.add(new_user)
        session.commit()
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

"""def add_budget(name, amount):
    session = Session()
    try:
        new_budget = Budget(budget_name = name, budget_amount = amount)
        session.add(new_budget)
        session.commit()
        return True, 'added'
    except IntegrityError:
        session.rollback()
        return False, 'budget name already exist'
    finally:
        session.close()

def get_catergories():
    catergory = []


    return catergory



def add_goal(name, amount):
    session = Session()

    try:
        new_goal = Goal(goal_name = name, goal_amount = amount)
        session.add(new_goal)
        session.commit()
        return True, 'added'
    except IntegrityError:
        session.rollback()
        return False, 'goal name already exist'
    finally:
        session.close()"""
