import tkinter as tk

import customtkinter as ctk
import mysql.connector

class LoginMenu(ctk.CTk):

    #def load_main_menu(self):

    def __init__(self):
        """Initialize the log in window."""
        super().__init__()

        self.title("Budget app")
        self.geometry("700x500")
        self.minsize(700, 500)
        self.maxsize(700, 500)

        self.mainframe = ctk.CTkFrame(self, fg_color="black",
                                      width=700,
                                      height=500)
        self.mainframe.pack(fill="both",
                            expand=True)

        self.main_frame_label = (ctk.CTkLabel
                                 (self.mainframe,
                                  text="Login",
                                  text_color="white",
                                  fg_color="#01a6f8",
                                  width=200, height=25,
                                  font=("Bold", 20),
                                  corner_radius=5))
        self.main_frame_label.pack(padx=10,
                                   pady=10)

        self.main_frame_holder = ctk.CTkFrame(self.mainframe,
                                              width=600,
                                              height=400)
        self.main_frame_holder.pack(padx=10,
                                    pady=10,
                                    fill="both",
                                    expand=True)

        #self.load_main_menu()
    
if __name__ == "__main__":
    LoginMenu().mainloop()
    
        
    