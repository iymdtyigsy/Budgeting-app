import tkinter as tk

import customtkinter as ctk
import mysql.connector

class LoginMenu(ctk.CTk):

    #def load_main_menu(self):

    def __init__(self):
        """Initialize the log in window."""
        super().__init__()

        self.title("Budget app")
        self.geometry("844x844")
        self.minsize(844, 844)
        self.maxsize(844, 844)

        self.mainframe = ctk.CTkFrame(self,
                                      fg_color="black",
                                      width=744,
                                      height=744)
        self.mainframe.pack(fill="both",
                            expand=True)

        self.mainframe_holder = ctk.CTkFrame(self.mainframe, 
                                             fg_color="#D9D9D9",
                                             width=644,
                                             height=644)
        self.mainframe_holder.pack(padx=10,
                                   pady=10,
                                   fill="both",
                                   expand=True)

        self.loginframe = ctk.CTkFrame(self.mainframe_holder,
                                       fg_color="white",
                                       width=605,
                                       height=500)
        self.loginframe.pack(padx=10,
                             pady=10,
                             expand=True)
        self.loginframe.pack_propagate(False)

        self.loginframe_label = ctk.CTkLabel(self.loginframe,
                                             text="LOG IN",
                                             text_color="black",
                                             fg_color="#FFFEFE",
                                             width=200, 
                                             height=25,
                                             font=("Bold", 20),
                                             corner_radius=5)
        self.loginframe_label.pack(padx=10,
                                   pady=10,
                                   expand=True)
        

        #self.load_main_menu()
    
if __name__ == "__main__":
    LoginMenu().mainloop()
    
        
    