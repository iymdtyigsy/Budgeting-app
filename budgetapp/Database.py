from sqlalchemy import Column, Float, Integer, String, ForeignKey, Sequence, UniqueConstraint, create_engine
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

    budget = relationship("Budget", back_populates="user")
    expense = relationship("Expense", back_populates="user")
    goal = relationship("Goal", back_populates="user")

    def hashpassword(self, password):
        salt = bcrypt.gensalt()
        bytes = password.encode()
        self.hashedpassword = bcrypt.hashpw(bytes, salt).decode()

    def checkpassword(self, password):
        bytes = password.encode()
        return bcrypt.checkpw(bytes, self.hashedpassword.encode())

class Budget(Base):
    __tablename__ = 'budget'

    id = Column(Integer, Sequence('budget_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    budget_name = Column(String, nullable=False)
    budget_amount = Column(Float, nullable=False)
    budget_income = Column(Float, nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'budget_name', name='unique_user_budget_name'),
    )

    user = relationship("User", back_populates="budget")

class Expense(Base):
    __tablename__ = 'expense'

    id = Column(Integer, Sequence('expense_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    expense_name = Column(String, nullable=False)
    expense_amount = Column(Float, nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'expense_name', name='unique_user_expense_name'),
    )

    user = relationship("User", back_populates="expense")

class Goal(Base):
    __tablename__ = 'goal'

    id = Column(Integer, Sequence('goal_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    goal_name = Column(String, nullable=False)
    goal_amount = Column(Float, nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'goal_name', name='unique_user_goal_name'),
    )

    user = relationship("User", back_populates="goal")

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

def check_budget(username):
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    if not user:
        return False
    
    try:
        budget_exist = session.query(Budget).filter(Budget.user_id == user.id).first()
        if budget_exist is not None:
            return True
        return False
    finally:
        session.close()

def add_budget(username, name, amount, income):
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    try:
        new_budget = Budget(user_id = user.id, budget_name = name, budget_amount = amount, budget_income = income)
        session.add(new_budget)
        session.commit()
        return True, 'added'
    except IntegrityError:
        session.rollback()
        return False, "Budget name already exist"
    finally:
        session.close()

def add_expenses(username, name, amount):
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    try:
        new_expense = Expense(user_id = user.id, expense_name = name, expense_amount = amount)
        session.add(new_expense)
        session.commit()
        return True, "added"
    except IntegrityError:
        session.rollback()
        return False, "Expense name already exist"
    finally:
        session.close()

def get_expense(username):
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    if not user:
        session.close()
        return []
    
    expenses = session.query(Expense).filter(Expense.user_id == user.id).all()
    session.close()
    return expenses

def add_goal(username, name, amount):
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    try:
        goal = Goal(user_id = user.id, goal_name = name, goal_amount = amount)
        session.add(goal)
        session.commit()
        return True, 'added'
    except IntegrityError:
        session.rollback()
        return False, "Goal name already exist"
    finally:
        session.close()

def get_user_data(username):
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    if not user:
        session.close()
        return None
    
    user_data = {
        "id": user.id,
        "username": user.username,
        "budget": [],
        "expenses": [],
        "goals": []
    }

    budgets = session.query(Budget).filter(Budget.user_id == user.id).all()
    expenses = session.query(Expense).filter(Expense.user_id == user.id).all()
    goals = session.query(Goal).filter(Goal.user_id == user.id).all()

    for budget in budgets:
        user_data["budget"].append({
            "name": budget.budget_name,
            "amount": budget.budget_amount,
            "income": budget.budget_income
        })

    for expense in expenses:
        user_data["expenses"].append({
            "name": expense.expense_name,
            "amount": expense.expense_amount
        })

    for goal in goals:
        user_data["goals"].append({
            "name": goal.goal_name,
            "amount": goal.goal_amount
        })

    session.close()
    return user_data

add_user("testuser", "12345678")