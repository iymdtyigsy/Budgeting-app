"""
This is the database module for the Budget App.
"""
from sqlalchemy import Column, Float, Integer, String, ForeignKey, Sequence, UniqueConstraint, create_engine
from sqlalchemy.orm import sessionmaker, relationship, declarative_base
from sqlalchemy.exc import IntegrityError
import bcrypt
import datetime

engine = create_engine('sqlite:///account.db', echo=False)
Session = sessionmaker(bind=engine)
Base = declarative_base()

class User(Base):
    """User model for the database."""
    __tablename__ = 'user'

    id = Column(Integer, Sequence('user_id_seq'), primary_key=True)
    username = Column(String(30), unique=True, nullable=False)
    hashedpassword = Column(String(256), nullable=False)

    budget = relationship("Budget", back_populates="user")
    expense = relationship("Expense", back_populates="user")
    goal = relationship("Goal", back_populates="user")

    def hashpassword(self, password):
        """Hash a password and store it."""
        salt = bcrypt.gensalt()
        bytes = password.encode()
        self.hashedpassword = bcrypt.hashpw(bytes, salt).decode()

    def checkpassword(self, password):
        """Check if a password is correct."""
        bytes = password.encode()
        return bcrypt.checkpw(bytes, self.hashedpassword.encode())

class Budget(Base):
    """Budget model for the database."""
    __tablename__ = 'budget'

    id = Column(Integer, Sequence('budget_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    budget_name = Column(String, nullable=False)
    budget_amount = Column(Integer, nullable=False)
    budget_income = Column(Integer, nullable=False)
    balance = Column(Integer, nullable=False)
    last_updated = Column(String, nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'budget_name', name='unique_user_budget_name'),
    )

    user = relationship("User", back_populates="budget")

class Expense(Base):
    """Expense model for the database."""
    __tablename__ = 'expense'

    id = Column(Integer, Sequence('expense_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    expense_name = Column(String, nullable=False)
    expense_amount = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'expense_name', name='unique_user_expense_name'),
    )

    user = relationship("User", back_populates="expense")

class Goal(Base):
    """Goal model for the database."""
    __tablename__ = 'goal'

    id = Column(Integer, Sequence('goal_id_seq'), primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    goal_name = Column(String, nullable=False)
    goal_amount = Column(Integer, nullable=False)

    __table_args__ = (
        UniqueConstraint('user_id', 'goal_name', name='unique_user_goal_name'),
    )

    user = relationship("User", back_populates="goal")

Base.metadata.create_all(engine)

def add_user(username, password):
    """Add a new user to the database.

    Args:
        username (str): The username of the new user.
        password (str): The password of the new user.

    Returns:
        tuple: A tuple containing a boolean indicating success and a message.
    """
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
    """Authenticate a user.

    Args:
        username (str): The username of the user.
        password (str): The password of the user.

    Returns:
        tuple: A tuple containing a boolean indicating success and a message.
    """
    session = Session()

    try:
        user = session.query(User).filter(User.username == username).first()
        if user and user.checkpassword(password):
            return True, "Login successfully"
        return False, "Wrong username or password"
    finally:
        session.close()

def check_budget(username):
    """Check if a user has a budget.

    Args:
        username (str): The username of the user.

    Returns:
        bool: True if the user has a budget, False otherwise.
    """
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
    """Add a new budget for a user.

    Args:
        username (str): The username of the user.
        name (str): The name of the budget.
        amount (int): The amount of the budget.
        income (int): The income for the budget.

    Returns:
        tuple: A tuple containing a boolean indicating success and a message.
    """
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    try:
        new_budget = Budget(user_id = user.id, budget_name = name, budget_amount = amount, budget_income = income, balance=amount, last_updated=datetime.date.today().isoformat())
        session.add(new_budget)
        session.commit()
        return True, 'added'
    except IntegrityError:
        session.rollback()
        return False, "Budget name already exist"
    finally:
        session.close()

def add_expenses(username, name, amount):
    """Add a new expense for a user.

    Args:
        username (str): The username of the user.
        name (str): The name of the expense.
        amount (int): The amount of the expense.

    Returns:
        tuple: A tuple containing a boolean indicating success and a message.
    """
    session = Session()
    user = session.query(User).filter(User.username == username).first()
    budget = session.query(Budget).filter(Budget.user_id == user.id).first()

    if not user or not budget:
        session.close()
        return False, "User or budget not found"

    try:
        new_expense = Expense(user_id = user.id, expense_name = name, expense_amount = amount)
        session.add(new_expense)
        budget.balance -= int(amount)
        session.commit()
        return True, "added"
    except IntegrityError:
        session.rollback()
        return False, "Expense name already exist"
    finally:
        session.close()

def get_expense(username):
    """Get all expenses for a user.

    Args:
        username (str): The username of the user.

    Returns:
        list: A list of Expense objects.
    """
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    if not user:
        session.close()
        return []
    
    expenses = session.query(Expense).filter(Expense.user_id == user.id).all()
    session.close()
    return expenses

def add_goal(username, name, amount):
    """Add a new goal for a user.

    Args:
        username (str): The username of the user.
        name (str): The name of the goal.
        amount (int): The amount of the goal.

    Returns:
        tuple: A tuple containing a boolean indicating success and a message.
    """
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
    """Get all data for a user.

    Args:
        username (str): The username of the user.

    Returns:
        dict: A dictionary containing all user data.
    """
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
            "income": budget.budget_income,
            "balance": budget.balance,
            "last_updated": budget.last_updated
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

def delete_expense(username, expense_name):
    """Delete an expense for a user.

    Args:
        username (str): The username of the user.
        expense_name (str): The name of the expense to delete.

    Returns:
        tuple: A tuple containing a boolean indicating success and a message.
    """
    session = Session()
    user = session.query(User).filter(User.username == username).first()
    budget = session.query(Budget).filter(Budget.user_id == user.id).first()

    if not user or not budget:
        session.close()
        return False, "User or budget not found"

    try:
        expense = session.query(Expense).filter(Expense.user_id == user.id, Expense.expense_name == expense_name).first()
        if expense:
            budget.balance += expense.expense_amount
            session.delete(expense)
            session.commit()
            return True, "Expense deleted"
        return False, "Expense not found"
    except Exception as e:
        session.rollback()
        return False, str(e)
    finally:
        session.close()

def edit_expense(username, old_name, new_name, new_amount):
    """Edit an expense for a user.

    Args:
        username (str): The username of the user.
        old_name (str): The old name of the expense.
        new_name (str): The new name of the expense.
        new_amount (int): The new amount of the expense.

    Returns:
        tuple: A tuple containing a boolean indicating success and a message.
    """
    session = Session()
    user = session.query(User).filter(User.username == username).first()
    budget = session.query(Budget).filter(Budget.user_id == user.id).first()

    if not user or not budget:
        session.close()
        return False, "User or budget not found"

    try:
        expense = session.query(Expense).filter(Expense.user_id == user.id, Expense.expense_name == old_name).first()
        if expense:
            budget.balance += expense.expense_amount
            expense.expense_name = new_name
            expense.expense_amount = new_amount
            budget.balance -= new_amount
            session.commit()
            return True, "Expense updated"
        return False, "Expense not found"
    except IntegrityError:
        session.rollback()
        return False, "Expense name already exists"
    except Exception as e:
        session.rollback()
        return False, str(e)
    finally:
        session.close()

def edit_budget(username, old_name, new_name, new_amount, new_income):
    """Edit a budget for a user.

    Args:
        username (str): The username of the user.
        old_name (str): The old name of the budget.
        new_name (str): The new name of the budget.
        new_amount (int): The new amount of the budget.
        new_income (int): The new income for the budget.

    Returns:
        tuple: A tuple containing a boolean indicating success and a message.
    """
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    if not user:
        session.close()
        return False, "User not found"

    try:
        budget = session.query(Budget).filter(Budget.user_id == user.id, Budget.budget_name == old_name ).first()
        if budget:
            budget.balance -= budget.budget_amount
            budget.balance += int(new_amount)
            budget.budget_name = new_name
            budget.budget_amount = new_amount
            budget.budget_income = new_income
            session.commit()
            return True, "Budget updated"
        return False, "Budget not found"
    except IntegrityError:
        session.rollback()
        return False, "Budget name already exists"
    except Exception as e:
        session.rollback()
        return False, str(e)
    finally:
        session.close()

def edit_goal(username, old_name, new_name, new_amount):
    """Edit a goal for a user.

    Args:
        username (str): The username of the user.
        old_name (str): The old name of the goal.
        new_name (str): The new name of the goal.
        new_amount (int): The new amount of the goal.

    Returns:
        tuple: A tuple containing a boolean indicating success and a message.
    """
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    if not user:
        session.close()
        return False, "User not found"

    try:
        goal = session.query(Goal).filter(Goal.user_id == user.id, Goal.goal_name == old_name).first()
        if goal:
            goal.goal_name = new_name
            goal.goal_amount = new_amount
            session.commit()
            return True, "Goal updated"
        return False, "Goal not found"
    except IntegrityError:
        session.rollback()
        return False, "Goal name already exists"
    except Exception as e:
        session.rollback()
        return False, str(e)
    finally:
        session.close()

def update_budget_balance(username):
    """Update the budget balance based on income and expenses.

    Args:
        username (str): The username of the user.
    """
    session = Session()
    user = session.query(User).filter(User.username == username).first()

    if not user:
        session.close()
        return

    budget = session.query(Budget).filter(Budget.user_id == user.id).first()
    if not budget:
        session.close()
        return

    today = datetime.date.today()
    last_updated = datetime.date.fromisoformat(budget.last_updated)
    
    months_passed = (today.year - last_updated.year) * 12 + (today.month - last_updated.month)

    if months_passed > 0:
        expenses = session.query(Expense).filter(Expense.user_id == user.id).all()
        total_expenses = sum(expense.expense_amount for expense in expenses)
        
        budget.balance += (budget.budget_income - total_expenses) * months_passed
        budget.last_updated = today.isoformat()
        session.commit()

    session.close()
