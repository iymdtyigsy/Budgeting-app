from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
import bcrypt

# Database setup
Base = declarative_base()
engine = create_engine('sqlite:///user_database3.db', echo=False)
Session = sessionmaker(bind=engine)

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password_hash = Column(String(100), nullable=False)
    
    def set_password(self, password):
        """Hash password with bcrypt"""
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode(), salt).decode()
    
    def check_password(self, password):
        """Verify password against stored hash"""
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())

# Create tables if they don't exist
Base.metadata.create_all(engine)

def create_user(username, email, password):
    """Create a new user in the database"""
    session = Session()
    try:
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        session.add(new_user)
        session.commit()
        return True, "Registration successful!"
    except IntegrityError:
        session.rollback()
        return False, "Username or email already exists"
    finally:
        session.close()

def authenticate_user(username, password):
    """Authenticate user credentials"""
    session = Session()
    try:
        user = session.query(User).filter(User.username == username).first()
        if user and user.check_password(password):
            return True, "Login successful!"
        return False, "Invalid username or password"
    finally:
        session.close()

def get_all_users():
    """Get all users (for debugging)"""
    session = Session()
    try:
        return session.query(User).all()
    finally:
        session.close()
