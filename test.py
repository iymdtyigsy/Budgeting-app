import bcrypt
import customtkinter as ctk
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

# Database Setup
Base = declarative_base()
engine = create_engine('sqlite:///user_database.db')
Session = sessionmaker(bind=engine)

# User Model
class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    password_hash = Column(String(60), nullable=False)  # bcrypt hash storage
    
    def set_password(self, password):
        """Hash and store password"""
        salt = bcrypt.gensalt()
        self.password_hash = bcrypt.hashpw(password.encode(), salt).decode()
    
    def check_password(self, password):
        """Verify password against stored hash"""
        return bcrypt.checkpw(password.encode(), self.password_hash.encode())

# Create tables
Base.metadata.create_all(engine)

# GUI Application
class LoginApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        # Window Configuration
        self.title("Secure Login System")
        self.geometry("500x400")
        self.resizable(False, False)
        
        # Theme Configuration
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("green")
        
        # Create Main Frame
        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(fill="both", expand=True, padx=20, pady=20)
        
        # Show Login Screen by Default
        self.show_login_screen()
    
    def clear_frame(self):
        """Clear all widgets from main frame"""
        for widget in self.main_frame.winfo_children():
            widget.destroy()
    
    def show_login_screen(self):
        """Display login form"""
        self.clear_frame()
        
        # Title
        ctk.CTkLabel(
            self.main_frame, 
            text="Login to Your Account",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 30))
        
        # Username Field
        ctk.CTkLabel(self.main_frame, text="Username:").pack()
        self.username_entry = ctk.CTkEntry(self.main_frame, width=250)
        self.username_entry.pack(pady=(0, 15))
        
        # Password Field
        ctk.CTkLabel(self.main_frame, text="Password:").pack()
        self.password_entry = ctk.CTkEntry(
            self.main_frame, 
            width=250, 
            show="•"
        )
        self.password_entry.pack(pady=(0, 20))
        
        # Login Button
        login_btn = ctk.CTkButton(
            self.main_frame,
            text="Login",
            command=self.authenticate_user,
            width=200,
            height=40
        )
        login_btn.pack(pady=(0, 10))
        
        # Register Link
        register_link = ctk.CTkButton(
            self.main_frame,
            text="Don't have an account? Register",
            fg_color="transparent",
            hover_color="#2b2b2b",
            command=self.show_register_screen,
            width=200
        )
        register_link.pack()
        
        # Status Label
        self.status_label = ctk.CTkLabel(self.main_frame, text="", text_color="#ff5555")
        self.status_label.pack(pady=(15, 0))
    
    def show_register_screen(self):
        """Display registration form"""
        self.clear_frame()
        
        # Title
        ctk.CTkLabel(
            self.main_frame, 
            text="Create New Account",
            font=("Arial", 20, "bold")
        ).pack(pady=(20, 30))
        
        # Username Field
        ctk.CTkLabel(self.main_frame, text="Username:").pack()
        self.reg_username_entry = ctk.CTkEntry(self.main_frame, width=250)
        self.reg_username_entry.pack(pady=(0, 10))
        
        # Password Field
        ctk.CTkLabel(self.main_frame, text="Password:").pack()
        self.reg_password_entry = ctk.CTkEntry(
            self.main_frame, 
            width=250, 
            show="•"
        )
        self.reg_password_entry.pack(pady=(0, 10))
        
        # Confirm Password
        ctk.CTkLabel(self.main_frame, text="Confirm Password:").pack()
        self.reg_confirm_entry = ctk.CTkEntry(
            self.main_frame, 
            width=250, 
            show="•"
        )
        self.reg_confirm_entry.pack(pady=(0, 20))
        
        # Register Button
        register_btn = ctk.CTkButton(
            self.main_frame,
            text="Create Account",
            command=self.register_user,
            width=200,
            height=40
        )
        register_btn.pack(pady=(0, 10))
        
        # Back to Login
        back_btn = ctk.CTkButton(
            self.main_frame,
            text="Back to Login",
            fg_color="transparent",
            hover_color="#2b2b2b",
            command=self.show_login_screen,
            width=200
        )
        back_btn.pack()
        
        # Status Label
        self.reg_status_label = ctk.CTkLabel(
            self.main_frame, 
            text="", 
            text_color="#ff5555"
        )
        self.reg_status_label.pack(pady=(15, 0))
    
    def register_user(self):
        """Handle user registration"""
        username = self.reg_username_entry.get().strip()
        password = self.reg_password_entry.get()
        confirm = self.reg_confirm_entry.get()
        
        # Validation
        if not username or not password:
            self.reg_status_label.configure(text="All fields are required")
            return
        
        if len(username) < 4:
            self.reg_status_label.configure(text="Username must be at least 4 characters")
            return
            
        if len(password) < 8:
            self.reg_status_label.configure(text="Password must be at least 8 characters")
            return
            
        if password != confirm:
            self.reg_status_label.configure(text="Passwords do not match")
            return
        
        # Create new user
        session = Session()
        try:
            new_user = User(username=username)
            new_user.set_password(password)
            session.add(new_user)
            session.commit()
            self.show_login_screen()
            self.status_label.configure(
                text="Registration successful! Please login",
                text_color="#55ff55"
            )
        except IntegrityError:
            self.reg_status_label.configure(text="Username already exists")
        finally:
            session.close()
    
    def authenticate_user(self):
        """Authenticate user credentials"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            self.status_label.configure(text="Please enter both fields")
            return
        
        session = Session()
        try:
            user = session.query(User).filter_by(username=username).first()
            
            if user and user.check_password(password):
                self.status_label.configure(
                    text="Login successful!",
                    text_color="#55ff55"
                )
                # Here you would typically open the main application window
                # self.open_main_app(user)
            else:
                self.status_label.configure(text="Invalid username or password")
        finally:
            session.close()

# Run the application
if __name__ == "__main__":
    app = LoginApp()
    app.mainloop()