import customtkinter as ctk
import re
from testdatabase import create_user, authenticate_user

class LoginSystem(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("Secure Login System")
        self.geometry("400x500")
        
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
        ctk.CTkLabel(self.container, text="Username:").pack(anchor="w", padx=50, pady=(10, 0))
        self.username_entry = ctk.CTkEntry(self.container)
        self.username_entry.pack(padx=50, fill="x")
        
        # Password field
        ctk.CTkLabel(self.container, text="Password:").pack(anchor="w", padx=50, pady=(10, 0))
        self.password_entry = ctk.CTkEntry(self.container, show="*")
        self.password_entry.pack(padx=50, fill="x")
        
        # Login button
        login_btn = ctk.CTkButton(self.container, text="Login", command=self.login)
        login_btn.pack(pady=20)
        
        # Status label
        self.status_label = ctk.CTkLabel(self.container, text="", text_color="red")
        self.status_label.pack()
        
        # Register link
        register_btn = ctk.CTkButton(
            self.container, 
            text="Create New Account", 
            command=self.show_register_screen,
            fg_color="transparent",
            hover_color="#2b2b2b"
        )
        register_btn.pack(pady=10)

    def show_register_screen(self):
        """Display registration interface"""
        self.clear_frame()
        
        # Create widgets
        title = ctk.CTkLabel(self.container, text="Register", font=("Arial", 24))
        title.pack(pady=20)
        
        # Username field
        ctk.CTkLabel(self.container, text="Username:").pack(anchor="w", padx=50, pady=(10, 0))
        self.reg_username = ctk.CTkEntry(self.container)
        self.reg_username.pack(padx=50, fill="x")
        
        # Email field
        ctk.CTkLabel(self.container, text="Email:").pack(anchor="w", padx=50, pady=(10, 0))
        self.reg_email = ctk.CTkEntry(self.container)
        self.reg_email.pack(padx=50, fill="x")
        
        # Password field
        ctk.CTkLabel(self.container, text="Password:").pack(anchor="w", padx=50, pady=(10, 0))
        self.reg_password = ctk.CTkEntry(self.container, show="*")
        self.reg_password.pack(padx=50, fill="x")
        
        # Confirm Password field
        ctk.CTkLabel(self.container, text="Confirm Password:").pack(anchor="w", padx=50, pady=(10, 0))
        self.reg_confirm = ctk.CTkEntry(self.container, show="*")
        self.reg_confirm.pack(padx=50, fill="x")
        
        # Register button
        register_btn = ctk.CTkButton(self.container, text="Register", command=self.register)
        register_btn.pack(pady=20)
        
        # Status label
        self.reg_status = ctk.CTkLabel(self.container, text="", text_color="red")
        self.reg_status.pack()
        
        # Back to login link
        login_btn = ctk.CTkButton(
            self.container, 
            text="Back to Login", 
            command=self.show_login_screen,
            fg_color="transparent",
            hover_color="#2b2b2b"
        )
        login_btn.pack(pady=10)

    def login(self):
        """Handle login attempt"""
        username = self.username_entry.get().strip()
        password = self.password_entry.get()
        
        if not username or not password:
            self.status_label.configure(text="Please fill all fields")
            return
            
        success, message = authenticate_user(username, password)
        if success:
            self.status_label.configure(text=message, text_color="green")
            # Here you would open the main application window
        else:
            self.status_label.configure(text=message)

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
            self.reg_status.configure(text="Password must be at least 8 characters")
            return
            
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            self.reg_status.configure(text="Invalid email format")
            return
            
        # Create user in database
        success, message = create_user(username, email, password)
        if success:
            self.reg_status.configure(text=message, text_color="green")
            # Automatically switch to login after 2 seconds
            self.after(2000, self.show_login_screen)
        else:
            self.reg_status.configure(text=message)

if __name__ == "__main__":
    app = LoginSystem()
    app.mainloop()