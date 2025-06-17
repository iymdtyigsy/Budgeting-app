import customtkinter as ctk
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError
import bcrypt
import re

# ==============================
# DATABASE SETUP (SQLAlchemy)
# ==============================
Base = declarative_base()
engine = create_engine('sqlite:///user_database2.db', echo=False)
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

# ==============================
# GUI SETUP (CustomTkinter)
# ==============================
class LoginSystem(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Secure Login System")
        self.geometry("400x500")
        self.resizable(False, False)
        
        # Configure theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")
        
        # Create main container
        self.container = ctk.CTkFrame(self)
        self.container.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Show login screen initially
        self.show_login_screen()

    def clear_frame(self):
        """Clear current screen"""
        for widget in self.container.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        """Display login interface"""
        self.clear_frame()
        
        # Create widgets
        title = ctk.CTkLabel(self.container, text="Login", font=("Arial", 24))
        title.pack(pady=20)
        
        # Username field
        username_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        username_frame.pack(fill="x", padx=50, pady=5)
        ctk.CTkLabel(username_frame, text="Username:").pack(side="left")
        self.username_entry = ctk.CTkEntry(username_frame)
        self.username_entry.pack(side="right", expand=True, fill="x")
        
        # Password field
        password_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        password_frame.pack(fill="x", padx=50, pady=5)
        ctk.CTkLabel(password_frame, text="Password:").pack(side="left")
        self.password_entry = ctk.CTkEntry(password_frame, show="*")
        self.password_entry.pack(side="right", expand=True, fill="x")
        
        # Login button
        login_btn = ctk.CTkButton(self.container, text="Login", command=self.login)
        login_btn.pack(pady=20)
        
        # Status label
        self.status_label = ctk.CTkLabel(self.container, text="", text_color="red")
        self.status_label.pack(pady=5)
        
        # Register link
        register_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        register_frame.pack(fill="x", pady=10)
        ctk.CTkLabel(register_frame, text="Don't have an account?").pack(side="left")
        register_link = ctk.CTkButton(
            register_frame, 
            text="Register", 
            command=self.show_register_screen,
            fg_color="transparent",
            hover_color="#2b2b2b"
        )
        register_link.pack(side="right")

    def show_register_screen(self):
        """Display registration interface"""
        self.clear_frame()
        
        # Create widgets
        title = ctk.CTkLabel(self.container, text="Register", font=("Arial", 24))
        title.pack(pady=20)
        
        # Username field
        username_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        username_frame.pack(fill="x", padx=50, pady=5)
        ctk.CTkLabel(username_frame, text="Username:").pack(side="left")
        self.reg_username = ctk.CTkEntry(username_frame)
        self.reg_username.pack(side="right", expand=True, fill="x")
        
        # Email field
        email_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        email_frame.pack(fill="x", padx=50, pady=5)
        ctk.CTkLabel(email_frame, text="Email:").pack(side="left")
        self.reg_email = ctk.CTkEntry(email_frame)
        self.reg_email.pack(side="right", expand=True, fill="x")
        
        # Password field
        password_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        password_frame.pack(fill="x", padx=50, pady=5)
        ctk.CTkLabel(password_frame, text="Password:").pack(side="left")
        self.reg_password = ctk.CTkEntry(password_frame, show="*")
        self.reg_password.pack(side="right", expand=True, fill="x")
        
        # Confirm Password field
        confirm_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        confirm_frame.pack(fill="x", padx=50, pady=5)
        ctk.CTkLabel(confirm_frame, text="Confirm:").pack(side="left")
        self.reg_confirm = ctk.CTkEntry(confirm_frame, show="*")
        self.reg_confirm.pack(side="right", expand=True, fill="x")
        
        # Register button
        register_btn = ctk.CTkButton(self.container, text="Register", command=self.register)
        register_btn.pack(pady=20)
        
        # Status label
        self.reg_status = ctk.CTkLabel(self.container, text="", text_color="red")
        self.reg_status.pack(pady=5)
        
        # Back to login link
        back_frame = ctk.CTkFrame(self.container, fg_color="transparent")
        back_frame.pack(fill="x", pady=10)
        ctk.CTkLabel(back_frame, text="Already have an account?").pack(side="left")
        login_link = ctk.CTkButton(
            back_frame, 
            text="Login", 
            command=self.show_login_screen,
            fg_color="transparent",
            hover_color="#2b2b2b"
        )
        login_link.pack(side="right")

    def login(self):
        """Handle login attempt"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            self.status_label.configure(text="Please fill all fields")
            return
            
        session = Session()
        user = session.query(User).filter(User.username == username).first()
        session.close()
        
        if user and user.check_password(password):
            self.status_label.configure(text="Login successful!", text_color="green")
            # Here you would typically open the main application window
        else:
            self.status_label.configure(text="Invalid username or password")

    def register(self):
        """Handle new registration"""
        username = self.reg_username.get().strip()
        email = self.reg_email.get().strip()
        password = self.reg_password.get()
        confirm = self.reg_confirm.get()
        
        # Validation checks
        if not all([username, email, password, confirm]):
            self.reg_status.configure(text="All fields are required")
            return
            
        if password != confirm:
            self.reg_status.configure(text="Passwords do not match")
            return
            
        if len(password) < 8:
            self.reg_status.configure(text="Password must be 8+ characters")
            return
            
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.reg_status.configure(text="Invalid email format")
            return
            
        # Create new user
        new_user = User(username=username, email=email)
        new_user.set_password(password)
        
        session = Session()
        try:
            session.add(new_user)
            session.commit()
            self.reg_status.configure(text="Registration successful!", text_color="green")
            # Automatically switch to login after 2 seconds
            self.after(2000, self.show_login_screen)
        except IntegrityError:
            session.rollback()
            self.reg_status.configure(text="Username or email already exists")
        finally:
            session.close()

# ==============================
# RUN APPLICATION
# ==============================
if __name__ == "__main__":
    app = LoginSystem()
    app.mainloop()