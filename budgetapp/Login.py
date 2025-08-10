import customtkinter as ctk
from Database import add_user, auth_user
from Budget import BudgetMenu

class LoginMenu(ctk.CTk):
    def __init__(self):
        """Initialize the log in window."""
        super().__init__()

        self.title("Budget app")
        self.geometry("844x844")
        self.maxsize(844, 844)
        self.minsize(844, 844)

        self.mainframe = ctk.CTkFrame(
            self, 
            fg_color="black", 
            width=744, 
            height=744
        )
        self.mainframe.pack(fill="both", expand=True)

        self.mainframe_holder = ctk.CTkFrame(
            self.mainframe, 
            fg_color="#D9D9D9", 
            width=644, 
            height=644
        )
        self.mainframe_holder.pack(padx=10, pady=10, fill="both", expand=True)

        self.load_login_menu()
        
    def delete_current(self):
        """Delete the current menu."""
        for widget in self.mainframe_holder.winfo_children():
            widget.forget()
       
    def load_login_menu(self):
        """Load the login menu widgets."""
        self.delete_current()

        self.loginframe = ctk.CTkFrame(
            self.mainframe_holder, 
            fg_color="white", 
            width=605, 
            height=500
        )
        self.loginframe.pack(padx=10, pady=10, expand=True)
        self.loginframe.pack_propagate(False)

        self.loginframe_label = ctk.CTkLabel(
            self.loginframe, 
            text="LOG IN", 
            text_color="black", 
            fg_color="#FFFEFE",
            width=200, 
            height=25, 
            font=("Bold", 60), 
            corner_radius=5
        )
        self.loginframe_label.pack(pady=25)
            
        self.loginframe_username = ctk.CTkEntry(
            self.loginframe, 
            placeholder_text="username", 
            placeholder_text_color= "black", 
            text_color="black", 
            fg_color="#D9D9D9", 
            width=300, 
            height=50
        )
        self.loginframe_username.pack(padx=50, pady=10)

        self.loginframe_password = ctk.CTkEntry(
            self.loginframe, 
            placeholder_text="password", 
            placeholder_text_color= "black", 
            text_color="black", 
            width=300, 
            height=50, 
            fg_color="#D9D9D9", 
            show="*"
        )
        self.loginframe_password.pack(padx=50, pady=10)
        
        self.loginframe_status_label = ctk.CTkLabel(
            self.loginframe, 
            text = "", 
            text_color="red"
        )
        self.loginframe_status_label.pack()

        self.loginframe_loginbtn = ctk.CTkButton(
            self.loginframe, 
            text="LOG IN", 
            text_color="black", 
            width=200, 
            height= 50, 
            fg_color="#D9D9D9", 
            command=self.login_user
        )
        self.loginframe_loginbtn.pack(padx=50, pady=10)

        self.loginframe_switchbtn = ctk.CTkButton(
            self.loginframe, 
            text="or signup", 
            text_color="black", 
            width=200, 
            height= 30, 
            fg_color="#D9D9D9", 
            command=self.load_signup_menu
        )
        self.loginframe_switchbtn.pack()
    
    def load_signup_menu(self):
        """Load the signup menu widgets."""
        self.delete_current()

        self.signupframe = ctk.CTkFrame(
            self.mainframe_holder, 
            fg_color="white", 
            width=605, 
            height=500
        )
        self.signupframe.pack(padx=10, pady=10, expand=True)
        self.signupframe.pack_propagate(False)

        self.signupframe_label = ctk.CTkLabel(
            self.signupframe, 
            text="SIGN UP", 
            text_color="black", 
            fg_color="#FFFEFE",
            width=200, 
            height=25, 
            font=("Bold", 60), 
            corner_radius=5
        )
        self.signupframe_label.pack(pady=25)
            
        self.signupframe_username = ctk.CTkEntry(
            self.signupframe, 
            placeholder_text="username", 
            placeholder_text_color= "black", 
            text_color="black", 
            fg_color="#D9D9D9", 
            width=300, 
            height=50
        )
        self.signupframe_username.pack(padx=50, pady=5)

        self.signupframe_password = ctk.CTkEntry(
            self.signupframe, 
            placeholder_text="password", 
            placeholder_text_color= "black", 
            text_color="black", 
            width=300, 
            height=50, 
            fg_color="#D9D9D9", 
            show="*"
        )
        self.signupframe_password.pack(padx=50, pady=5)

        self.signupframe_confirmpassword = ctk.CTkEntry(
            self.signupframe, 
            placeholder_text="confirm password", 
            placeholder_text_color= "black", 
            text_color="black", 
            width=300, 
            height=50, 
            fg_color="#D9D9D9", 
            show="*"
        )
        self.signupframe_confirmpassword.pack(padx=50, pady=5)

        self.signupframe_status_label = ctk.CTkLabel(
            self.signupframe, 
            text = "", 
            text_color="red"
        )
        self.signupframe_status_label.pack()

        self.signupframe_signupbtn = ctk.CTkButton(
            self.signupframe, 
            text="SIGN UP", 
            text_color="black", 
            width=200, 
            height= 50, 
            fg_color="#D9D9D9", 
            command=self.register_user
        )
        self.signupframe_signupbtn.pack(padx=50, pady=10)

        self.signupframe_switchbtn = ctk.CTkButton(
            self.signupframe, 
            text="or login", 
            text_color="black", 
            width=200, 
            height= 30, 
            fg_color="#D9D9D9", 
            command=self.load_login_menu
        )
        self.signupframe_switchbtn.pack()

    def register_user(self):
        """Register a new user."""
        username = self.signupframe_username.get().strip()
        password = self.signupframe_password.get()
        confirm = self.signupframe_confirmpassword.get()

        if not all([username, password, confirm]):
            self.signupframe_status_label.configure(text="Fill in the username, password, and confirm password")
            return
        
        if len(password) <8:
            self.signupframe_status_label.configure(text="password need to be atleast 8 letters")
            return
        
        if confirm != password:
            self.signupframe_status_label.configure(text ="confirm password does not match")
            return
        
        success, message = add_user(username, password)
        if success:
            self.signupframe_status_label.configure(text=message, text_color="green")
            self.after(300, self.load_login_menu)
        else:
            self.signupframe_status_label.configure(text=message)
    
    def login_user(self):
        """Login a user."""
        username = self.loginframe_username.get().strip()
        password = self.loginframe_password.get()

        if not username or not password:
            self.loginframe_status_label.configure(text="Fill in the username and password")
            return
        
        success, message = auth_user(username, password)
        if success:
            self.loginframe_status_label.configure(text=message, text_color="green")
            self.destroy()
            BudgetMenu(username).mainloop()
        else:
            self.loginframe_status_label.configure(text=message)
    
if __name__ == "__main__":
    LoginMenu().mainloop()
