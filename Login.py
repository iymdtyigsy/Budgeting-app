import tkinter as tk
import sqlite3
from Database import conn, c

import customtkinter as ctk

class LoginMenu(ctk.CTk):

    def __init__(self):
        """Initialize the log in window."""
        super().__init__()

        self.title("Budget app")
        self.geometry("844x844")
        self.minsize(844, 844)
        self.maxsize(844, 844)

        self.mainframe = ctk.CTkFrame(
        self, fg_color="black", width=744, height=744)
        self.mainframe.pack(fill="both", expand=True)

        self.mainframe_holder = ctk.CTkFrame(
        self.mainframe, fg_color="#D9D9D9", width=644, height=644)
        self.mainframe_holder.pack(padx=10, pady=10, fill="both", expand=True)

        self.load_login_menu()
    
    def signup(self):
<<<<<<< Updated upstream
        username = self.signupframe_username.cget()
        password = self.signupframe_password.cget()
=======
        username = self.signupframe_username.cget("text")
        password = self.signupframe_password.cget("text")
>>>>>>> Stashed changes

    def delete_current(self):
        """Delete the current menu."""
        for widget in self.mainframe_holder.winfo_children():
            widget.forget()

    def switch_login(self):
        #trial
        self.delete_current()
        self.load_login_menu()

    def switch_signup(self):
        #trial
        self.delete_current()
        self.load_signup_menu()

    def load_login_menu(self):

        self.loginframe = ctk.CTkFrame(
        self.mainframe_holder, fg_color="white", width=605, height=500)
        self.loginframe.pack(padx=10, pady=10, expand=True)
        self.loginframe.pack_propagate(False)

        self.loginframe_label = ctk.CTkLabel(
        self.loginframe, text="LOG IN", text_color="black", fg_color="#FFFEFE",
        width=200, height=25, font=("Bold", 60), corner_radius=5)
        self.loginframe_label.pack(pady=25)
            
        self.loginframe_username = ctk.CTkEntry(
        self.loginframe, placeholder_text="username", placeholder_text_color= "black", 
        text_color="black", fg_color="#D9D9D9", width=300, height=50)
        self.loginframe_username.pack(padx=50, pady=25)

        self.loginframe_password = ctk.CTkEntry(
        self.loginframe, placeholder_text="password", placeholder_text_color= "black", 
        text_color="black", width=300, height=50, fg_color="#D9D9D9")
        self.loginframe_password.pack(padx=50)

        self.loginframe_loginbtn = ctk.CTkButton(
        self.loginframe, text="LOG IN", text_color="black", width=200, height= 50, 
        fg_color="#D9D9D9")
        self.loginframe_loginbtn.pack(padx=50, pady=25)

        self.loginframe_switchbtn = ctk.CTkButton(
        self.loginframe, text="or signup", text_color="black", width=200, height= 50, 
        fg_color="#D9D9D9", command=self.switch_signup)
        self.loginframe_switchbtn.pack()
    
    def load_signup_menu(self):

        self.signupframe = ctk.CTkFrame(
        self.mainframe_holder, fg_color="white", width=605, height=500)
        self.signupframe.pack(padx=10, pady=10, expand=True)
        self.signupframe.pack_propagate(False)

        self.signupframe_label = ctk.CTkLabel(
        self.signupframe, text="SIGN UP", text_color="black", fg_color="#FFFEFE",
        width=200, height=25, font=("Bold", 60), corner_radius=5)
        self.signupframe_label.pack(pady=25)
            
        self.signupframe_username = ctk.CTkEntry(
        self.signupframe, placeholder_text="username", placeholder_text_color= "black", 
        text_color="black", fg_color="#D9D9D9", width=300, height=50)
        self.signupframe_username.pack(padx=50, pady=25)

        self.signupframe_password = ctk.CTkEntry(
        self.signupframe, placeholder_text="password", placeholder_text_color= "black", 
        text_color="black", width=300, height=50, fg_color="#D9D9D9")
        self.signupframe_password.pack(padx=50)

        self.signupframe_signupbtn = ctk.CTkButton(
        self.signupframe, text="SIGN UP", text_color="black", width=200, height= 50, 
        fg_color="#D9D9D9")
        self.signupframe_signupbtn.pack(padx=50, pady=25)

        self.signupframe_switchbtn = ctk.CTkButton(
        self.signupframe, text="or login", text_color="black", width=200, height= 50, 
        fg_color="#D9D9D9", command=self.switch_login)
        self.signupframe_switchbtn.pack()

if __name__ == "__main__":
    LoginMenu().mainloop()
    
        
    